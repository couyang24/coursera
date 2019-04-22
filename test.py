import numpy as np


np.random.seed(1)
A_prev = np.random.randn(10,4,4,3)
W = np.random.randn(2,2,3,8)
b = np.random.randn(1,1,1,8)
hparameters = {"pad" : 2,
               "stride": 2}

(m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape

(f, f, n_C_prev, n_C) = W.shape

stride = hparameters['stride']
pad = hparameters['pad']

n_H = int((n_H_prev + 2 * pad - f) / stride) + 1
n_W = int((n_W_prev + 2 * pad - f) / stride) + 1

Z = np.zeros((m, n_H, n_W, n_C))

Z.shape

for x in range(2,4):
    y=2
    while y<4:
        print(x**y)
        y+=1