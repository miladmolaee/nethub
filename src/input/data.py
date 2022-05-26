import math

import numpy
import pandas

from src.input.utils.generate_random_list import generateList
from src.input.utils.normalizer import Normalizer


class Data:

    def __init__(self, input_dim, output_dim, root_path, file_name, validation_split=0.15, test_split=0.15,
                 upper_norm=-1, lower_norm=1):

        self.root_path = root_path

        self.input_dim = input_dim
        self.output_dim = output_dim

        # read excel file ----------------------------------------------------------------------------------------------
        raw_data = pandas.read_excel(root_path + file_name)

        # set columns --------------------------------------------------------------------------------------------------
        column_title = []

        for i in range(input_dim):
            column_title.append('in' + str(i + 1))

        for i in range(output_dim):
            column_title.append('out' + str(i + 1))

        # get columns as a list ----------------------------------------------------------------------------------------
        column_1 = list(raw_data[column_title[0]])
        column_2 = list(raw_data[column_title[1]])

        if input_dim + output_dim > 2:
            column_3 = list(raw_data[column_title[2]])
            if input_dim + output_dim > 3:
                column_4 = list(raw_data[column_title[3]])
            if input_dim + output_dim > 4:
                column_5 = list(raw_data[column_title[4]])
            if input_dim + output_dim > 5:
                column_6 = list(raw_data[column_title[5]])
            if input_dim + output_dim > 6:
                column_7 = list(raw_data[column_title[6]])
            if input_dim + output_dim > 7:
                column_8 = list(raw_data[column_title[7]])
            if input_dim + output_dim > 8:
                column_9 = list(raw_data[column_title[8]])
            if input_dim + output_dim > 9:
                column_10 = list(raw_data[column_title[9]])

        if input_dim + output_dim > 10:
            column_11 = list(raw_data[column_title[10]])
            if input_dim + output_dim > 11:
                column_12 = list(raw_data[column_title[11]])
            if input_dim + output_dim > 12:
                column_13 = list(raw_data[column_title[12]])
            if input_dim + output_dim > 13:
                column_14 = list(raw_data[column_title[13]])
            if input_dim + output_dim > 14:
                column_15 = list(raw_data[column_title[14]])
            if input_dim + output_dim > 15:
                column_16 = list(raw_data[column_title[15]])
            if input_dim + output_dim > 16:
                column_17 = list(raw_data[column_title[16]])
            if input_dim + output_dim > 17:
                column_18 = list(raw_data[column_title[17]])
            if input_dim + output_dim > 18:
                column_19 = list(raw_data[column_title[18]])
            if input_dim + output_dim > 19:
                column_20 = list(raw_data[column_title[19]])

        if input_dim + output_dim > 20:
            column_21 = list(raw_data[column_title[20]])
            if input_dim + output_dim > 21:
                column_22 = list(raw_data[column_title[21]])
            if input_dim + output_dim > 22:
                column_23 = list(raw_data[column_title[22]])
            if input_dim + output_dim > 23:
                column_24 = list(raw_data[column_title[23]])
            if input_dim + output_dim > 24:
                column_25 = list(raw_data[column_title[24]])
            if input_dim + output_dim > 25:
                column_26 = list(raw_data[column_title[25]])
            if input_dim + output_dim > 26:
                column_27 = list(raw_data[column_title[26]])
            if input_dim + output_dim > 27:
                column_28 = list(raw_data[column_title[27]])
            if input_dim + output_dim > 28:
                column_29 = list(raw_data[column_title[28]])
            if input_dim + output_dim > 29:
                column_30 = list(raw_data[column_title[29]])

        if input_dim + output_dim > 30:
            column_31 = list(raw_data[column_title[30]])
            if input_dim + output_dim > 31:
                column_32 = list(raw_data[column_title[31]])
            if input_dim + output_dim > 32:
                column_33 = list(raw_data[column_title[32]])
            if input_dim + output_dim > 33:
                column_34 = list(raw_data[column_title[33]])
            if input_dim + output_dim > 34:
                column_35 = list(raw_data[column_title[34]])
            if input_dim + output_dim > 35:
                column_36 = list(raw_data[column_title[35]])
            if input_dim + output_dim > 36:
                column_37 = list(raw_data[column_title[36]])
            if input_dim + output_dim > 37:
                column_38 = list(raw_data[column_title[37]])
            if input_dim + output_dim > 38:
                column_39 = list(raw_data[column_title[38]])
            if input_dim + output_dim > 39:
                column_40 = list(raw_data[column_title[39]])

        if input_dim + output_dim > 40:
            column_41 = list(raw_data[column_title[40]])
            if input_dim + output_dim > 41:
                column_42 = list(raw_data[column_title[41]])
            if input_dim + output_dim > 42:
                column_43 = list(raw_data[column_title[42]])
            if input_dim + output_dim > 43:
                column_44 = list(raw_data[column_title[43]])
            if input_dim + output_dim > 44:
                column_45 = list(raw_data[column_title[44]])
            if input_dim + output_dim > 45:
                column_46 = list(raw_data[column_title[45]])
            if input_dim + output_dim > 46:
                column_47 = list(raw_data[column_title[46]])
            if input_dim + output_dim > 47:
                column_48 = list(raw_data[column_title[47]])
            if input_dim + output_dim > 48:
                column_49 = list(raw_data[column_title[48]])
            if input_dim + output_dim > 49:
                column_50 = list(raw_data[column_title[49]])

        # set size
        self.size = len(column_1)

        # change scales ------------------------------------------------------------------------------------------------
        _column_1 = numpy.zeros(self.size)
        _column_2 = numpy.zeros(self.size)

        if input_dim + output_dim > 2:
            _column_3 = numpy.zeros(self.size)
            if input_dim + output_dim > 3:
                _column_4 = numpy.zeros(self.size)
            if input_dim + output_dim > 4:
                _column_5 = numpy.zeros(self.size)
            if input_dim + output_dim > 5:
                _column_6 = numpy.zeros(self.size)
            if input_dim + output_dim > 6:
                _column_7 = numpy.zeros(self.size)
            if input_dim + output_dim > 7:
                _column_8 = numpy.zeros(self.size)
            if input_dim + output_dim > 8:
                _column_9 = numpy.zeros(self.size)
            if input_dim + output_dim > 9:
                _column_10 = numpy.zeros(self.size)

        if input_dim + output_dim > 10:
            _column_11 = numpy.zeros(self.size)
            if input_dim + output_dim > 11:
                _column_12 = numpy.zeros(self.size)
            if input_dim + output_dim > 12:
                _column_13 = numpy.zeros(self.size)
            if input_dim + output_dim > 13:
                _column_14 = numpy.zeros(self.size)
            if input_dim + output_dim > 14:
                _column_15 = numpy.zeros(self.size)
            if input_dim + output_dim > 15:
                _column_16 = numpy.zeros(self.size)
            if input_dim + output_dim > 16:
                _column_17 = numpy.zeros(self.size)
            if input_dim + output_dim > 17:
                _column_18 = numpy.zeros(self.size)
            if input_dim + output_dim > 18:
                _column_19 = numpy.zeros(self.size)
            if input_dim + output_dim > 19:
                _column_20 = numpy.zeros(self.size)

        if input_dim + output_dim > 20:
            _column_21 = numpy.zeros(self.size)
            if input_dim + output_dim > 21:
                _column_22 = numpy.zeros(self.size)
            if input_dim + output_dim > 22:
                _column_23 = numpy.zeros(self.size)
            if input_dim + output_dim > 23:
                _column_24 = numpy.zeros(self.size)
            if input_dim + output_dim > 24:
                _column_25 = numpy.zeros(self.size)
            if input_dim + output_dim > 25:
                _column_26 = numpy.zeros(self.size)
            if input_dim + output_dim > 26:
                _column_27 = numpy.zeros(self.size)
            if input_dim + output_dim > 27:
                _column_28 = numpy.zeros(self.size)
            if input_dim + output_dim > 28:
                _column_29 = numpy.zeros(self.size)
            if input_dim + output_dim > 29:
                _column_30 = numpy.zeros(self.size)

        if input_dim + output_dim > 30:
            _column_31 = numpy.zeros(self.size)
            if input_dim + output_dim > 31:
                _column_32 = numpy.zeros(self.size)
            if input_dim + output_dim > 32:
                _column_33 = numpy.zeros(self.size)
            if input_dim + output_dim > 33:
                _column_34 = numpy.zeros(self.size)
            if input_dim + output_dim > 34:
                _column_35 = numpy.zeros(self.size)
            if input_dim + output_dim > 35:
                _column_36 = numpy.zeros(self.size)
            if input_dim + output_dim > 36:
                _column_37 = numpy.zeros(self.size)
            if input_dim + output_dim > 37:
                _column_38 = numpy.zeros(self.size)
            if input_dim + output_dim > 38:
                _column_39 = numpy.zeros(self.size)
            if input_dim + output_dim > 39:
                _column_40 = numpy.zeros(self.size)

        if input_dim + output_dim > 40:
            _column_41 = numpy.zeros(self.size)
            if input_dim + output_dim > 41:
                _column_42 = numpy.zeros(self.size)
            if input_dim + output_dim > 42:
                _column_43 = numpy.zeros(self.size)
            if input_dim + output_dim > 43:
                _column_44 = numpy.zeros(self.size)
            if input_dim + output_dim > 44:
                _column_45 = numpy.zeros(self.size)
            if input_dim + output_dim > 45:
                _column_46 = numpy.zeros(self.size)
            if input_dim + output_dim > 46:
                _column_47 = numpy.zeros(self.size)
            if input_dim + output_dim > 47:
                _column_48 = numpy.zeros(self.size)
            if input_dim + output_dim > 48:
                _column_49 = numpy.zeros(self.size)
            if input_dim + output_dim > 49:
                _column_50 = numpy.zeros(self.size)

        # make data list -----------------------------------------------------------------------------------------------
        self.data_list = []

        for i in range(self.size):
            temp_list = []

            _column_1[i] = column_1[i]
            _column_2[i] = column_2[i]

            temp_list.append(_column_1[i])
            temp_list.append(_column_2[i])

            if input_dim + output_dim > 2:
                _column_3[i] = column_3[i]
                temp_list.append(_column_3[i])
                if input_dim + output_dim > 3:
                    _column_4[i] = column_4[i]
                    temp_list.append(_column_4[i])
                if input_dim + output_dim > 4:
                    _column_5[i] = column_5[i]
                    temp_list.append(_column_5[i])
                if input_dim + output_dim > 5:
                    _column_6[i] = column_6[i]
                    temp_list.append(_column_6[i])
                if input_dim + output_dim > 6:
                    _column_7[i] = column_7[i]
                    temp_list.append(_column_7[i])
                if input_dim + output_dim > 7:
                    _column_8[i] = column_8[i]
                    temp_list.append(_column_8[i])
                if input_dim + output_dim > 8:
                    _column_9[i] = column_9[i]
                    temp_list.append(_column_9[i])
                if input_dim + output_dim > 9:
                    _column_10[i] = column_10[i]
                    temp_list.append(_column_10[i])

            if input_dim + output_dim > 10:
                _column_11[i] = column_11[i]
                temp_list.append(_column_11[i])
                if input_dim + output_dim > 11:
                    _column_12[i] = column_12[i]
                    temp_list.append(_column_12[i])
                if input_dim + output_dim > 12:
                    _column_13[i] = column_13[i]
                    temp_list.append(_column_13[i])
                if input_dim + output_dim > 13:
                    _column_14[i] = column_14[i]
                    temp_list.append(_column_14[i])
                if input_dim + output_dim > 14:
                    _column_15[i] = column_15[i]
                    temp_list.append(_column_15[i])
                if input_dim + output_dim > 15:
                    _column_16[i] = column_16[i]
                    temp_list.append(_column_16[i])
                if input_dim + output_dim > 16:
                    _column_17[i] = column_17[i]
                    temp_list.append(_column_17[i])
                if input_dim + output_dim > 17:
                    _column_18[i] = column_18[i]
                    temp_list.append(_column_18[i])
                if input_dim + output_dim > 18:
                    _column_19[i] = column_19[i]
                    temp_list.append(_column_19[i])
                if input_dim + output_dim > 19:
                    _column_20[i] = column_20[i]
                    temp_list.append(_column_20[i])

            if input_dim + output_dim > 20:
                _column_21[i] = column_21[i]
                temp_list.append(_column_21[i])
                if input_dim + output_dim > 21:
                    _column_22[i] = column_22[i]
                    temp_list.append(_column_22[i])
                if input_dim + output_dim > 22:
                    _column_23[i] = column_23[i]
                    temp_list.append(_column_23[i])
                if input_dim + output_dim > 23:
                    _column_24[i] = column_24[i]
                    temp_list.append(_column_24[i])
                if input_dim + output_dim > 24:
                    _column_25[i] = column_25[i]
                    temp_list.append(_column_25[i])
                if input_dim + output_dim > 25:
                    _column_26[i] = column_26[i]
                    temp_list.append(_column_26[i])
                if input_dim + output_dim > 26:
                    _column_27[i] = column_27[i]
                    temp_list.append(_column_27[i])
                if input_dim + output_dim > 27:
                    _column_28[i] = column_28[i]
                    temp_list.append(_column_28[i])
                if input_dim + output_dim > 28:
                    _column_29[i] = column_29[i]
                    temp_list.append(_column_29[i])
                if input_dim + output_dim > 29:
                    _column_30[i] = column_30[i]
                    temp_list.append(_column_30[i])

            if input_dim + output_dim > 30:
                _column_31[i] = column_31[i]
                temp_list.append(_column_31[i])
                if input_dim + output_dim > 31:
                    _column_32[i] = column_32[i]
                    temp_list.append(_column_32[i])
                if input_dim + output_dim > 32:
                    _column_33[i] = column_33[i]
                    temp_list.append(_column_33[i])
                if input_dim + output_dim > 33:
                    _column_34[i] = column_34[i]
                    temp_list.append(_column_34[i])
                if input_dim + output_dim > 34:
                    _column_35[i] = column_35[i]
                    temp_list.append(_column_35[i])
                if input_dim + output_dim > 35:
                    _column_36[i] = column_36[i]
                    temp_list.append(_column_36[i])
                if input_dim + output_dim > 36:
                    _column_37[i] = column_37[i]
                    temp_list.append(_column_36[i])
                if input_dim + output_dim > 37:
                    _column_38[i] = column_38[i]
                    temp_list.append(_column_38[i])
                if input_dim + output_dim > 38:
                    _column_39[i] = column_39[i]
                    temp_list.append(_column_39[i])
                if input_dim + output_dim > 39:
                    _column_40[i] = column_40[i]
                    temp_list.append(_column_40[i])

            if input_dim + output_dim > 40:
                _column_41[i] = column_41[i]
                temp_list.append(_column_41[i])
                if input_dim + output_dim > 41:
                    _column_42[i] = column_42[i]
                    temp_list.append(_column_42[i])
                if input_dim + output_dim > 42:
                    _column_43[i] = column_43[i]
                    temp_list.append(_column_43[i])
                if input_dim + output_dim > 43:
                    _column_44[i] = column_44[i]
                    temp_list.append(_column_44[i])
                if input_dim + output_dim > 44:
                    _column_45[i] = column_45[i]
                    temp_list.append(_column_45[i])
                if input_dim + output_dim > 45:
                    _column_46[i] = column_46[i]
                    temp_list.append(_column_46[i])
                if input_dim + output_dim > 46:
                    _column_47[i] = column_47[i]
                    temp_list.append(_column_47[i])
                if input_dim + output_dim > 47:
                    _column_48[i] = column_48[i]
                    temp_list.append(_column_48[i])
                if input_dim + output_dim > 48:
                    _column_49[i] = column_49[i]
                    temp_list.append(_column_49[i])
                if input_dim + output_dim > 49:
                    _column_50[i] = column_50[i]
                    temp_list.append(_column_50[i])

            self.data_list.append(temp_list)

        # data normalization -------------------------------------------------------------------------------------------
        self.normalizer = Normalizer(input_dim, output_dim, lower_norm, upper_norm, root_path=self.root_path)

        data = self.normalizer.normalize(self.data_list)

        # set input and output -----------------------------------------------------------------------------------------
        net_input_training = []
        net_output_training = []

        net_input_test = []
        net_output_test = []

        net_input_validation = []
        net_output_validation = []

        net_input_all = []
        net_output_all = []

        # split data
        test_split_number = math.ceil(self.size * test_split)
        validation_split_number = math.ceil(self.size * validation_split)

        randoms = generateList(0, self.size, test_split_number + validation_split_number)

        tests = randoms[0:test_split_number]
        validations = randoms[test_split_number:len(randoms)]

        for i in range(self.size):

            list_in = []
            list_out = []

            j = 0

            while j < input_dim:
                list_in.append(data[i][j])
                j = j + 1

            while j < input_dim + output_dim:
                list_out.append(data[i][j])
                j = j + 1

            net_input_all.append(list_in)
            net_output_all.append(list_out)

            if i in tests:
                net_input_test.append(list_in)
                net_output_test.append(list_out)

            elif i in validations:
                net_input_validation.append(list_in)
                net_output_validation.append(list_out)

            else:
                net_input_training.append(list_in)
                net_output_training.append(list_out)

        # data for training
        self.input_training = numpy.array(net_input_training)
        self.output_training = numpy.array(net_output_training)

        # data for test
        self.input_test = numpy.array(net_input_test)
        self.output_test = numpy.array(net_output_test)

        # data for validation
        self.input_validation = numpy.array(net_input_validation)
        self.output_validation = numpy.array(net_output_validation)

        # all of data
        self.input_all = numpy.array(net_input_all)
        self.output_all = numpy.array(net_output_all)

    def get_inputs(self):
        return self.input_training

    def get_outputs(self):
        return self.output_training

    def get_test_inputs(self):
        return self.input_test

    def get_test_outputs(self):
        return self.output_test

    def get_validation_inputs(self):
        return self.input_validation

    def get_validation_outputs(self):
        return self.output_validation
