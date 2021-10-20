import math
import cmath
import matplotlib.pyplot as plt

def X(k, T, T1):
    if(k == 0):
        return 2*T1/T
    return 2 * math.sin(k * 2*math.pi/T * T1) / (k * 2*math.pi/T * T)

def x(t, T, T1):
    sum = 0j
    k = -1000
    while k <= 1000:
        sum = X(k, T, T1) * cmath.exp(1j * k  * 2*math.pi/T * t)
        k += 1
    return sum

xVals = []
yVals = []
t = -10
while t <= 10:
    xVals.append(t)
    yVals.append(x(t, 10, 2))
    print(t, "\t", yVals[t + 10])
    t += 1