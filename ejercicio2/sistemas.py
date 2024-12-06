import numpy as np

def sistema(x):
    n = len(x)
    y = np.zeros(n)

    for i in range(n):
        y[i] += x[i]
        if i - 8820 >= 0:
            y[i] += (2/5) * x[i - 8820]
        if i - 17640 >= 0:
            y[i] += (4/25) * x[i - 17640]

    return y

def filtro1(x):
    n = len(x)
    y = np.zeros(n)

    for i in range(n):
        y[i] += x[i]
        if i - 8820 >= 0:
            y[i] -= (2/5) * x[i - 8820]

    return y


def filtro2(x):
    n = len(x)
    y = np.zeros(n)

    for i in range(n):
        y[i] += x[i]
        if i - 8820 >= 0:
            y[i] -= (2/5) * x[i - 8820]
        if i - 17640 >= 0:
            y[i] -= (4/25) * x[i - 17640]

    return y