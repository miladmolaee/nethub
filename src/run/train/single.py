
from src.engine.mlp import MLP
from src.engine.network import optimizers
from src.engine.network import Network
from src.input.data import Data
import src.input.texture as texture
import src.run.utils.write_training_result as wr
from src.run.utils.play_sound import Sound

class Single:
    commands: str
    root_path: str

    def set(self, root_path, script):
        self.commands = script
        self.root_path = root_path

    def run(self):

        tex = texture.Texture()
        tex.make(self.commands)

        while True:

            data = Data(root_path=self.root_path, file_name='input.xlsx', test_split=tex.test_split,
                        validation_split=tex.validation_split,
                        input_dim=tex.input_dimension, output_dim=tex.output_dimension,
                        lower_norm=tex.normalization_range[0], upper_norm=tex.normalization_range[1])

            net = MLP(parent_directory=self.root_path, run_num=tex.run_number, multi_run=False, plot=tex.plot,
                      min_accuracy=tex.min_training_accuracy, min_accuracy_v=tex.min_validation_accuracy,
                      max_loss=tex.max_training_loss, max_loss_v=tex.max_validation_loss,
                      max_epoch=tex.max_epoch, check=tex.check_result)

            net.set_data(data)

            net.add_layer(tex.layer[0].neuron, activation_function=tex.layer[0].activation,
                          layer_type=Network.INPUT_LAYER)

            for i in range(tex.layer_dim - 2):
                net.add_layer(tex.layer[i + 1].neuron, activation_function=tex.layer[i + 1].activation,
                              layer_type=Network.HIDDEN_LAYER)

            net.add_layer(tex.layer[tex.layer_dim - 1].neuron,
                          activation_function=tex.layer[tex.layer_dim - 1].activation,
                          layer_type=Network.OUTPUT_LAYER)

            optimizer = optimizers.Optimizers.Adam

            net.compile(optimizer=optimizer)

            if tex.sound:
                sound = Sound()
                sound.say_start()
                

            net.exe(batch_split=tex.batch_split)

            if net.epoch < tex.max_epoch:

                net.prediction()

                wr.write_final_result(net)

                if net.final_test_accuracy >= tex.min_test_accuracy:
                    if tex.sound:
                        sound = Sound()
                        sound.say_finished_ok() 
                    break
                else:

                    if tex.sound:
                        sound.say_finished_not_acceptable()

                    if not tex.check_result:
                        print('# Test Accuracy is not acceptable.')
                        d = input("Dou you want to try again?   'y' or 'n'\n")
                        if not d == 'y':
                            break
                    else:
                        print('# Test Accuracy is not acceptable. We Must Try Again ...')
            else:

                if tex.sound:
                    sound.say_finished_not_acceptable()

                if not tex.check_result:
                    net.prediction()
                    wr.write_final_result(net)
                    print('>>> # result is not acceptable.')
                    d = input('Dou you want to try again?   \'y\' or \'n\'\n')
                    if not d == 'y':
                        break
                else:
                    print('>>> # result is not acceptable. We Must Try Again ...')
