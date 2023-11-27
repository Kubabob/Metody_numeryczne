import numpy as np
import matplotlib.pyplot as plt

dynamic_czebyszef = {}
def czebyszef(x, n):
    if x in dynamic_czebyszef.keys():
        if n in dynamic_czebyszef[x].keys():
            return dynamic_czebyszef[x][n]
        else:
            if n == 0:
                dynamic_czebyszef[x][n] = 1
                return 1
            elif n == 1:
                dynamic_czebyszef[x][n] = x
                return x
            else:
                dynamic_czebyszef[x][n] = 2*x*czebyszef(x, n-1) - czebyszef(x, n-2)
                return 2*x*czebyszef(x, n-1) - czebyszef(x, n-2)
    else:
        if n == 0:
            dynamic_czebyszef[x] = {n:1}
            return 1
        elif n == 1:
            dynamic_czebyszef[x] = {n:x}
            return x
        else:
            dynamic_czebyszef[x] = {n:2 * x * czebyszef(x, n-1) - czebyszef(x, n-2)}
            return 2 * x * czebyszef(x, n-1) - czebyszef(x, n-2)


stopien = 10
x_space = np.linspace(-1,1,100)
[czebyszef(x, stopien) for x in x_space]
print(dynamic_czebyszef)

wartosci_wielomianow = np.array([[dynamic_czebyszef[x][n] for n in range(stopien)] for x in x_space])
for i in range(stopien):
    plt.plot(x_space, [wartosci_wielomianow[x][i] for x in range(len(x_space))])
else:
    plt.show()


