import numpy as np
from numpy import sin, cos, pi
import time
import matplotlib.pyplot

L1 = 2
L2 = 1
m1 = 2
m2 = 1
g = 9.8

theta1 = 0
theta2 = 2
omega1 = 0
omega2 = 0
alpha1 = 0
alpha2 = 0

dt = 0.05
t = 0

Time = []
Theta1 = []
Theta2 = []
Omega1 = []
Omega2 = []

x1 = []
y1 = []
x2 = []
y2 = []

def a1():
    num1 = -g*(2*m1 + m2)*sin(theta1)
    num2 = -m2*g*sin(theta1 - 2*theta2)
    num3 = -2*sin(theta1 - theta2)*m2*(omega2**2*L2+omega1**2*L1*cos(theta1 - theta2))
    den = L1*(2*m1 + m2 - m2*cos(2*theta1 - 2*theta2))
    return (num1 + num2 + num3)/den

    return
def a2():
    num1 = 2*sin(theta1 - theta2)
    num2 = omega1**2*L1*(m1 + m2)
    num3 = g*(m1 + m2)*cos(theta1)
    num4 = omega2**2*L2*m2*cos(theta1 - theta2)
    den = L2*(2*m1 + m2 - m2*cos(2*theta1 - 2* theta2))
    return num1*(num2 + num3 + num4)/den

i = 1

while t < 40:
    alpha1 = a1()
    alpha2 = a2()
    omega1 += alpha1*dt
    omega2 += alpha2*dt
    theta1 += omega1*dt
    theta2 += omega2*dt

    t += dt

    Time.append(t)
    Theta1.append(theta1)
    Theta2.append(theta2)
    x1.append(L1*sin(theta1))
    y1.append(-L1*cos(theta1))
    x2.append(L1)
    y2.append

fig, value = matplotlib.pyplot.subplots()
value.plot(Time, Theta1, Time, Theta2)
#value.axvline(S)
matplotlib.pyplot.show()