import os

import numpy


class Normalizer:
    def __init__(self, input_dim, output_dim, d_min, d_max, root_path):

        self.root_path = root_path

        self.s = []
        self.o = []

        self.d_min = d_min
        self.d_max = d_max

        self.input_dim = input_dim
        self.output_dim = output_dim

    def normalize(self, data_list):

        # convert data List to Array ---- and transpose it -------------------------------------------------------------
        raw_data = numpy.array(data_list)
        raw_data_t = numpy.transpose(raw_data)

        # create a zero matrix for normalized data ---------------------------------------------------------------------
        normalized_data_t = numpy.zeros((len(raw_data_t[:, 0]), len(raw_data_t[0, :])))

        # normalize data -----------------------------------------------------------------------------------------------
        for i in range(len(raw_data_t[:, 0])):

            _min = min(raw_data_t[i, :])
            _max = max(raw_data_t[i, :])

            self.s.append((self.d_max - self.d_min) / (_max - _min))
            self.o.append((_max * self.d_min - _min * self.d_max) / (_max - _min))

            for j in range(len(raw_data_t[i, :])):
                normalized_data_t[i, j] = self.s[i] * raw_data_t[i, j] + self.o[i]

        # transpose normalized_data_t array ----------------------------------------------------------------------------
        self.normalized_data = numpy.transpose(normalized_data_t)

        # Create directorys
        try:
            os.mkdir(os.path.join(self.root_path, '.properties'))
        except OSError as error:
            pass
            # print(error)

        try:
            os.mkdir(os.path.join(self.root_path, '.temp'))
        except OSError as error:
            pass
            # print(error)

        # write s and o ------------------------------------------------------------------------------------------------
        file = open(self.root_path + '.properties/input.properties', 'w')
        file.write('input dimension : [' + str(self.input_dim) + ']\n')
        file.write('output dimension : [' + str(self.output_dim) + ']\n')
        file.write('s : ')
        file.write(str(self.s))
        file.write('\n')
        file.write('o : ')
        file.write(str(self.o))
        file.write('\n')
        file.close()

        numpy.savetxt(self.root_path + '.temp/normalized_data.text', self.normalized_data, delimiter='\t', fmt='%1.9f')

        # return normalized data as a list -----------------------------------------------------------------------------
        return self.normalized_data.tolist()

    def de_normalize(self, data_list):

        # convert normalized data List to Array ---- and transpose it --------------------------------------------------
        normalized_data = numpy.array(data_list)
        normalized_data_t = numpy.transpose(normalized_data)

        # create a zero matrix for raw data ----------------------------------------------------------------------------
        raw_data_t = numpy.zeros((len(normalized_data_t[:, 0]), len(normalized_data_t[0, :])))

        # denormalize data ---------------------------------------------------------------------------------------------
        for i in range(len(normalized_data_t[:, 0])):
            for j in range(len(normalized_data_t[i, :])):
                raw_data_t[i, j] = (normalized_data_t[i, j] - self.o[i])/self.s[i]

        # transpose raw_data_t array -----------------------------------------------------------------------------------
        raw_data = raw_data_t.transpose()

        # return raw data as a list ------------------------------------------------------------------------------------
        return raw_data.tolist()
