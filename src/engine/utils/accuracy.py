# created by Milad Molaee: miladmolaee@hotmail.com  -  May 2019
#

import numpy
from tensorflow.keras import backend


# define new accuracy : R^2 --------------------------------------------------------------------------------------------
def r_squared(y_true, y_pred):
    """define new accuracy : R^2

    Arguments:
        y_true -- _description_
        y_pred -- _description_

    Returns:
        _description_
    """
    print('type yt:', type(y_true), ', type yp:', type(y_pred))
    print('-'*30)
    print('yt:', y_true)
    print('-'*30)
    print('yp:', y_pred)
    print('-'*30)

    SS_res = backend.sum(backend.square(y_true - y_pred))
    SS_tot = backend.sum(backend.square(y_true - backend.mean(y_true)))
    r2 = 1 - SS_res / (SS_tot + backend.epsilon())

    return r2


def r_squared_np(y_true, y_pred):

    y1 = numpy.subtract(y_pred, y_true)
    y2 = numpy.subtract(y_pred, numpy.mean(y_true))

    ys1 = numpy.square(y1)
    ys2 = numpy.square(y2)

    S1 = numpy.sum(ys1)
    S2 = numpy.sum(ys2)

    r2 = 1 - S1 / (S2 + 10**-30)

    return r2


def mse(y_true, y_pred):
    """calculation of "mean squre error"

    Arguments:
        y_true -- _description_
        y_pred -- _description_

    Returns:
        _description_
    """

    y1 = numpy.subtract(y_true, y_pred)
    y2 = numpy.square(y1)
    y3 = numpy.mean(y2)

    return y3
