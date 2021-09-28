import matplotlib.pyplot as plt
from math import sin, pi

#----------------------------------------------------------------------------------

#e^(j * x) = cos(x) + j * sin(x)
#real_part = cos(x)
#imaginary_part = sin(x)
def complex_exponential_function(angle):
    real_part = cos(angle)
    imaginary_part = sin(angle)
    return real_part, imaginary_part

#----------------------------------------------------------------------------------
#plot sin(b * x) * e^(j * x) on the complex plane

real_part_data_1 = []
imaginary_part_data_1 = []
angle_min = 0
angle_max = 2 * pi
angle = angle_min
dangle = 0.001
b = 1 #scale the angle
while(angle <= angle_max):
    amplitude = sin(b * angle) 
    real_part, imaginary_part = complex_exponential_function(angle)
    real_part = amplitude * real_part
    imaginary_part = amplitude * imaginary_part
    real_part_data_1.append(real_part)
    imaginary_part_data_1.append(imaginary_part)
    angle += dangle

plt.figure(1)
plt.subplot(3, 1, 1)
plt.plot(real_part_data_1, imaginary_part_data_1, color = "red", label = "sin(" + str(b) + " * x) * e^(j * x)")
plt.legend(loc = "upper left")
plt.xlabel("real axis")
plt.ylabel("imaginary axis")
plt.title("complex plane")
plt.grid()

#----------------------------------------------------------------------------------
#plot sin(b * x) * e^(j * x) on the complex plane

real_part_data_2 = []
imaginary_part_data_2 = []
angle_min = 0
angle_max = 2 * pi
angle = angle_min
dangle = 0.001
b = 2 #scale the angle
while(angle <= angle_max):
    amplitude = sin(b * angle) 
    real_part, imaginary_part = complex_exponential_function(angle)
    real_part = amplitude * real_part
    imaginary_part = amplitude * imaginary_part
    real_part_data_2.append(real_part)
    imaginary_part_data_2.append(imaginary_part)
    angle += dangle

plt.figure(1)
plt.subplot(3, 1, 2)
plt.plot(real_part_data_2, imaginary_part_data_2, color = "green", label = "sin(" + str(b) + " * x) * e^(j * x)")
plt.legend(loc = "upper left")
plt.xlabel("real axis")
plt.ylabel("imaginary axis")
plt.title("")
plt.grid()

#----------------------------------------------------------------------------------
#plot sin(b * x) * e^(j * x) on the complex plane

real_part_data_3 = []
imaginary_part_data_3 = []
angle_min = 0
angle_max = 2 * pi
angle = angle_min
dangle = 0.001
b = 3 #scale the angle
while(angle <= angle_max):
    amplitude = sin(b * angle) 
    real_part, imaginary_part = complex_exponential_function(angle)
    real_part = amplitude * real_part
    imaginary_part = amplitude * imaginary_part
    real_part_data_3.append(real_part)
    imaginary_part_data_3.append(imaginary_part)
    angle += dangle

plt.figure(1)
plt.subplot(3, 1, 3)
plt.plot(real_part_data_3, imaginary_part_data_3, color = "blue", label = "sin(" + str(b) + " * x) * e^(j * x)")
plt.legend(loc = "upper left")
plt.xlabel("real axis")
plt.ylabel("imaginary axis")
plt.title("")
plt.grid()

#----------------------------------------------------------------------------------

plt.show()
