import matplotlib.pyplot as plt

def f(t):
    return 1 - abs(t)

t_data = []
y_data = []

t_min = -1
t_max = 1
num_points = 100
dt = (t_max - t_min)/num_points

t = t_min
while(t <= t_max):
    t_data.append(t)
    t += dt
    
num_points = len(t_data)
for i in range(0, num_points):
    y_data.append(f(t_data[i]))

plt.figure(1)
plt.plot(t_data, y_data, color = "midnightblue", label = "f(t) = 1 - |t|")
plt.legend(loc = "upper left")
#plt.xticks(t_data)
plt.xlabel("t")
plt.ylabel("y")
plt.grid()

#----------------------------------------------------------------------------------

x_tick = []
for x in range(-4, 5):
    x_tick.append(x)

#----------------------------------------------------------------------------------

T_sample = 0.25 #sampling interval
n_data = [] #sampling points
n_min = t_min/T_sample
n_max = t_max/T_sample
n = n_min
while(n <= n_max):
    n_data.append(n)
    n += 1

y_data_sample = []
for n in n_data:
    y_data_sample.append(f(n*T_sample))

plt.figure(2)
plt.scatter(n_data, y_data_sample, color = "blue", label = "f(n*T_sample) = 1 - |n*T_sample| , T_sample = " + str(T_sample))
plt.legend(loc = "upper left")
plt.xticks(x_tick)
plt.xlabel("n")
plt.ylabel("f(n*T_sample)")
plt.grid()

#----------------------------------------------------------------------------------

T_sample = 0.5 #sampling interval
n_data = [] #sampling points
n_min = t_min/T_sample
n_max = t_max/T_sample
n = n_min
while(n <= n_max):
    n_data.append(n)
    n += 1

y_data_sample = []
for n in n_data:
    y_data_sample.append(f(n*T_sample))

plt.figure(2)
plt.scatter(n_data, y_data_sample, color = "green", label = "f(n*T_sample) = 1 - |n*T_sample| , T_sample = " + str(T_sample))
plt.legend(loc = "upper left")
plt.xticks(x_tick)
plt.xlabel("n")
plt.ylabel("f(n*T_sample)")
plt.grid()

#----------------------------------------------------------------------------------

T_sample = 1 #sampling interval
n_data = [] #sampling points
n_min = t_min/T_sample
n_max = t_max/T_sample
n = n_min
while(n <= n_max):
    n_data.append(n)
    n += 1

y_data_sample = []
for n in n_data:
    y_data_sample.append(f(n*T_sample))

plt.figure(2)
plt.scatter(n_data, y_data_sample, color = "red", label = "f(n*T_sample) = 1 - |n*T_sample| , T_sample = " + str(T_sample))
plt.legend(loc = "upper left")
plt.xticks(x_tick)
plt.xlabel("n")
plt.ylabel("f(n*T_sample)")
plt.grid()

#----------------------------------------------------------------------------------

plt.show()
