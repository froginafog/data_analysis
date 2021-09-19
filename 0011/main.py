#discrete convolution

import matplotlib.pyplot as plt

#unit_step_function(x) = {1 for x >= 0, 0 for x < 0}
def unit_step_function(x): 
    if(x >= 0):
        return 1
    else:
        return 0

#f_1 and f_2 are functions
def discrete_convolution(f_1, f_2, n, lower_limit, upper_limit):
    total = 0
    k = lower_limit
    while(k <= upper_limit):
        total = total + f_1(k) * f_2(n - k)
        k += 1
    return total

def f_1(n):
    return unit_step_function(n)

def f_2(n):
    x = 0.5
    return x**n * unit_step_function(n)

#----------------------------------------------------------------------------------

x_data_1 = []
y_data_1 = []

n_min = -5
n_max = 5
n = n_min
while(n <= n_max):
    x_data_1.append(n)
    y_data_1.append(f_1(n))
    n += 1

plt.figure(1)
plt.subplot(3, 1, 1) #plt.subplot(number of rows of plots, number of columns of plots, plot number)
plt.scatter(x_data_1, y_data_1, color = "red", label = "f_1")
plt.legend(loc = "upper left")
plt.xlabel("x_data_1")
plt.ylabel("y_data_1")
plt.grid()

#----------------------------------------------------------------------------------

x_data_2 = []
y_data_2 = []

n_min = -5
n_max = 5
n = n_min
k = 0
while(n <= n_max):
    x_data_2.append(n)
    y_data_2.append(f_2(n - k))
    n += 1

plt.figure(1)
plt.subplot(3, 1, 2) #plt.subplot(number of rows of plots, number of columns of plots, plot number)
plt.scatter(x_data_2, y_data_2, color = "green", label = "f_2")
plt.legend(loc = "upper left")
plt.xlabel("x_data_2")
plt.ylabel("y_data_2")
plt.grid()

#----------------------------------------------------------------------------------

x_data_3 = []
y_data_3 = []

n_min = -5
n_max = 5
n = n_min
while(n <= n_max):
    x_data_3.append(n)
    y_data_3.append(discrete_convolution(f_1, f_2, n, n_min, n_max))
    n += 1

plt.figure(1)
plt.subplot(3, 1, 3) #plt.subplot(number of rows of plots, number of columns of plots, plot number)
plt.scatter(x_data_3, y_data_3, color = "blue", label = "convolution of f_1 and f_2")
plt.legend(loc = "upper left")
plt.xlabel("x_data_3")
plt.ylabel("y_data_3")
plt.grid()


#----------------------------------------------------------------------------------

plt.show()
