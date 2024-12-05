import numpy as np


def tftd(x, n):
    ds = 0.001
    s = np.arange(-1, 1 + ds, ds)  # Frecuencias en el rango [-2, 2] con paso ds
    N = len(s)  # Número de muestras de la TFTD

    # Inicialización de la TFTD
    X = np.zeros(N, dtype=complex)

    # Cálculo de la transformada
    for k in range(N):
        X[k] = np.sum(x * np.exp(-1j * 2 * np.pi * s[k] * n))

    return X, s
