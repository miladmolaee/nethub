import numpy
import os


class PNormalizer:
    def __init__(self, root_path, input_dim, output_dim, d_min, d_max, s, o):

        self.root_path = root_path

        self.s = s
        self.o = o

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

            for j in range(len(raw_data_t[i, :])):
                normalized_data_t[i, j] = self.s[i] * raw_data_t[i, j] + self.o[i]

        # transpose normalized_data_t array ----------------------------------------------------------------------------
        normalized_data = numpy.transpose(normalized_data_t)

        # Create directories
        try:
            os.mkdir(os.path.join(self.root_path, '.properties'))
        except OSError as error:
            print(error)
        try:
            os.mkdir(os.path.join(self.root_path, '.temp'))
        except OSError as error:
            print(error)

        # write s and o ------------------------------------------------------------------------------------------------
        file = open(self.root_path + '\\.properties\\input_for_prediction.properties', 'w')
        file.write('input dimension : [' + str(self.input_dim) + ']\n')
        file.write('output dimension : [' + str(self.output_dim) + ']\n')
        file.write('s : ')
        file.write(str(self.s))
        file.write('\n')
        file.write('o : ')
        file.write(str(self.o))
        file.write('\n')
        file.close()

        numpy.savetxt(self.root_path + '\\.temp\\normalized_data_for_prediction.dat', normalized_data,
                      delimiter='\t', fmt='%1.9f')

        # return normalized data as a list -----------------------------------------------------------------------------
        return normalized_data.tolist()

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
