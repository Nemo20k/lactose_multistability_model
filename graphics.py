from matplotlib import pyplot as plt
import numpy as np

def plot_bacteria(bacteria_ndarray: np.ndarray, dimensions: tuple, save_path: str = None, cmap: str='prism'):
    im = bacteria_ndarray.reshape(dimensions)
    fig = plt.imshow(im, cmap=cmap, vmin=0, vmax=1)
    plt.title('Red/Green graphic distribution')
    if save_path:
        fig.write_png(save_path)

def plot_green_TMG(green_history):
    pass
    pass

def create_gif(history_ndarray):
    pass
