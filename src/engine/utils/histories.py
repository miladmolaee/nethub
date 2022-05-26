# created by Milad Molaee: miladmolaee@hotmail.com  -  May 2019
#

from typing import Any, List

from tensorflow.keras.callbacks import Callback


# History class for managing and saving each Epoch ---------------------------------------------------------------------
class Histories(Callback):
    """History class for managing and saving each Epoch

    Arguments:
        Callback -- _description_
    """

    accuracies: List[Any]
    losses: List[Any]

    val_accuracies: List[Any]
    val_losses: List[Any]

    max_loss: float
    min_accuracy: float

    max_loss_v: float
    min_accuracy_v: float

    finished_epoch: int

    is_stopped_training: bool = False

    finished_by: str


    def __init__(self, max_loss, min_accuracy, max_loss_v, min_accuracy_v, run_number):
        super(Histories, self).__init__()

        self.max_loss = max_loss
        self.max_loss_v = max_loss_v

        self.min_accuracy = min_accuracy
        self.min_accuracy_v = min_accuracy_v

        self.run_number = run_number

    def on_train_begin(self, logs=None):
        self.losses = []
        self.accuracies = []

        self.val_losses = []
        self.val_accuracies = []

    def on_epoch_end(self, epoch, logs=None):

        self.losses.append(logs.get('loss'))
        self.accuracies.append(logs.get('r_squared'))

        self.val_losses.append(logs.get('val_loss'))
        self.val_accuracies.append(logs.get('val_r_squared'))

        if (epoch > 100) and (logs.get('r_squared') > self.min_accuracy and (
                logs.get('val_r_squared') >= self.min_accuracy_v or logs.get('val_loss') <= self.max_loss_v)):
            self.model.stop_training = True
            self.is_stopped_training = True
            self.finished_epoch = epoch

            if logs.get('val_r_squared') >= self.min_accuracy_v:
                self.finished_by = ' \"accuracy\" '
            else:
                self.finished_by = ' \"loss\" '

    def on_train_end(self, logs=None):
        if self.is_stopped_training:
            print(' # [ Training Finished by ', self.finished_by, ' at __epoch :', self.finished_epoch, ']')
        else:
            print(' # [ Training Finished without acceptable result ]')
