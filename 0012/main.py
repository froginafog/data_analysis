#discrete complex exponential

import matplotlib.pyplot as plt
from math import sin, cos, pi

#----------------------------------------------------------------------------------

#r * e^(j * x) = r * cos(x) + j * r * sin(x)
#x = 2 * pi * k / N
#r = radius of the circle in the complex plane = amplitude of the circle in the complex plane 
#N = number of intervals = number of sub arcs forming the circle in the complex plane 
#k = kth sub arc
#returns 2 arrays
#first array: real_part_data
#second array: imaginary_part_data
def discretize_complex_exponential_function(N, r):
    real_part_data = []
    imaginary_part_data = []
    for k in range(0, num_intervals):
        real_part_data.append(r * cos(2 * pi * k / num_intervals))
        imaginary_part_data.append(r * sin(2 * pi * k / num_intervals))
    return real_part_data, imaginary_part_data

#----------------------------------------------------------------------------------

x_data_circle = []
y_data_circle = []
radius = 5
angle = 0
angle_max = 2 * pi
while(angle <= angle_max):
    x_data_circle.append(radius * cos(angle))
    y_data_circle.append(radius * sin(angle))
    angle = angle + 0.001

plt.figure(1)
plt.plot(x_data_circle, y_data_circle, color = "steelblue", label = "circle")
plt.grid()

#----------------------------------------------------------------------------------

num_intervals = 8
real_part_data, imaginary_part_data = discretize_complex_exponential_function(num_intervals, radius)

plt.figure(1)
plt.scatter(real_part_data, imaginary_part_data, color = "red", label = str(num_intervals) + " discrete points of the complex exponential function")
plt.legend(loc = "upper left")
plt.xlabel("real axis")
plt.ylabel("imaginary axis")
plt.title("complex plane")
plt.grid()

#----------------------------------------------------------------------------------

plt.show()
