import numpy as np
from numpy import sin, cos, pi 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
import matplotlib.animation as animation

# Constants 

g = 9.81

# Givens 

m1 = 1
m2 = 1

l1 = 1
l2 = 1

theta10 = -pi/6
theta20 = pi/2

omega10 = 0
omega20 = 0

alpha1 = 0
alpha2 = 0


def a1(theta1,theta2,omega1,omega2):
    num = -g*(2*m1 + m2)*sin(theta1)-m2*g*sin(theta1 - 2*theta2) - 2*sin(theta1 - theta2)*m2*(omega2**2*l2+omega1**2*l1*cos(theta1 - theta2))
    den = l1*(2*m1 + m2-m2*cos(2*theta1 - 2*theta2))
    alpha1 = num/den
    return alpha1 

def a2(theta1,theta2,omega1,omega2):
    num = 2*sin(theta1-theta2)*((omega1**2*l1*(m1+m2))+g*(m1+m2)*cos(theta1)+omega2**2*l2*m2*cos(theta1-theta2))
    den = l2*(2*m1 + m2-m2*cos(2*theta1 - 2*theta2))
    alpha2 = num/den
    return alpha2 

test1 = a1(1,1,1,1)
test2 = a2(1,1,1,1)

t = 0
tf = 5
dt = 0.01


theta1 = theta10
theta2 = theta20

omega1 = omega10
omega2 = omega20

t_List = []
theta1_List = []
omega1_list = []
theta2_List = []
omega2_list = []

while t < tf:
     alpha1 = a1(theta1,theta2,omega1,omega2)
     alpha2 = a2(theta1,theta2,omega1,omega2)

     omega1 += alpha1*dt
     omega2 += alpha2*dt

     theta1 += omega1*dt
     theta2 += omega2*dt

     print("Theta1: ", theta1, "  -  Theta2: ", theta2)
     t += dt
     t_List.append(t)
     theta1_List.append(theta1) 
     omega1_list.append(omega1)
     theta2_List.append(theta2)
     omega2_list.append(omega2)


# Calculate the x and y locations

x1 = l1*sin(theta1_List)
y1 = -l1*cos(theta1_List)

x2 = l2*sin(theta2_List) + x1
y2 = -l2*cos(theta2_List) + y1

history_len = 1000  # how many trajectory points to display

fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(autoscale_on=False, xlim=(-(l1+l2), (l1+l2)), ylim=(-(l1+l2), (l1+l2)))
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
trace, = ax.plot([], [], '.-', lw=2, ms=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
history_x, history_y = deque(maxlen=history_len), deque(maxlen=history_len)


def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    if i == 0:
        history_x.clear()
        history_y.clear()

    history_x.appendleft(thisx[2])
    history_y.appendleft(thisy[2])

    line.set_data(thisx, thisy)
    trace.set_data(history_x, history_y)  
    time_text.set_text(time_template % (i*dt))
    fig.suptitle('Double Pendulum - Euler\'s Method', fontsize=12)
    return line, trace, time_text

ani = animation.FuncAnimation(fig, animate, len(t_List), interval=0.1)
plt.show()

# Uncomment to save a gif 

ani.save('myAnimation.gif', writer='imagemagick', fps=30) #

# Theta vs t plot

# fig, value = matplotlib.pyplot.subplots()
# value.plot(t_List, theta1_List, t_List, theta2_List)
# #value.axvline(S)
# matplotlib.p
# yplot.show()

# Phase PLan plot

# fig, value = matplotlib.pyplot.subplots()
# value.plot(theta1_List, omega1_list,theta2_List, omega2_list,)
# matplotlib.pyplot.show()
