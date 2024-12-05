import numpy as np
import matplotlib.pyplot as plt


# Sistemas FIR 1 y 2
def sistema1(x):
    n = len(x)
    y = np.zeros(n)

    for i in range(n):
        y[i] += 0.5 * x[i]
        if i - 1 >= 0:
            y[i] += 0.5 * x[i - 1]

    return y


def sistema2(x):
    n = len(x)
    y = np.zeros(n)

    for i in range(n):
        y[i] += 0.5 * x[i]
        if i - 1 >= 0:
            y[i] -= 0.5 * x[i - 1]

    return y


# Sistemas IIR 1 y 2
def sistema3(x):
    n = len(x)
    y = np.zeros(n)

    for i in range(n):
        y[i] += 0.25 * x[i]
        if i - 1 >= 0:
            y[i] += 0.25 * x[i - 1] + 0.5 * y[i - 1]

    return y


def sistema4(x):
    n = len(x)
    y = np.zeros(n)

    for i in range(n):
        y[i] += 0.25 * x[i]
        if i - 1 >= 0:
            y[i] += -0.25 * x[i - 1] - 0.5 * y[i - 1]

    return y
