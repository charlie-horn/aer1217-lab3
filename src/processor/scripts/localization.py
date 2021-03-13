import numpy as np

class Localizer():
    def __init__(self):
        self.best_guess = np.empty((2,6))
        return

    def localize(self, pixels, pos):
        return self.best_guess
