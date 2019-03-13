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
