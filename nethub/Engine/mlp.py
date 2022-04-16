import os

import numpy as np

import tensorflow.keras as keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

from matplotlib import pyplot as plt

from Engine.network import Net
from Engine.network import activations
from Engine.Util.histories import Histories
from Engine.Util.accuracy import R_squared
import Engine.Util.accuracy as acc
import Engine.network as net

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


# ******************************************* Multi-Layer Perceptron Network *******************************************
class MLP(Net):
    # directories ------------------------------------------------------------------------------------------------------
    parent_directory: str
    working_directory: str

    # options defined in __init__ --------------------------------------------------------------------------------------
    multi_run: bool
    plot: bool
    check_result: bool

    max_loss: float
    max_loss_v: float
    min_accuracy: float
    min_accuracy_v: float

    run_num: int
    epoch: int

    # data -------------------------------------------------------------------------------------------------------------
    data_size: float
    input_test_data: float
    output_test_data: float

    input_all_data: float
    output_all_data: float

    final_training_loss: float
    final_training_accuracy: float

    final_val_loss: float
    final_val_accuracy: float

    final_test_loss: float
    final_test_accuracy: float

    final_all_loss: float
    final_all_accuracy: float

    training_predictions: float
    test_predictions: float
    val_predictions: float
    all_prediction: float

    y_true_training: float
    y_prediction_training: float
    output_training: float

    y_true_test: float
    y_prediction_test: float
    output_test: float

    y_true_val: float
    y_prediction_val: float
    output_val: float

    y_true_all: float
    y_prediction_all: float
    output_all: float

    y_true: float
    y_prediction: float
    output: float

    success = False

    # initialization ===================================================================================================
    def __init__(self, run_num=101, multi_run=False, plot=True, check=False, max_epoch=5000, min_accuracy=0.99,
                 min_accuracy_v=0.99, max_loss=5e-5, max_loss_v=5e-4, parent_directory=''):

        super().__init__()

        self.model = Sequential()

        self.run_num = run_num
        self.multi_run = multi_run
        self.plot = plot
        self.check_result = check
        self.max_epoch = max_epoch
        self.min_accuracy = min_accuracy
        self.min_accuracy_v = min_accuracy_v
        self.max_loss = max_loss
        self.max_loss_v = max_loss_v

        self.parent_directory = parent_directory

        # Create result directory
        try:
            os.mkdir(os.path.join(parent_directory, 'result'))
        except OSError as error:
            pass
            print(error)

        # set output directory
        parent_dir = self.parent_directory

        # new directory
        directory = "Run No. " + str(self.run_num)

        # Path
        path = os.path.join(parent_dir + '\\result', directory)

        # Create directory
        try:
            os.mkdir(path)
        except OSError as error:
            pass
            print(error)

        # set working directory
        self.working_directory = parent_dir + "\\result\\Run No. " + str(self.run_num)

        project_path = os.path.join(self.working_directory, ".project")

        # Create directories
        try:
            os.mkdir(project_path)
        except OSError as error:
            pass
            print(error)

        self.project_path = self.working_directory + "\\.project"

        file = open(self.project_path + '\\architecture.txt', 'w+')
        file.write('')
        file.close()

    # set data =========================================================================================================
    def set_data(self, data):

        # get all data in one array
        self.data = data

        # set training data
        self.input_training_data = data.get_inputs()
        self.output_training_data = data.get_outputs()

        # set validation data
        self.input_validation_data = data.get_validation_inputs()
        self.output_validation_data = data.get_validation_outputs()

        # set test data
        self.input_test_data = data.get_test_inputs()
        self.output_test_data = data.get_test_outputs()

        # set all of data
        self.input_all_data = data.input_all
        self.output_all_data = data.output_all

        # set dimensions
        self.input_dimension = data.input_dim
        self.output_dimension = data.output_dim

        self.data_size = data.size

        try:
            os.mkdir(os.path.join(self.working_directory, '.properties'))
        except OSError as error:
            pass
            print(error)

        try:
            os.mkdir(os.path.join(self.working_directory, '.temp'))
        except OSError as error:
            pass
            print(error)

        # write s and o ------------------------------------------------------------------------------------------------
        file = open(self.working_directory + '\\.properties\\input.properties', 'w')
        file.write('lower bond : [' + str(self.data.normalizer.d_min) + ']\n')
        file.write('upper bond : [' + str(self.data.normalizer.d_max) + ']\n')
        file.write('input dimension : [' + str(self.data.input_dim) + ']\n')
        file.write('output dimension : [' + str(self.data.output_dim) + ']\n')
        file.write('s : ')
        file.write(str(self.data.normalizer.s))
        file.write('\n')
        file.write('o : ')
        file.write(str(self.data.normalizer.o))
        file.write('\n')
        file.close()

        np.savetxt(self.working_directory + '\\.temp\\normalized_training_data.dat',
                   self.data.normalizer.normalized_data, delimiter='\t', fmt='%1.9f')

    # add layer ========================================================================================================
    def add_layer(self, neuron, activation_function=activations.linear, kernel_initializer='uniform',
                  layer_type=Net.HIDDEN_LAYER, kernel_regularizer=None):

        file = open(self.project_path + '\\architecture.txt', 'a')

        # add an input layer -------------------------------------------------------------------------------------------
        if layer_type == Net.INPUT_LAYER:
            self.model.add(Dense(neuron, activation=activation_function, kernel_initializer=kernel_initializer,
                                 input_dim=self.input_dimension, kernel_regularizer=kernel_regularizer))
            file.write('Dense Layer - \tType : INPUT_LAYER \t - \t neurons : [ ' + str(neuron) +
                       ' ] \t - \t activation function : [ ' + activation_function.name + ' ]\n')

        # add an output layer ------------------------------------------------------------------------------------------
        elif layer_type == Net.OUTPUT_LAYER:
            self.model.add(Dense(neuron, activation=activation_function, kernel_initializer=kernel_initializer,
                                 kernel_regularizer=kernel_regularizer))
            file.write('Dense Layer - \tType : OUTPUT_LAYER \t - \t neurons : [ ' + str(neuron) +
                       ' ] \t - \t activation function : [ ' + activation_function.name + ' ]\n')

            if neuron != self.output_dimension:
                raise NameError('The Number of Neurons in Output Layer must be equal to Output Dimension in Raw Data')

        # add a hidden layer -------------------------------------------------------------------------------------------
        else:
            self.model.add(Dense(neuron, activation=activation_function, kernel_initializer=kernel_initializer,
                                 kernel_regularizer=kernel_regularizer))
            file.write('Dense Layer - \tType : HIDDEN_LAYER \t - \t neurons : [ ' + str(neuron) +
                       ' ] \t - \t activation function : [ ' + activation_function.name + ' ]\n')

        file.close()

    # compile network ==================================================================================================
    def compile(self, optimizer=net.optimizers.Adam, loss=keras.losses.mse, metrics=None):

        if metrics is None:
            metrics = [R_squared]

        self.model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    # model execution ==================================================================================================
    def exe(self, multi_processing=True, verbose=1, batch_split=0.2):

        # setting history
        histories = Histories(max_loss=self.max_loss, min_accuracy=self.min_accuracy,
                              max_loss_v=self.max_loss_v, min_accuracy_v=self.min_accuracy_v,
                              run_number=self.run_num)

        batch_size = int(self.data_size * batch_split)

        # training network ---------------------------------------------------------------------------------------------
        self.model.fit(self.input_training_data, self.output_training_data,
                       epochs=self.max_epoch,
                       batch_size=batch_size,
                       callbacks=[histories],
                       validation_data=(self.input_validation_data, self.output_validation_data),
                       use_multiprocessing=multi_processing,
                       verbose=verbose)

        # result creation ----------------------------------------------------------------------------------------------
        result_output = []

        if len(histories.losses) == self.max_epoch:
            self.epoch = self.max_epoch
            if self.check_result:
                return
        else:
            self.epoch = len(histories.losses)
            self.success = True

        for i in range(self.epoch):

            if histories.accuracies[i] < 0:
                histories.accuracies[i] = 0

            if histories.val_accuracies[i] < 0:
                histories.val_accuracies[i] = 0

            result_output.append([i + 1, histories.losses[i], histories.val_losses[i],
                                  histories.accuracies[i], histories.val_accuracies[i]])

        result = np.array(result_output)

        # save result into a txt file ----------------------------------------------------------------------------------
        result_file_name = self.working_directory + "\\result.txt"
        np.savetxt(result_file_name, result, delimiter="\t", fmt='%1.9f',
                   header='Epoch\tloss\t\t\tval loss\t\taccuracy\t\tval accuracy')

        self.final_training_loss = result[len(result[:, 1]) - 1, 1]
        self.final_training_accuracy = result[len(result[:, 3]) - 1, 3]

        self.final_val_loss = result[len(result[:, 2]) - 1, 2]
        self.final_val_accuracy = result[len(result[:, 4]) - 1, 4]

        # creates a HDF5 file 'my_model.h5' ----------------------------------------------------------------------------
        self.model.save(self.working_directory + '\\my_model.h5')
        self.model.save_weights(self.working_directory + '\\my_model_weights.h5')

        # save and plot --- loss ---------------------------------------------------------------------------------------
        plt.figure()
        plt.semilogy(result[:, 0], result[:, 1], 'b-')
        plt.semilogy(result[:, 0], result[:, 2], 'r-')
        plt.ylabel('Loss')
        plt.xlabel('Epoch')
        plt.legend(['Training', 'Validation'])
        plt.savefig(self.working_directory + '\\loss.png', dpi=300, bbox_inches='tight')

        if self.plot:
            plt.show()
        else:
            plt.close('all')

        # save and plot --- accuracy -----------------------------------------------------------------------------------
        plt.figure()
        plt.plot(result[:, 0], result[:, 3], 'b.')
        plt.plot(result[:, 0], result[:, 4], 'r.')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.legend(['Training', 'Validation'])
        plt.savefig(self.working_directory + '\\accuracy.png', dpi=300, bbox_inches='tight')

        if self.plot:
            plt.show()
        else:
            plt.close('all')

    # get data from model (prediction) =================================================================================
    def prediction(self):

        # --- prediction -----------------------------------------------------------------------------------------------
        self.training_predictions = self.model.predict(self.input_training_data)
        self.test_predictions = self.model.predict(self.input_test_data)
        self.val_predictions = self.model.predict(self.input_validation_data)
        self.all_prediction = self.model.predict(self.input_all_data)

        # --- training evaluation --------------------------------------------------------------------------------------
        self.y_true_training = np.transpose(self.output_training_data).tolist()
        self.y_prediction_training = np.transpose(self.training_predictions).tolist()
        self.output_training = np.transpose(np.vstack((self.y_true_training, self.y_prediction_training)))

        self.final_training_loss = acc.mse(self.y_true_training, self.y_prediction_training)
        self.final_training_accuracy = acc.r_squared(self.y_true_training, self.y_prediction_training)

        # --- test evaluation ------------------------------------------------------------------------------------------
        self.y_true_test = np.transpose(self.output_test_data).tolist()
        self.y_prediction_test = np.transpose(self.test_predictions).tolist()
        self.output_test = np.transpose(np.vstack((self.y_true_test, self.y_prediction_test)))

        self.final_test_loss = acc.mse(self.y_true_test, self.y_prediction_test)
        self.final_test_accuracy = acc.r_squared(self.y_true_test, self.y_prediction_test)

        # --- validation evaluation ------------------------------------------------------------------------------------
        self.y_true_val = np.transpose(self.output_validation_data).tolist()
        self.y_prediction_val = np.transpose(self.val_predictions).tolist()
        self.output_val = np.transpose(np.vstack((self.y_true_val, self.y_prediction_val)))

        # --- all data evaluation --------------------------------------------------------------------------------------
        self.y_true_all = np.transpose(self.output_all_data).tolist()
        self.y_prediction_all = np.transpose(self.all_prediction).tolist()
        self.output_all = np.transpose(np.vstack((self.y_true_all, self.y_prediction_all)))

        self.final_all_loss = acc.mse(self.y_true_all, self.y_prediction_all)
        self.final_all_accuracy = acc.r_squared(self.y_true_all, self.y_prediction_all)

        if self.final_training_accuracy >= self.min_accuracy:
            if self.final_test_accuracy >= self.min_accuracy_v:
                if self.final_val_accuracy >= self.min_accuracy_v:
                    self.success = True

        # saving Evaluation of training results ------------------------------------------------------------------------
        result_file_name = self.working_directory + "\\regression_train.txt"
        np.savetxt(result_file_name, self.output_training, delimiter="\t", fmt='%1.9f', header='--- true ---\t\t--- '
                                                                                               'prediction ---')

        # saving Evaluation of test results ----------------------------------------------------------------------------
        result_file_name = self.working_directory + "\\regression_test.txt"
        np.savetxt(result_file_name, self.output_test, delimiter="\t", fmt='%1.9f', header='--- true ---\t\t--- '
                                                                                           'prediction ---')

        # saving Evaluation of validation results ----------------------------------------------------------------------
        result_file_name = self.working_directory + "\\regression_validation.txt"
        np.savetxt(result_file_name, self.output_val, delimiter="\t", fmt='%1.9f', header='--- true ---\t\t--- '
                                                                                          'prediction ---')

        # saving Evaluation of all results ----------------------------------------------------------------------
        result_file_name = self.working_directory + "\\regression_all.txt"
        np.savetxt(result_file_name, self.output_all, delimiter="\t", fmt='%1.9f', header='--- true ---\t\t--- '
                                                                                          'prediction ---')

        # plot training regression -------------------------------------------------------------------------------------
        plt.figure()
        plt.plot(self.training_predictions, self.output_training_data, 'ro', label='line 1')
        plt.plot([self.data.normalizer.d_min, 0, self.data.normalizer.d_max],
                 [self.data.normalizer.d_min, 0, self.data.normalizer.d_max], 'b-', label='line 2')
        plt.xlabel('Prediction')
        plt.ylabel('Experimental')
        plt.title('Training')
        plt.savefig(self.working_directory + '\\regression_train.png', dpi=300, bbox_inches='tight')
        plt.close()

        # plot test regression -----------------------------------------------------------------------------------------
        plt.figure()
        plt.plot(self.test_predictions, self.output_test_data, 'ro', label='line 1')
        plt.plot([self.data.normalizer.d_min, 0, self.data.normalizer.d_max],
                 [self.data.normalizer.d_min, 0, self.data.normalizer.d_max], 'b-', label='line 2')
        plt.xlabel('Prediction')
        plt.ylabel('Experimental')
        plt.title('Test')
        plt.savefig(self.working_directory + '\\regression_test.png', dpi=300, bbox_inches='tight')
        plt.close()

        # plot validation regression -----------------------------------------------------------------------------------
        plt.figure()
        plt.plot(self.val_predictions, self.output_validation_data, 'ro', label='line 1')
        plt.plot([self.data.normalizer.d_min, 0, self.data.normalizer.d_max],
                 [self.data.normalizer.d_min, 0, self.data.normalizer.d_max], 'b-', label='line 2')
        plt.xlabel('Prediction')
        plt.ylabel('Experimental')
        plt.title('Validation')
        plt.savefig(self.working_directory + '\\regression_validation.png', dpi=300, bbox_inches='tight')
        plt.close()

        # plot regression (all) ----------------------------------------------------------------------------------------
        plt.figure()
        plt.plot(self.training_predictions, self.output_training_data, 'ro', label='line 1')
        plt.plot(self.test_predictions, self.output_test_data, 'bo', label='line 2')
        plt.plot(self.val_predictions, self.output_validation_data, 'go', label='line 3')
        plt.plot([self.data.normalizer.d_min, 0, self.data.normalizer.d_max],
                 [self.data.normalizer.d_min, 0, self.data.normalizer.d_max], 'b-', label='line 4')
        plt.xlabel('Prediction')
        plt.ylabel('Experimental')
        plt.title('All')
        if self.output_dimension == 1:
            plt.legend(['Training', 'Test', 'Validation'])
        plt.savefig(self.working_directory + '\\regression_all.png', dpi=300, bbox_inches='tight')

        if self.plot:
            plt.show()
        else:
            plt.close('all')

    def trained_model_prediction(self, file_path, input_data, output_data):

        path = os.path.join(file_path, 'result from trained model')
        try:
            os.mkdir(path)
        except OSError as error:
            print(error)
        working_dir = file_path + '\\result from trained model'

        # --- prediction -----------------------------------------------------------------------------------------------
        my_prediction = self.model.predict(input_data)
        # ------------ evaluation --------------------------------------------------------------------------------------
        y_true = np.transpose(output_data).tolist()
        y_prediction = np.transpose(my_prediction).tolist()

        output = np.transpose(np.vstack((y_true, y_prediction)))

        loss = acc.mse(y_true, y_prediction)
        accuracy = acc.r_squared(y_true, y_prediction)

        # saving Evaluation of training results ------------------------------------------------------------------------
        result_file_name = working_dir + "\\regression.txt"
        np.savetxt(result_file_name, output, delimiter="\t", fmt='%1.9f', header='--- true ---\t\t--- '
                                                                                 'prediction ---')

        # plot training regression -------------------------------------------------------------------------------------
        plt.figure()
        plt.plot(my_prediction, output_data, 'ro', label='line 1')
        plt.plot([-1, 0, 1], [-1, 0, 1], 'b-', label='line 2')
        plt.xlabel('Prediction')
        plt.ylabel('Experimental')
        plt.savefig(working_dir + '\\regression.png', dpi=300, bbox_inches='tight')
        plt.close()

        if self.plot:
            plt.show()
        else:
            plt.close('all')

        print('# prediction finished successfully\n### loss :', loss, '\taccuracy :', accuracy)

    def get_prediction(self, input_data, output_data):

        self.predictions = self.model.predict(input_data)

        self.y_true = np.transpose(output_data).tolist()
        self.y_prediction = np.transpose(self.predictions).tolist()
        self.output = np.transpose(np.vstack((self.y_true, self.y_prediction)))

        return self.y_prediction

    def get_final_training_loss(self):
        return self.final_training_loss

    def get_final_training_accuracy(self):
        return self.final_training_accuracy

    def get_final_val_loss(self):
        return self.final_val_loss

    def get_final_val_accuracy(self):
        return self.final_val_accuracy

    def get_final_all_loss(self):
        return self.final_all_loss

    def get_final_all_accuracy(self):
        return self.final_all_accuracy
