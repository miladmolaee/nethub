from src.engine.network import activations
from tensorflow import keras
from tensorflow.keras.layers import Dense


class NetModel:

    def __init__(self, path, input_dim):

        file = open(path + '.project/architecture.text', 'r')
        Lines = file.readlines()
        file.close()

        newLines = []

        for line in Lines:
            string = ''
            for i in line:
                if not (i == ' ' or i == '\t'):
                    string = string + i
            newLines.append(string)

        n = []
        act = []

        for line in newLines:

            temp = ''
            cmd = ''

            for s in line:
                if s == '-':
                    temp = ''
                    cmd = ''
                elif s == ':':
                    cmd = temp
                    temp = ''
                elif s == ']':
                    if cmd == 'neurons':
                        n.append(int(temp))
                    elif cmd == 'activationfunction':

                        act_func = activations.relu

                        if temp == activations.relu.name:
                            act_func = activations.relu
                        elif temp == activations.elu.name:
                            act_func = activations.elu
                        elif temp == activations.selu.name:
                            act_func = activations.selu
                        if temp == activations.linear.name:
                            act_func = activations.linear
                        if temp == activations.tanh.name:
                            act_func = activations.tanh
                        if temp == activations.sigmoid.name:
                            act_func = activations.sigmoid
                        elif temp == activations.hard_sigmoid.name:
                            act_func = activations.hard_sigmoid
                        elif temp == activations.softmax.name:
                            act_func = activations.softmax
                        elif temp == activations.softsign.name:
                            act_func = activations.softsign
                        elif temp == activations.softplus.name:
                            act_func = activations.softplus
                        elif temp == activations.exponential.name:
                            act_func = activations.exponential

                        act.append(act_func)

                elif not s == '[':
                    temp = temp + s

        self.model = keras.models.Sequential()

        self.model.add(Dense(n[0], activation=act[0], input_dim=int(input_dim)))

        for i in range(len(n) - 2):
            self.model.add(Dense(n[i + 1], activation=act[i + 1]))

        self.model.add(Dense(n[len(n) - 1], activation=act[len(act) - 1]))

        self.model.load_weights(path + 'my_model_weights.h5')

    def run(self, inputs):
        self.predictions = self.model.predict(inputs)
        return self.predictions

    def get_model(self):
        return self.model
