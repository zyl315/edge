import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.1)
y = 1 / np.pi * np.arctan(x) + 0.5

plt.figure()
plt.plot(x, y)
plt.ylabel("$f(r_{i,j})$")
plt.xlabel("$r_{i,j}$")
plt.title("$f(r_{i,j})=\\frac{1}{\pi}arctan(r_{i,j})+\\frac{1}{2}$")
plt.show()
