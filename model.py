import numpy as np
from matplotlib import pyplot as plt
import imageio

# ---------------    Model Class  -----------------------------------

def logistic_func(x):

    return 1/(1 + np.exp(-x))
class TestMS:
    def __init__(self, number_of_bacteria: int, TMG_amount: float=0, GLU_amount: float=0, TMG_rate: float=0, GLU_rate: float=0,
    init_switch_green: float=0, init_switch_double_TMG: float=0):
        self.bacteria: np.ndarray = np.zeros(number_of_bacteria, bool)
        self.TMG_rate: float = TMG_rate
        self.TMG_amount: float = TMG_amount
        self.GLU_amount = GLU_amount
        self.GLU_rate: float = GLU_rate
        self.switch_to_green = init_switch_green
        self.switch_double_TMG_amount: float = init_switch_double_TMG
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

# ------------------------------------------------------------------
if __name__ == "__name__":
# ---------------    Script  -----------------------------------
    # parameters
    number_of_bactria = 10000
    TMG_initial_amount = 0
    GLU_initial_amount = 0
    TMG_rate = 1
    GLU_rate = 0.1
    number_of_timesteps = 100

    model_object = TestMS(number_of_bactria, TMG_initial_amount, GLU_initial_amount, TMG_rate, GLU_rate)

    for timestep in range(number_of_timesteps):
        model_object.next_time_step()
    
# ---------------  graphs ---------------------------------------
    #  GRAPH 1 - number of green bacteria as function of TMG level
    title = "number of green bacteria as function of TMG level"
    x_title = "TMG level"
    y_title = "number of green bacteria"

    x_data = model_object.TMG_history
    y_data = model_object.green_history
    plt.grid()
    plt.plot(x_data, y_data)

    #  GRAPH 2 - .gif File of bacteria visual
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave('/path/to/movie.gif', images)








