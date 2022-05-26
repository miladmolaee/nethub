from src.engine.network.activations import Activations as activations
from src.engine.network.optimizers import Optimizers as optimizers

class Layer:

    def __init__(self, n, act_func):
        self.neuron = n
        self.activation = act_func


class Texture:

    run_number = 1
    max_epoch = 2500
    min_training_accuracy = 0.9
    min_validation_accuracy = 0.9
    min_test_accuracy = 0.9
    max_training_loss = 5e-5
    max_validation_loss = 5e-5
    max_test_loss = 5e-5
    input_dimension = 2
    output_dimension = 1
    test_split = 0.15
    validation_split = 0.15
    batch_split = 0.2
    normalization_range = [-1, 1]
    multi_run = False
    plot = False
    check_result = False
    sound = False
    layer = []
    layer_dim = 0

    def __init__(self, run_number=1, max_epoch=2500, min_training_accuracy=0.9, min_validation_accuracy=0.9,
                 min_test_accuracy=0.9, max_training_loss=5e-5, max_validation_loss=5e-5, max_test_loss=5e-5,
                 input_dimension=2, output_dimension=1, test_split=0.15, validation_split=0.15, batch_split=0.2,
                 normalization_range=[], multi_run=False, plot=True, check_result=False, sound=True,
                 layer=[], layer_dim=0):

        if normalization_range is None:
            normalization_range = [-1, 1]
        self.run_number = run_number
        self.max_epoch = max_epoch
        self.min_training_accuracy = min_training_accuracy
        self.min_validation_accuracy = min_validation_accuracy
        self.min_test_accuracy = min_test_accuracy
        self.max_training_loss = max_training_loss
        self.max_validation_loss = max_validation_loss
        self.max_test_loss = max_test_loss
        self.input_dimension = input_dimension
        self.output_dimension = output_dimension
        self.test_split = test_split
        self.validation_split = validation_split
        self.batch_split = batch_split
        self.normalization_range = normalization_range
        self.multi_run = multi_run
        self.plot = plot
        self.check_result = check_result
        self.sound = sound
        self.layer = layer
        self.layer_dim = layer_dim

    def make(self, scripts):

        for i in range(len(scripts)):

            if scripts[i].__contains__('runnumber'):
                self.run_number = int(separate(scripts[i]))

            elif scripts[i].__contains__('maxepoch'):
                self.max_epoch = int(separate(scripts[i]))

            elif scripts[i].__contains__('multirun'):
                if separate(scripts[i]) == 'on':
                    self.multi_run = True
                elif separate(scripts[i]) == 'off':
                    self.multi_run = False

            elif scripts[i].__contains__('plot'):
                if separate(scripts[i]) == 'on':
                    self.plot = True
                elif separate(scripts[i]) == 'off':
                    self.plot = False

            elif scripts[i].__contains__('checkresult'):
                if separate(scripts[i]) == 'on':
                    self.check_result = True
                elif separate(scripts[i]) == 'off':
                    self.check_result = False

            elif scripts[i].__contains__('sound'):
                if separate(scripts[i]) == 'on':
                    self.sound = True
                elif separate(scripts[i]) == 'off':
                    self.sound = False

            elif scripts[i].__contains__('mintrainingaccuracy'):
                self.min_training_accuracy = float(separate(scripts[i]))

            elif scripts[i].__contains__('minvalidationaccuracy'):
                self.min_validation_accuracy = float(separate(scripts[i]))

            elif scripts[i].__contains__('mintestaccuracy'):
                self.min_test_accuracy = float(separate(scripts[i]))

            elif scripts[i].__contains__('maxtrainingloss'):
                self.max_training_loss = float(separate(scripts[i]))

            elif scripts[i].__contains__('maxvalidationloss'):
                self.max_validation_loss = float(separate(scripts[i]))

            elif scripts[i].__contains__('maxtestloss'):
                self.max_test_loss = float(separate(scripts[i]))

            elif scripts[i].__contains__('inputdimension'):
                self.input_dimension = int(separate(scripts[i]))

            elif scripts[i].__contains__('outputdimension'):
                self.output_dimension = int(separate(scripts[i]))

            elif scripts[i].__contains__('testsplit'):
                self.test_split = float(separate(scripts[i]))

            elif scripts[i].__contains__('validationsplit'):
                self.validation_split = float(separate(scripts[i]))

            elif scripts[i].__contains__('batchsplit'):
                self.batch_split = float(separate(scripts[i]))

            elif scripts[i].__contains__('normalization'):
                self.normalization_range = []
                temp = ''
                for s in separate(scripts[i]):
                    if not (s == '[' or s == ']' or s == ','):
                        temp = temp + s
                    if s == ',':
                        self.normalization_range.append(float(temp))
                        temp = ''
                    if s == ']':
                        self.normalization_range.append(float(temp))
                        temp = ''

            elif scripts[i].__contains__('layer'):

                my_str = separate(scripts[i]) + ','

                n = 1
                act_func = activations.relu

                st = ''
                ast = ''

                for s in my_str:

                    if s == '=' and st == 'n':
                        ast = st
                        st = ''

                    if s == '=' and st == 'activation':
                        ast = st
                        st = ''

                    elif s == ',' and ast == 'n':
                        n = int(st)
                        ast = ''
                        st = ''

                    elif s == ',' and ast == 'activation':

                        if st == activations.relu.name:
                            act_func = activations.relu
                            ast = ''
                            st = ''

                        elif st == activations.elu.name:
                            act_func = activations.elu
                            ast = ''
                            st = ''

                        elif st == activations.selu.name:
                            act_func = activations.selu
                            ast = ''
                            st = ''

                        elif st == activations.linear.name:
                            act_func = activations.linear
                            ast = ''
                            st = ''

                        elif st == activations.tanh.name:
                            act_func = activations.tanh
                            ast = ''
                            st = ''

                        elif st == activations.sigmoid.name:
                            act_func = activations.sigmoid
                            ast = ''
                            st = ''

                        elif st == activations.hard_sigmoid.name:
                            act_func = activations.hard_sigmoid
                            ast = ''
                            st = ''

                        elif st == activations.softmax.name:
                            act_func = activations.softmax
                            ast = ''
                            st = ''

                        elif st == activations.softsign.name:
                            act_func = activations.softsign
                            ast = ''
                            st = ''

                        elif st == activations.softplus.name:
                            act_func = activations.softplus
                            ast = ''
                            st = ''

                        elif st == activations.exponential.name:
                            act_func = activations.exponential
                            ast = ''
                            st = ''

                        layer = Layer(n, act_func)
                        self.layer_dim = self.layer_dim + 1
                        self.layer.append(layer)

                    if not (s == '=' or s == ','):
                        st = st + s


def separate(string):
    my_str = ''
    bl = 0

    for s in string:

        if not bl:
            if s == ':':
                bl = 1
        else:
            my_str = my_str + s

    return my_str
