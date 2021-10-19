import math
import cmath
import matplotlib.pyplot as plt

def X(k, T, T1, w0):
    if(k == 0):
        return 2*T1/T
    return 2 * math.sin(k * w0 * T1) / (k * w0 * T)

def x(t, w0):
    sum = 0j
    k = -100000
    while k <= 100000:
        sum = X(k, 4, 1, w0) * cmath.exp(1j * k  * w0 * t)
        k += 1
    return sum


xVals = []
yVals = []
i = -10
while i <= 10:
    xVals.append(i)
    yVals.append(x(i, 2*math.pi/4))
    print(i, yVals[i + 10])
    i += 1