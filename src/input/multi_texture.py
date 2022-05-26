from src.engine.network import Network


class MultiTexture:

    m_activations = []
    m_neurons = []

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

    def make(self, scripts):

        self.set_constants(scripts)
        # self.size = get_number_of_networks(scripts)

        for i in range(len(scripts)):

            if scripts[i].__contains__('layer'):

                activations_name = []
                activations = []
                neurons = []
                string = ''
                temp = ''

                for s in scripts[i]:

                    if string == 'layer:n=':

                        if s == ',':

                            if temp.__contains__(':'):

                                _temp = temp.split(':')

                                start = int(_temp[0])
                                step = int(_temp[1])
                                end = int(_temp[2])

                                while start <= end:
                                    neurons.append(int(start))
                                    start = start + step

                            else:
                                neurons.append(int(temp))

                            self.m_neurons.append(neurons)
                            string = 'layer:'
                            temp = ''
                        else:
                            temp = temp + s

                    elif string == 'layer:activation={':

                        if s == ',':
                            activations_name.append(temp)
                            temp = ''
                        elif s == '}':
                            activations_name.append(temp)
                            temp = ''

                            for name in activations_name:

                                if name == Net.activations.relu.name:
                                    activations.append(Net.activations.relu)

                                elif name == Net.activations.elu.name:
                                    activations.append(Net.activations.elu)

                                elif name == Net.activations.selu.name:
                                    activations.append(Net.activations.selu)

                                elif name == Net.activations.linear.name:
                                    activations.append(Net.activations.linear)

                                elif name == Net.activations.tanh.name:
                                    activations.append(Net.activations.tanh)

                                elif name == Net.activations.sigmoid.name:
                                    activations.append(Net.activations.sigmoid)

                                elif name == Net.activations.hard_sigmoid.name:
                                    activations.append(Net.activations.hard_sigmoid)

                                elif name == Net.activations.softmax.name:
                                    activations.append(Net.activations.softmax)

                                elif name == Net.activations.softsign.name:
                                    activations.append(Net.activations.softsign)

                                elif name == Net.activations.softplus.name:
                                    activations.append(Net.activations.softplus)

                                elif name == Net.activations.exponential.name:
                                    activations.append(Net.activations.exponential)

                            self.m_activations.append(activations)
                        else:
                            temp = temp + s

                    else:
                        string = string + s

    def set_constants(self, scripts):

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


def get_number_of_networks(command):
    total = 1

    for i in range(len(command)):

        if command[i].__contains__('layer'):

            num_of_acts = 0
            num_of_neurons = 0
            string = ''
            temp = ''

            for s in command[i]:

                if string == 'layer:n=':

                    if s == ',':

                        if temp.__contains__(':'):

                            _temp = temp.split(':')

                            start = int(_temp[0])
                            step = int(_temp[1])
                            end = int(_temp[2])

                            num_of_neurons = 0

                            while start <= end and end > 0:
                                num_of_neurons = num_of_neurons + 1
                                start = start + step

                        else:
                            num_of_neurons = 1

                        string = 'layer:'
                    else:
                        temp = temp + s

                elif string == 'layer:activation={':

                    if s == ',':
                        num_of_acts = num_of_acts + 1
                    elif s == '}':
                        num_of_acts = num_of_acts + 1

                else:
                    string = string + s

            total = total * num_of_neurons * num_of_acts

    return total
