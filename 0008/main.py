import matplotlib.pyplot as plt
import math

#t = n * sampling_interval
#f(t) = f(n * sampling_interval) = f[n]
def discretize_function(function, t_min, t_max, sampling_interval):
    n_data = [] #sampling independent values on the horizontal axis
    y_data_sample = [] #sampling dependent values on the vertical axis
    n_min = t_min/sampling_interval
    n_max = t_max/sampling_interval
    n = n_min
    while(n <= n_max):
        n_data.append(n)
        y_data_sample.append(function(n * sampling_interval))
        n += 1
    return n_data, y_data_sample

t_data = []
y_data = []

t_min = -2*math.pi
t_max = 2*math.pi
num_points = 100
dt = (t_max - t_min)/num_points

t = t_min
while(t <= t_max):
    t_data.append(t)
    y_data.append(math.sin(t))
    t += dt

plt.figure(1)

plt.subplot(3, 1, 1) #plt.subplot(number of rows of plots, number of columns of plots, plot number)
plt.plot(t_data, y_data, color = "midnightblue", label = "f(t) = sin(t)")
plt.legend(loc = "upper left")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.grid()

#----------------------------------------------------------------------------------

sampling_interval = 0.25
t_min = -2*math.pi
t_max = 2*math.pi
n_data, y_data_sample = discretize_function(math.sin, t_min, t_max, sampling_interval) #(n_data[i], y_data_sample[i]) = i th sampling point

plt.subplot(3, 1, 2) #plt.subplot(number of rows of plots, number of columns of plots, plot number)
plt.scatter(n_data, y_data_sample, color = "green", label = "f(n * sampling_interval) = sin(n * sampling_interval) , sampling_interval = " + str(sampling_interval))
plt.legend(loc = "upper left")
plt.xlabel("n")
plt.ylabel("f(n * sampling_interval)")
plt.grid()

#----------------------------------------------------------------------------------

t_data = []
y_data = []

t_min = -2*math.pi
t_max = 2*math.pi
num_points = 100
dt = (t_max - t_min)/num_points

t = t_min
while(t <= t_max):
    t_data.append(t)
    y_data.append(math.cos(t))
    t += dt

plt.figure(2)

plt.subplot(3, 1, 1) #plt.subplot(number of rows of plots, number of columns of plots, plot number)
plt.plot(t_data, y_data, color = "midnightblue", label = "f(t) = cos(t)")
plt.legend(loc = "upper left")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.grid()

#----------------------------------------------------------------------------------

sampling_interval = 0.25
t_min = -2*math.pi
t_max = 2*math.pi
n_data, y_data_sample = discretize_function(math.cos, t_min, t_max, sampling_interval) #(n_data[i], y_data_sample[i]) = i th sampling point

plt.subplot(3, 1, 2) #plt.subplot(number of rows of plots, number of columns of plots, plot number)
plt.scatter(n_data, y_data_sample, color = "green", label = "f(n * sampling_interval) = cos(n * sampling_interval) , sampling_interval = " + str(sampling_interval))
plt.legend(loc = "upper left")
plt.xlabel("n")
plt.ylabel("f(n * sampling_interval)")
plt.grid()

#----------------------------------------------------------------------------------

plt.show()
