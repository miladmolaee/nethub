import numpy
from tensorflow.keras import backend


# define new accuracy : R^2 --------------------------------------------------------------------------------------------
def R_squared(y_true, y_pred):

    SS_res = backend.sum(backend.square(y_true - y_pred))
    SS_tot = backend.sum(backend.square(y_true - backend.mean(y_true)))
    r2 = 1 - SS_res / (SS_tot + backend.epsilon())

    return r2


def r_squared(y_true, y_pred):

    y1 = numpy.subtract(y_pred, y_true)
    y2 = numpy.subtract(y_pred, numpy.mean(y_true))

    ys1 = numpy.square(y1)
    ys2 = numpy.square(y2)

    S1 = numpy.sum(ys1)
    S2 = numpy.sum(ys2)

    r2 = 1 - S1 / (S2 + 10**-30)

    return r2


def mse(y_true, y_pred):

    y1 = numpy.subtract(y_true, y_pred)
    y2 = numpy.square(y1)
    y3 = numpy.mean(y2)

    return y3
