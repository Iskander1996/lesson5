import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01)
plt.plot(x, np.cos(x), x, np.sin(x), x, -x)
plt.show
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f_1(x) = cos(x), f_2(x) = sin(x), f_3(x) = -x$')
plt.grid(True)