
import platform

class Sound:

    def __init__(self):
        
        self.platform = platform.system() 

        if self.platform == 'Windows':
            import winsound

    def say_error(self):
        pass

    def say_start(self):

        if self.platform == 'Windows':
            winsound.Beep(1000, 500)

    def say_finished_ok(self):
        if self.platform == 'Windows':
            winsound.Beep(1000, 1500)   

    def say_finished_not_acceptable(self):
        if self.platform == 'Windows':
            winsound.Beep(2000, 500)