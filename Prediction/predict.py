from Prediction.model import NetModel
from Prediction.Util.data_for_prediction import PData
import numpy


def prediction(path):

    lower_bond = -1
    upper_bond = 1

    input_dim = 1
    output_dim = 1

    _o = []
    _s = []

    file = open(path + '\\.properties\\input.properties', 'r')
    Lines = file.readlines()
    newLines = []

    for line in Lines:

        string = ''

        for i in line:
            if not (i == ' ' or i == '\t'):
                string = string + i
        newLines.append(string)

    for s in newLines:

        if not s.__contains__(','):
            mstr = ''
            b = True
            cmd = ''

            for char in s:
                if char == ':':
                    b = False
                    cmd = mstr
                    mstr = ''
                elif b:
                    mstr = mstr + char
                elif not (char == '[' or char == ']'):
                    mstr = mstr + char
                elif char == ']':
                    if cmd == 'lowerbond':
                        lower_bond = float(mstr)
                    elif cmd == 'upperbond':
                        upper_bond = float(mstr)
                    elif cmd == 'inputdimension':
                        input_dim = float(mstr)
                    elif cmd == 'outputdimension':
                        output_dim = float(mstr)
        else:
            b = True
            mstr = ''
            cmd = ''
            list = []

            for char in s:
                if char == ':':
                    b = False
                    cmd = mstr
                    mstr = ''
                elif b:
                    mstr = mstr + char
                elif char == ',':
                    list.append(float(mstr))
                    mstr = ''
                elif not (char == '[' or char == ']'):
                    mstr = mstr + char
                elif char == ']':
                    list.append(float(mstr))
                    mstr = ''
                    if cmd == 'o':
                        _o = list
                    elif cmd == 's':
                        _s = list

    data = PData(path, 'input.xlsx', input_dim, output_dim, upper_bond, lower_bond, _s, _o)

    net = NetModel(path, input_dim)
    predicted = net.run(data.input)

    for i in range(len(predicted[:, 0])):
        for j in range(len(predicted[0, :])):
            predicted[i, j] = (predicted[i, j] - _o[int(input_dim) + j]) / _s[int(input_dim) + j]

    numpy.savetxt(path + '\\prediction_output.txt', predicted, delimiter='\t', fmt='%1.9f')




