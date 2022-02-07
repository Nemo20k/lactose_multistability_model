from logging import CRITICAL
import numpy as np

TMG_CRITICAL_AMOUNT = 10**6


def sigmoid(x):
    return 1/(1 + np.exp(-x)) - 0.5


class TestMS:
    def __init__(self, number_of_bacteria: int, TMG_rate: float, GLU_rate: float):
        self.bacteria: np.ndarray = np.zeros(number_of_bacteria, bool)
        self.TMG_rate: float = TMG_rate
        self.TMG_amount: float = 0
        self.GLU_amount = 0
        self.GLU_rate: float = GLU_rate
        self.p_to_double_TMG_amount: float = 0
        self.bacteria_history = [self.bacteria]
        self.green_history = []
        self.TMG_history = []
        self.save_history()

    def next_time_step(self):
        self.TMG_amount += self.TMG_rate
        self.GLU_amount += self.GLU_rate
        turned_to_green = np.random.binomial(1, p=self.p_switch_color, size=self.bacteria.size)
        self.bacteria =  self.bacteria | turned_to_green
        self.save_history()

    def save_history(self):
        self.bacteria_history.append(self.bacteria)
        self.green_history.append((self.bacteria.nonzero()[0].size))
        self.TMG_history.append(self.TMG_amount)
        
    @property
    def p_switch_color(self):
        return sigmoid(self.TMG_amount - self.GLU_amount)
