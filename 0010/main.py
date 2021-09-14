import matplotlib.pyplot as plt
import math

#unit_step_function(x) = {1 for x >= 0, 0 for x < 0}
def unit_step_function(x): 
    if(x >= 0):
        return 1
    else:
        return 0

#shifted_unit_step_function(x, k) = {1 for x >= k, 0 for x < k}
#k = the amount shifted by which unit_step_function(x, k) is shifted to the right
def shifted_unit_step_function(x, k):
    if(x >= k):
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

plt.subplot(3, 1, 1) #plt.subplot(number of rows of plots, number of columns of plots, plot number)
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
    y = math.cos(x) * unit_step_function(x)
    y_data_2.append(y)
    x += dx

plt.figure(1)

plt.subplot(3, 1, 2) #plt.subplot(number of rows of plots, number of columns of plots, plot number)
plt.scatter(x_data_2, y_data_2, color = "blue", label = "f(x) = cos(x) * unit_step_function(x)")
plt.legend(loc = "upper left")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

#----------------------------------------------------------------------------------

x_data_3 = []
y_data_3 = []

x_min = -2*math.pi
x_max = 2*math.pi
num_points = 100
dx = (x_max - x_min)/num_points

x = x_min
while(x <= x_max):
    x_data_3.append(x)
    y = math.cos(x) * shifted_unit_step_function(x, math.pi/2)
    y_data_3.append(y)
    x += dx

plt.figure(1)

plt.subplot(3, 1, 3) #plt.subplot(number of rows of plots, number of columns of plots, plot number)
plt.scatter(x_data_3, y_data_3, color = "blue", label = "f(x) = cos(x) * shifted_unit_step_function(x, k)")
plt.legend(loc = "upper left")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

#----------------------------------------------------------------------------------

plt.show()
