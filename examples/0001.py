#author: froginafog (Liang D.S.)
import matplotlib.pyplot as plt

def matrix_transpose(A):
    num_rows = len(A)
    num_columns = len(A[0])
    a = [] 
    for j in range(0, num_columns):
        for i in range(0, num_rows):
            a.append(A[i][j])
    temp = num_rows
    num_rows = num_columns
    num_columns = temp
    AT = [] #transpose of A
    k = 0
    for i in range(0, num_rows):
        row = []
        for j in range(0, num_columns):
            row.append(a[k])
            k = k + 1
        AT.append(row)
    return AT

def table_to_string(column_names, table, starting_row, ending_row, starting_column, ending_column):
    ending_row -= 1
    ending_column -= 1
    max_column_lengths = [0] * len(column_names)
    for j in range(starting_column, ending_column + 1):
        max_column_lengths[j] = len(column_names[j])
    for i in range(starting_row, ending_row + 1):
        for j in range(starting_column, ending_column + 1):
            table[i][j] = str(table[i][j])
            if(len(table[i][j]) > max_column_lengths[j]):
                max_column_lengths[j] = len(table[i][j])
    num_dashes = 0
    for n in range(starting_column, ending_column + 1):
        num_dashes = num_dashes + max_column_lengths[n] + 3
    num_dashes = num_dashes + 1
    dashes = ""
    for n in range(0, num_dashes):
        dashes = dashes + '-'
    output = dashes + "\n|" 
    for j in range(starting_column, ending_column + 1):
        s = " %" + str(max_column_lengths[j]) + "s "
        s = s % column_names[j]
        output = output + s + "|"
    output = output + "\n" + dashes + "\n"
    for i in range(starting_row, ending_row + 1):
        output = output + dashes + "\n|"
        for j in range(starting_column, ending_column + 1):
            s = " %" + str(max_column_lengths[j]) + "s "
            s = s % table[i][j]
            output = output + s + "|"
        output = output + "\n"
    output = output + dashes + "\n"
    return output    

def calculate_mean(data):
    total = 0
    for n in data:
        total = total + n
    return total/len(data)

def calculate_mean(data):
    total = 0
    for n in data:
        total = total + n
    return total/len(data)

def calculate_slope_of_regression_line(x_data, y_data):
    mean_x_data = calculate_mean(x_data)
    mean_y_data = calculate_mean(y_data)
    x_data_size = len(x_data)
    y_data_size = len(y_data)
    if(x_data_size != y_data_size):
        print("The size of x_data and the size of y_data do not match.")
        return None
    num_points = x_data_size
    numerator_total = 0
    denominator_total = 0
    for i in range(0, num_points):
        numerator_total = numerator_total + (x_data[i] - mean_x_data) * (y_data[i] - mean_y_data)
        denominator_total = denominator_total + (x_data[i] - mean_x_data)**2
    return numerator_total / denominator_total #slope of the regression line

#y_predicted = b_0 + b_1*x
def calculate_predicted_y(x, b_0, b_1):
    return b_0 + b_1*x

#sum of squares regression
def calculate_SSR(y_data, y_data_predicted):
    y_data_size = len(y_data)
    y_data_predicted_size = len(y_data_predicted)
    if(y_data_size != y_data_predicted_size):
        print("The size of y_data and the size of y_data_predicted do not match.")
    data_mean = calculate_mean(y_data)
    SSR = 0
    for i in range(0, y_data_size):
        SSR = SSR + (y_data_predicted[i] - data_mean)**2
    return SSR

#sum of squares error
def calculate_SSE(y_data, y_data_predicted):
    y_data_size = len(y_data)
    y_data_predicted_size = len(y_data_predicted)
    if(y_data_size != y_data_predicted_size):
        print("The size of y_data and the size of y_data_predicted do not match.")
        return None
    SSE = 0
    for i in range(y_data_size):
        SSE = SSE + (y_data[i] - y_data_predicted[i])**2
    return SSE

#sum of squares total
def calculate_SST(y_data):
    y_data_mean = calculate_mean(y_data)
    SST = 0
    for n in y_data:
        SST = SST + (n - y_data_mean)**2
    return SST

