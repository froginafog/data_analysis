import matplotlib.pyplot as plt
import math

#impulse_function(x, tol) = {1 for x = 0, 0 for x != 0}
def impulse_function(x, tol): #tol = tolerance
    if(x >= 0 - tol and x <= 0 + tol):
        return 1
    else:
        return 0

x_data_1 = []
y_data_1 = []

x_min = -2*math.pi
x_max = 2*math.pi
num_points = 100
dx = (x_max - x_min)/num_points

x = x_min
while(x <= x_max):
    x_data_1.append(x)
    y = math.cos(x)
    y_data_1.append(y)
    x += dx

plt.figure(1)

plt.subplot(2, 1, 1) #plt.subplot(number of rows of plots, number of columns of plots, plot number)
plt.scatter(x_data_1, y_data_1, color = "blue", label = "f(x) = cos(x)")
plt.legend(loc = "lower left")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

#----------------------------------------------------------------------------------

x_data_2 = []
y_data_2 = []

x_min = -2*math.pi
x_max = 2*math.pi
num_points = 100
dx = (x_max - x_min)/num_points

x = x_min
while(x <= x_max):
    x_data_2.append(x)
    y = math.cos(x) * impulse_function(x, 0.01)
    y_data_2.append(y)
    x += dx

plt.figure(1)

plt.subplot(2, 1, 2) #plt.subplot(number of rows of plots, number of columns of plots, plot number)
plt.scatter(x_data_2, y_data_2, color = "blue", label = "f(x) = cos(x) * impulse_function(x, tol)")
plt.legend(loc = "upper left")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

#----------------------------------------------------------------------------------

plt.show()
