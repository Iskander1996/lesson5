import numpy as np

x = 1
y = 10
z = 100
def f(x):
    return np.log(np.exp(1/(np.sin(x)+1))/(5/4 + 1/(x**15)))/np.log(1+x**2)

print("f(1) = ",f(x))
print("f(10) = ", f(y))
print("f(100) =", f(z))

