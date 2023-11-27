import numpy as np
import matplotlib.pyplot as plt

lista = []

data = np.array([[1.0, 3.0], [2.0, 1.0], [3.5,4.], [5., 0.], [6., 0.5], [9., -2.], [9.5, -3.0]])

x_space = []

def s(x, yi, yi1, ti, ti1):
    return ((yi1-yi)/(ti1-ti)) * (x - ti) + yi

for i in range(data.shape[0]-1):
    if i == 0:
        iksy = np.linspace(0, data[i+1][0], 20)
    elif i == data.shape[0]-2:
        iksy = np.linspace(data[i][0], 10, 20)
    else:
        iksy = np.linspace(data[i][0], data[i + 1][0], 20)

    x_space.extend(iksy)
    interpolated = s(iksy, data[i][1], data[i + 1][1], data[i][0], data[i + 1][0])
    lista.extend(interpolated)
else:
    plt.scatter([data[i][0] for i in range(data.shape[0])], [data[i][1] for i in range(data.shape[0])])
    plt.plot(x_space, lista)
    plt.show()