#correlation coefficient R for y_data and y_data_predicted
#-1 <= R <= 1
#If R = 1, then there is a perfect positive linear relationship.
#If R = -1, then there is a perfect negative linear relationship.
#If R = 0, then there is a no relationship.
def calculate_correlation_coefficient(y_data, y_data_predicted):
    SSR = calculate_SSR(y_data, y_data_predicted)
    SST = calculate_SST(y_data)
    R = (SSR/SST)**(1/2)
    return R

#Consider 20 students. The number of hours they study per day:
num_hours_studies = [5, 6, 3, 3, 2, 4, 7, 5, 2, 3, 5, 6, 5, 4, 4, 3, 5, 2, 5, 3]   #numbers of hours of studies per day
num_hours_studies.sort() #sort num_hours_studies in increasing order

print("num_hours_studies:", num_hours_studies)

previous_num_hours = num_hours_studies[0]

unique_num_hours_studies = [] #the unique numbers of hours of studies

unique_num_hours_studies.append(num_hours_studies[0])

for num_hours in num_hours_studies:
    if(num_hours != previous_num_hours):
         unique_num_hours_studies.append(num_hours)
    previous_num_hours = num_hours

print("unique_num_hours_studies:", unique_num_hours_studies)

unique_num_hours_studies_size = len(unique_num_hours_studies)

frequencies_num_hours_studies = []

for i in range(0, unique_num_hours_studies_size):
    frequencies_num_hours_studies.append(0)

for num_hours in num_hours_studies:
    for i in range(0, unique_num_hours_studies_size):
        if(num_hours == unique_num_hours_studies[i]):
             frequencies_num_hours_studies[i] += 1    

print("frequencies_num_hours_studies:", frequencies_num_hours_studies)

num_hours_studies_size = len(num_hours_studies)

relative_frequencies_num_hours_studies = []

for frequency in frequencies_num_hours_studies:
    relative_frequency = frequency/num_hours_studies_size
    relative_frequencies_num_hours_studies.append(relative_frequency)

print("relative_frequencies_num_hours_studies:", relative_frequencies_num_hours_studies)

cummulative_relative_frequencies_num_hours_studies = []

total = 0
for relative_frequency in relative_frequencies_num_hours_studies:
    total += relative_frequency
    total = round(total, 3) #round to 3 digits
    cummulative_relative_frequencies_num_hours_studies.append(total)

print("cummulative_relative_frequencies_num_hours_studies:", cummulative_relative_frequencies_num_hours_studies)

#--------------------------------------------------------------------

column_names = ["hours of studies", "frequency", "relative frequency", "cummulative frequency"]
table = []
table.append(unique_num_hours_studies)
table.append(frequencies_num_hours_studies)
table.append(relative_frequencies_num_hours_studies)
table.append(cummulative_relative_frequencies_num_hours_studies)

table = matrix_transpose(table)
table_string = table_to_string(column_names, table, 0, unique_num_hours_studies_size, 0, len(column_names))
print(table_string)
  
#--------------------------------------------------------------------

b_1 = calculate_slope_of_regression_line(unique_num_hours_studies, frequencies_num_hours_studies)    #slope of regression line
b_0 = calculate_mean(frequencies_num_hours_studies) - b_1 * calculate_mean(unique_num_hours_studies) #intercept of regression line

frequencies_num_hours_studies_predicted = []
for n in unique_num_hours_studies:
    frequencies_num_hours_studies_predicted.append(calculate_predicted_y(n, b_0, b_1))

R = calculate_correlation_coefficient(frequencies_num_hours_studies, frequencies_num_hours_studies_predicted) #correlation coefficient
print("correlation coefficient R:", R)

x_min = unique_num_hours_studies[0]
x_max = unique_num_hours_studies[len(unique_num_hours_studies) - 1]
x_data_regression_line = []
y_data_regression_line = []
x = x_min
while(x <= x_max):
    x_data_regression_line.append(x)
    y_data_regression_line.append(calculate_predicted_y(x, b_0, b_1))
    x = x + 0.05

plt.scatter(unique_num_hours_studies, frequencies_num_hours_studies)
plt.plot(x_data_regression_line , y_data_regression_line)
plt.xlabel("number of hours of studies")
plt.ylabel("number of students")
plt.show()

#--------------------------------------------------------------------

