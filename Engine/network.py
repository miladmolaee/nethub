from keras import optimizers
from keras import activations


class Net:

    # constants --------------------------------------------------------------------------------------------------------
    INPUT_LAYER: str = 'input-layer'
    OUTPUT_LAYER: str = 'output-layer'
    HIDDEN_LAYER: str = 'hidden-layer'

    # data -------------------------------------------------------------------------------------------------------------
    data: object

    input_training_data: object
    output_training_data: object

    input_validation_data: object
    output_validation_data: object

    input_dimension: int
    output_dimension: int

    batch_size: int

    # network structure ------------------------------------------------------------------------------------------------
    layers: list

    # execution --------------------------------------------------------------------------------------------------------
    max_epoch: int

    # result -----------------------------------------------------------------------------------------------------------
    predictions: object

    # *************************************************** optimizers ***************************************************
    class optimizers:
        # ==================================================== SGD =====================================================
        # keras.optimizers.SGD(lr=0.01, momentum=0.0, decay=0.0, nesterov=False)
        #
        # • lr: float >= 0. Learning rate.
        # • momentum: float >= 0. Parameter updates momentum.
        # • decay: float >= 0. Learning rate decay over each update.
        # • nesterov: boolean. Whether to apply Nesterov momentum.

        SGD = optimizers.SGD()
        # --------------------------------------------------------------------------------------------------------------

        # ================================================== RMSprop ===================================================
        # keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)
        #
        # • lr: float >= 0. Learning rate.
        # • rho: float >= 0.
        # • epsilon: float >= 0. Fuzz factor.
        # • decay: float >= 0. Learning rate decay over each update.

        RMSprop = optimizers.RMSprop()
        # --------------------------------------------------------------------------------------------------------------

        # =================================================== Adagrad ==================================================
        # keras.optimizers.Adagrad(lr=0.01, epsilon=1e-08, decay=0.0)
        #
        # • lr: float >= 0. Learning rate.
        # • epsilon: float >= 0.
        # • decay: float >= 0. Learning rate decay over each update.

        Adagrad = optimizers.Adagrad()
        # --------------------------------------------------------------------------------------------------------------

        # ================================================== Adadelta ==================================================
        # keras.optimizers.Adadelta(lr=1.0, rho=0.95, epsilon=1e-08, decay=0.0)
        #
        # • lr: float >= 0. Learning rate. It is recommended to leave it at the default value.
        # • rho: float >= 0.
        # • epsilon: float >= 0. Fuzz factor.
        # • decay: float >= 0. Learning rate decay over each update.

        Adadelta = optimizers.Adadelta()
        # --------------------------------------------------------------------------------------------------------------

        # ==================================================== Adam ====================================================
        # keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
        #
        # • lr: float >= 0. Learning rate.
        # • beta_1: float, 0 < beta < 1. Generally close to 1.
        # • beta_2: float, 0 < beta < 1. Generally close to 1.
        # • epsilon: float >= 0. Fuzz factor.
        # • decay: float >= 0. Learning rate decay over each update.

        Adam = optimizers.Adam()
        # --------------------------------------------------------------------------------------------------------------

        # =================================================== Adamax ===================================================
        # keras.optimizers.Adamax(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
        #
        # • lr: float >= 0. Learning rate.
        # • beta_1: float, 0 < beta < 1. Generally close to 1.
        # • beta_2: float, 0 < beta < 1. Generally close to 1.
        # • epsilon: float >= 0. Fuzz factor.
        # • decay: float >= 0. Learning rate decay over each update.

        Adamax = optimizers.Adamax()
        # --------------------------------------------------------------------------------------------------------------

        # =================================================== Nadam ====================================================
        # keras.optimizers.Nadam(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=1e-08, schedule_decay=0.004)
        #
        # • lr: float >= 0. Learning rate.
        # • beta_1: float, 0 < beta < 1. Generally close to 1.
        # • beta_2: float, 0 < beta < 1. Generally close to 1.
        # • epsilon: float >= 0. Fuzz factor.
        # • decay: float >= 0. Learning rate decay over each update.

        Nadam = optimizers.Nadam()
        # --------------------------------------------------------------------------------------------------------------

        # =================================================== Ftrl ====================================================
        # keras.optimizers.Ftrl(
        #                learning_rate=0.001,
        #                learning_rate_power=-0.5,
        #                initial_accumulator_value=0.1,
        #                l1_regularization_strength=0.0,
        #                l2_regularization_strength=0.0,
        #                l2_shrinkage_regularization_strength=0.0)
        #
        # • lr: float >= 0. Learning rate.
        # • beta_1: float, 0 < beta < 1. Generally close to 1.
        # • beta_2: float, 0 < beta < 1. Generally close to 1.
        # • epsilon: float >= 0. Fuzz factor.
        # • decay: float >= 0. Learning rate decay over each update.

        Ftrl = optimizers.Ftrl()
        # --------------------------------------------------------------------------------------------------------------

    # ********************************************** activation functions **********************************************
    class activations:
        # =================================================== relu =====================================================
        # keras.activations.relu(x, alpha=0., max_value=None, threshold=0)

        relu = activations.relu
        relu.name = 'relu'
        # --------------------------------------------------------------------------------------------------------------

        # =================================================== elu ======================================================
        # keras.activations.elu(x, alpha=1.0)

        elu = activations.elu
        elu.name = 'elu'
        # --------------------------------------------------------------------------------------------------------------

        # ================================================== selu ======================================================
        # keras.activations.selu(x)

        selu = activations.selu
        selu.name = 'selu'
        # --------------------------------------------------------------------------------------------------------------

        # ================================================= linear =====================================================
        # keras.activations.linear(x)

        linear = activations.linear
        linear.name = 'linear'
        # --------------------------------------------------------------------------------------------------------------

        # =================================================== tanh =====================================================
        # keras.activations.tanh(x)

        tanh = activations.tanh
        tanh.name = 'tanh'
        # --------------------------------------------------------------------------------------------------------------

        # ================================================= sigmoid ====================================================
        # keras.activations.sigmoid(x)

        sigmoid = activations.sigmoid
        sigmoid.name = 'sigmoid'
        # --------------------------------------------------------------------------------------------------------------

        # =============================================== hard_sigmoid =================================================
        # keras.activations.hard_sigmoid(x)

        hard_sigmoid = activations.hard_sigmoid
        hard_sigmoid.name = 'hard_sigmoid'
        # --------------------------------------------------------------------------------------------------------------

        # ================================================= softmax ====================================================
        # keras.activations.softmax(x, axis=-1)

        softmax = activations.softmax
        softmax.name = 'softmax'
        # --------------------------------------------------------------------------------------------------------------

        # ================================================= softsign ===================================================
        # keras.activations.softsign(x)

        softsign = activations.softsign
        softsign.name = 'softsign'
        # --------------------------------------------------------------------------------------------------------------

        # ================================================= softplus ===================================================
        # keras.activations.softplus(x)

        softplus = activations.softplus
        softplus.name = 'softplus'
        # --------------------------------------------------------------------------------------------------------------

        # =============================================== exponential ==================================================
        # keras.activations.exponential(x)

        exponential = activations.exponential
        exponential.name = 'exponential'
        # --------------------------------------------------------------------------------------------------------------

    def __str__(self):
        return 'this is a neural network'
