
from tensorflow.keras import optimizers

# *************************************************** optimizers ***************************************************
class Optimizers:
    # ==================================================== SGD =====================================================
    # keras.optimizers.SGD(lr=0.01, momentum=0.0, decay=0.0, nesterov=False)
    #
    # • lr: float >= 0. Learning rate.
    # • momentum: float >= 0. Parameter updates momentum.
    # • decay: float >= 0. Learning rate decay over each update.
    # • nesterov: boolean. Whether to apply Nesterov momentum.

    SGD = optimizers.SGD
    # --------------------------------------------------------------------------------------------------------------

    # ================================================== RMSprop ===================================================
    # keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)
    #
    # • lr: float >= 0. Learning rate.
    # • rho: float >= 0.
    # • epsilon: float >= 0. Fuzz factor.
    # • decay: float >= 0. Learning rate decay over each update.

    RMSprop = optimizers.RMSprop
    # --------------------------------------------------------------------------------------------------------------

    # =================================================== Adagrad ==================================================
    # keras.optimizers.Adagrad(lr=0.01, epsilon=1e-08, decay=0.0)
    #
    # • lr: float >= 0. Learning rate.
    # • epsilon: float >= 0.
    # • decay: float >= 0. Learning rate decay over each update.

    Adagrad = optimizers.Adagrad
    # --------------------------------------------------------------------------------------------------------------

    # ================================================== Adadelta ==================================================
    # keras.optimizers.Adadelta(lr=1.0, rho=0.95, epsilon=1e-08, decay=0.0)
    #
    # • lr: float >= 0. Learning rate. It is recommended to leave it at the default value.
    # • rho: float >= 0.
    # • epsilon: float >= 0. Fuzz factor.
    # • decay: float >= 0. Learning rate decay over each update.

    Adadelta = optimizers.Adadelta
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

    Adamax = optimizers.Adamax
    # --------------------------------------------------------------------------------------------------------------

    # =================================================== Nadam ====================================================
    # keras.optimizers.Nadam(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=1e-08, schedule_decay=0.004)
    #
    # • lr: float >= 0. Learning rate.
    # • beta_1: float, 0 < beta < 1. Generally close to 1.
    # • beta_2: float, 0 < beta < 1. Generally close to 1.
    # • epsilon: float >= 0. Fuzz factor.
    # • decay: float >= 0. Learning rate decay over each update.

    Nadam = optimizers.Nadam
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

    Ftrl = optimizers.Ftrl
    # --------------------------------------------------------------------------------------------------------------

