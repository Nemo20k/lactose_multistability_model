from logging import CRITICAL
import numpy as np

TMG_CRITICAL_AMOUNT = 10**6


def sigmoid(x):
    return 1/(1 + np.exp(-x)) - 0.5


class TestMS:
    def __init__(self, number_of_bacteria: int, TMG_amount: float=0, GLU_amount: float=0, TMG_rate: float=0, GLU_rate: float=0):
        self.bacteria: np.ndarray = np.zeros(number_of_bacteria, bool)
        self.TMG_rate: float = TMG_rate
        self.TMG_amount: float = TMG_amount
        self.GLU_amount = GLU_amount
        self.GLU_rate: float = GLU_rate
        self.switch_to_green = 0
        self.switch_to_red = 0
        self.switch_double_TMG_amount: float = 0
        self.bacteria_history = [self.bacteria]
        self.green_history = []
        self.TMG_history = []
        self.GLU_history = []
        self.save_history()

    def next_time_step(self):

        # update the amounts and switchs
        self.TMG_amount += self.TMG_rate
        self.GLU_amount += self.GLU_rate
        self.switch_to_green += self.TMG_amount - self.GLU_amount
        self.switch_double_TMG_amount += self.TMG_amount - self.GLU_amount

        # update the bacteria state accordingly
        turned_to_green = np.random.binomial(1, p=self.switch_to_green, size=self.bacteria.size) & self.bacteria
        turned_to_red = np.random.binomial(1, p=(1-self.switch_to_green), size=self.bacteria.size) & self.bacteria
        self.bacteria = self.bacteria + turned_to_green - turned_to_red

        self.save_history()

    def save_history(self):
        self.bacteria_history.append(self.bacteria)
        self.green_history.append((self.bacteria.nonzero()[0].size))
        self.TMG_history.append(self.TMG_amount)
        self.GLU_history.append(self.GLU_amount)
        
    @property
    def p_switch_green(self):
        return logistic_func(self.switch_to_green - 100)

    @property
    def p_switch_red(self):
        return logistic_func(self.GLU_amount - 100)

    @property
    def p_double_TMG(self):
        return logistic_func(self.switch_double_TMG_amount - 100)

