from Engine.network import Net


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
    multi_run = False
    plot = False
    check_result = False
    sound = False
    layer = []
    layer_dim = 0

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

            elif scripts[i].__contains__('inputdimention'):
                self.input_dimention = int(separate(scripts[i]))

            elif scripts[i].__contains__('outputdimention'):
                self.output_dimention = int(separate(scripts[i]))

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
                    if not(s == '[' or s == ']' or s == ','):
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
                act_func = Net.activations.relu

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

                        if st == Net.activations.relu.name:
                            act_func = Net.activations.relu
                            ast = ''
                            st = ''

                        if st == Net.activations.elu.name:
                            act_func = Net.activations.elu
                            ast = ''
                            st = ''

                        if st == Net.activations.selu.name:
                            act_func = Net.activations.selu
                            ast = ''
                            st = ''

                        if st == Net.activations.linear.name:
                            act_func = Net.activations.linear
                            ast = ''
                            st = ''

                        if st == Net.activations.tanh.name:
                            act_func = Net.activations.tanh
                            ast = ''
                            st = ''

                        if st == Net.activations.sigmoid.name:
                            act_func = Net.activations.sigmoid
                            ast = ''
                            st = ''

                        if st == Net.activations.hard_sigmoid.name:
                            act_func = Net.activations.hard_sigmoid
                            ast = ''
                            st = ''

                        if st == Net.activations.softmax.name:
                            act_func = Net.activations.softmax
                            ast = ''
                            st = ''

                        if st == Net.activations.softsign.name:
                            act_func = Net.activations.softsign
                            ast = ''
                            st = ''

                        if st == Net.activations.softplus.name:
                            act_func = Net.activations.softplus
                            ast = ''
                            st = ''

                        if st == Net.activations.exponential.name:
                            act_func = Net.activations.exponential
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
