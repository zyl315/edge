import matplotlib.pyplot as plt
import numpy as np




def fun(x:float):
    y = 1 / np.pi * np.arcsin(x) + 0.5
    print(y)

def fun2(x:float):
    y = 1 / (1 + np.exp(1 - 2*x))
    print("x=%.2f y=%.2f" % (x, y))

def paint1():
    x = np.arange(0, 1, 0.1)
    y = 1 / np.pi * np.arcsin(x) + 0.5
    plt.figure(dpi=200)
    plt.plot(x, y)
    plt.ylabel("$f(r_{i,j})$")
    plt.xlabel("$r_{i,j}$")
    plt.title("$f(r_{i,j})=\\frac{1}{\pi}arctan(r_{i,j})+\\frac{1}{2}$")
    plt.show()

def paint2():
    x = np.arange(-5, 5, 0.1)
    y = 1 / (1 + np.exp(1 - 2*x))
    plt.figure(dpi=400)
    plt.plot(x, y)
    plt.ylabel("$R(q_{i,j})$")
    plt.xlabel("x")
    plt.title("$R({q_{i,j}}) = (\\frac{1}{{1 + {e^{1{\\rm{ - }}{2 \cdot (r_{i,j} + \gamma \cdot q_{i,j})}}}}}),$")
    plt.show()



if __name__ == '__main__':
    paint2()
    fun2(0.3 + 0.7)
    fun2(0.5 + 0)
    fun2(0.9 + -0.7)