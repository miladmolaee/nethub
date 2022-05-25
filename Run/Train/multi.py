import time
import winsound

import Run.Util.write_training_result as wr
from Engine.mlp import MLP
from Engine.network import Net
from Input.data import Data
from Input.multi_texture import Multi_Texture


class Multi:
    commands: str
    root_path: str

    def set(self, script, root_path):
        self.commands = script
        self.root_path = root_path

    def run(self):
        multi_texture = Multi_Texture()
        multi_texture.make(self.commands)

        ne = []
        af = []

        for m in multi_texture.m_neurons:
            ne.append(len(m))

        for a in multi_texture.m_activations:
            af.append(len(a))

        nk = []
        tem = []

        all_state = 1

        for i in range(len(ne)):
            nk.append(ne[i])
            nk.append(af[i])
            all_state = all_state * ne[i] * af[i]

        for i in range(len(nk)):
            tem.append(1)

        is_ = False
        n = 0

        rows, cols = (len(nk), all_state)

        state = [[0 for i in range(rows)] for j in range(cols)]

        while True:

            for ni in range(len(tem)):
                state[n][ni] = tem[ni]

            n = n + 1
            cn = 0

            for i in range(len(nk)):
                if tem[i] == nk[i]:
                    cn = cn + 1

            if cn == len(nk):
                break

            for i in range(len(tem)):
                j = len(tem) - i - 1

                if tem[j] < nk[j] and is_:
                    tem[j] = tem[j] + 1
                    for k in range(j + 1, len(nk)):
                        tem[k] = 1
                    is_ = False
                    break

                elif tem[j] < nk[j]:
                    tem[j] = tem[j] + 1
                    break

                elif tem[j] == nk[j]:
                    is_ = True

        for i in range(all_state):

            data = Data(root_path=self.root_path, file_name='input.xlsx', test_split=multi_texture.test_split,
                        validation_split=multi_texture.validation_split,
                        input_dim=multi_texture.input_dimension, output_dim=multi_texture.output_dimension)

            net = MLP(parent_directory=self.root_path, run_num=multi_texture.run_number + i + 1, multi_run=False,
                      plot=multi_texture.plot,
                      min_accuracy=multi_texture.min_training_accuracy,
                      min_accuracy_v=multi_texture.min_validation_accuracy,
                      max_loss=multi_texture.max_training_loss, max_loss_v=multi_texture.max_validation_loss,
                      max_epoch=multi_texture.max_epoch, check=multi_texture.check_result)

            net.set_data(data)

            # add layer ----------------------------------------------------------------------------
            net.add_layer(multi_texture.m_neurons[0][state[i][0] - 1],
                          activation_function=multi_texture.m_activations[0][state[i][1] - 1],
                          layer_type=Net.INPUT_LAYER)

            for j in range(int(len(nk) / 2 - 2)):
                if multi_texture.m_neurons[j][state[i][j + 1] - 1] > 0:
                    net.add_layer(multi_texture.m_neurons[j][state[i][j + 1] - 1],
                                  activation_function=multi_texture.m_activations[j][state[i][j + 1] - 1],
                                  layer_type=Net.HIDDEN_LAYER)

            net.add_layer(multi_texture.m_neurons[int(len(nk) / 2) - 1][state[i][len(nk) - 2] - 1],
                          activation_function=multi_texture.m_activations[int(len(nk) / 2) - 1][
                              state[i][len(nk) - 1] - 1],
                          layer_type=Net.OUTPUT_LAYER)
            # --------------------------------------------------------------------------------------------------

            optimizer = Net.optimizers.Adam

            net.compile(optimizer=optimizer)

            if multi_texture.sound:
                winsound.Beep(1000, 500)

            print('\n # starting run number:', i + 1, '/', all_state, '...')
            start_time = time.time()

            net.exe(batch_split=multi_texture.batch_split, verbose=0)

            net.prediction()

            wr.write_final_result(net, _print=False)

            print(' # final result ->  [ run number :', i + 1, ']  -  [ mse :',
                  net.get_final_all_loss(), ']  -  [ R2 :', net.get_final_all_accuracy(),
                  ']  -  [ success :', net.success, ']')

            print(' # run number', i + 1, 'finished after', int(time.time() - start_time), 'second.')

            if net.epoch < multi_texture.max_epoch:

                if net.final_test_accuracy >= multi_texture.min_test_accuracy:

                    if multi_texture.sound:
                        winsound.Beep(1000, 1500)

                    print(' * This run finished with acceptable result.')

                else:

                    if multi_texture.sound:
                        winsound.Beep(1000, 500)

                    print(' * Test Accuracy is not acceptable.')
            else:

                if multi_texture.sound:
                    winsound.Beep(2000, 500)

                # print('>>> # result is not acceptable.')
