import winsound

import Run.Util.write_training_result as wr
from Engine.mlp import MLP
from Engine.network import Net
from Input.data import Data
from Input.texture import Texture


class Single:
    commands: str
    root_path: str

    def set(self, root_path, script):
        self.commands = script
        self.root_path = root_path

    def run(self):

        texture = Texture()
        texture.make(self.commands)

        while True:

            data = Data(root_path=self.root_path, file_name='input.xlsx', test_split=texture.test_split,
                        validation_split=texture.validation_split,
                        input_dim=texture.input_dimension, output_dim=texture.output_dimension,
                        lower_norm=texture.normalization_range[0], upper_norm=texture.normalization_range[1])

            net = MLP(parent_directory=self.root_path, run_num=texture.run_number, multi_run=False, plot=texture.plot,
                      min_accuracy=texture.min_training_accuracy, min_accuracy_v=texture.min_validation_accuracy,
                      max_loss=texture.max_training_loss, max_loss_v=texture.max_validation_loss,
                      max_epoch=texture.max_epoch, check=texture.check_result)

            net.set_data(data)

            net.add_layer(texture.layer[0].neuron, activation_function=texture.layer[0].activation,
                          layer_type=Net.INPUT_LAYER)

            for i in range(texture.layer_dim - 2):
                net.add_layer(texture.layer[i + 1].neuron, activation_function=texture.layer[i + 1].activation,
                              layer_type=Net.HIDDEN_LAYER)

            net.add_layer(texture.layer[texture.layer_dim - 1].neuron,
                          activation_function=texture.layer[texture.layer_dim - 1].activation,
                          layer_type=Net.OUTPUT_LAYER)

            optimizer = Net.optimizers.Adam

            net.compile(optimizer=optimizer)

            if texture.sound:
                winsound.Beep(1000, 500)

            net.exe(batch_split=texture.batch_split)

            if net.epoch < texture.max_epoch:

                net.prediction()

                wr.write_final_result(net)

                if net.final_test_accuracy >= texture.min_test_accuracy:
                    if texture.sound:
                        winsound.Beep(1000, 1500)
                    break
                else:

                    if texture.sound:
                        winsound.Beep(1000, 500)

                    if not texture.check_result:
                        print('# Test Accuracy is not acceptable.')
                        d = input('Dou you want to try again?   \'y\' or \'n\'\n')
                        if not d == 'y':
                            break
                    else:
                        print('# Test Accuracy is not acceptable. We Must Try Again ...')
            else:

                if texture.sound:
                    winsound.Beep(2000, 500)

                if not texture.check_result:
                    net.prediction()
                    wr.write_final_result(net)
                    print('>>> # result is not acceptable.')
                    d = input('Dou you want to try again?   \'y\' or \'n\'\n')
                    if not d == 'y':
                        break
                else:
                    print('>>> # result is not acceptable. We Must Try Again ...')
