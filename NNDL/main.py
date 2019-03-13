import numpy as np

sample = np.array([1,2,3,4])

print(sample)

del sample

import time

timeExp1 = np.random.rand(1000000)
timeExp2 = np.random.rand(1000000)

# print(timeExp1)

# Vectorized

tic = time.time()
sumV = np.dot(timeExp1, timeExp2)
toc = time.time()

print("Vectorized Version:" + str(1000*(toc - tic))+'ms')

# Non-Vectorized

sumNV = 0

tic = time.time()
for index in range(len(timeExp1)):
    sumNV += timeExp1[index]*timeExp2[index]
toc = time.time()
print("Non-Vectorized Version:" + str(1000*(toc - tic))+'ms')


# Broadcasting in Python
import numpy as np

nutri = np.array([[56, 0, 4.4, 68],
                 [1.2, 104, 52, 8],
                 [1.8, 135, 99, .9]])

print(nutri)

cal = nutri.sum(axis=0)

print(cal)
percentage = 100*nutri/cal.reshape(1,4)
print(percentage)


# A note
import numpy as np
a = np.random.randn(5)
print(a)

# a.reshape(5,1)
print(a.T.shape)

print(np.dot(a,a.T))

a = np.random.randn(5,1)
print(a)

a.shape

print(a.T)
a.T.shape

print(np.dot(a, a.T))
print(np.dot(a.T, a))
