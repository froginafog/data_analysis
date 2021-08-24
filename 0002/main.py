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

def table_to_string(names_of_columns, table, starting_row, ending_row, starting_column, ending_column):
    max_column_lengths = [0] * len(column_names)
    for j in range(starting_column, ending_column):
        max_column_lengths[j] = len(column_names[j])
    for i in range(starting_row, ending_row):
        for j in range(starting_column, ending_column):
            table[i][j] = str(table[i][j])
            if(len(table[i][j]) > max_column_lengths[j]):
                max_column_lengths[j] = len(table[i][j])
    num_dashes = 0
    for n in range(starting_column, ending_column):
        num_dashes = num_dashes + max_column_lengths[n] + 3
    num_dashes = num_dashes + 1
    dashes = ""
    for n in range(0, num_dashes):
        dashes = dashes + '-'
    output = dashes + "\n|" 
    for j in range(starting_column, ending_column):
        s = " %" + str(max_column_lengths[j]) + "s "
        s = s % column_names[j]
        output = output + s + "|"
    output = output + "\n" + dashes + "\n"
    for i in range(starting_row, ending_row):
        output = output + dashes + "\n|"
        for j in range(starting_column, ending_column):
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

def calculate_median(a):
    num_elements = len(a)
    a.sort()
    if(num_elements % 2 == 0):  #num_elements is even
        return (a[int(num_elements/2) - 1] + a[int(num_elements/2)])/2
    else:  #num_elements is odd
        return a[int((num_elements + 1)/2) - 1]

def calculate_mode(a):
    a.sort()
    current_frequency = 0
    highest_frequency = 0
    index_highest_frequency = 0
    previous_number = a[0]
    i = 0
    for current_number in a:
        if(current_number == previous_number):
            current_frequency = current_frequency + 1
        else:
            current_frequency = 0
        if(current_frequency > highest_frequency):
            highest_frequency = current_frequency
            index_highest_frequency = i
        previous_number = current_number 
        i = i + 1
    return a[index_highest_frequency]

def calculate_standard_deviation(a):
    N = len(a)  #size of the sample
    total = 0
    for n in a:
        total = total + n
    mean = total/N
    total = 0
    for n in a:
        total = total + (n - mean)**2
    sample_standard_deviation = (total/(N-1))**(1/2)
    return sample_standard_deviation

def label_bars(plt, x_data, y_data): #label each bar with its y-value
    num_items = len(x_data)
    for i in range(0, num_items):
        plt.text(x_data[i], y_data[i], str(y_data[i]), ha = "center")

heights = [60, 60.5, 61, 61, 61.5, 63.5, 63.5, 63.5, 64, 64, 64, 64, 64, 64, 64, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5,
           66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66.5, 66.5, 66.5, 66.5, 66.5, 66.5, 66.5, 66.5, 66.5, 66.5, 66.5,
           67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67.5, 67.5, 67.5, 67.5, 67.5, 67.5, 67.5, 68, 68, 69, 69, 69, 69, 69,
           69, 69, 69, 69, 69, 69.5, 69.5, 69.5, 69.5, 69.5, 70, 70, 70, 70, 70, 70, 70.5, 70.5, 70.5, 71, 71, 71, 72, 72, 72, 72.5, 72.5, 73, 73.5, 74]
num_of_heights = len(heights)

mean_of_heights = calculate_mean(heights)
print("mean_of_heights:", mean_of_heights)
heights.sort()
median_of_heights = calculate_median(heights)
print("median_of_heights:", median_of_heights)
mode_of_heights = calculate_mode(heights)
print("mode_of_heights:", mode_of_heights)
standard_deviation_of_heights = calculate_standard_deviation(heights)
print("standard_deviation_of_heights:", standard_deviation_of_heights)
print()

#intervals:
#59.95-61.95 
#61.95-63.95 
#63.95-65.95 
#65.95-67.95
#67.95-69.95
#69.95-71.95
#71.95-73.95
#73.95-75.95
intervals_of_heights = ["59.95-61.95", "61.95-63.95", "63.95-65.95", "65.95-67.95", "67.95-69.95", "69.95-71.95", "71.95-73.95", "73.95-75.95"]
num_of_intervals_of_heights = len(intervals_of_heights)
print("intervals_of_heights:")
print(intervals_of_heights)
print()

frequencies_of_heights_in_each_interval = [0] * num_of_intervals_of_heights

for i in range(0, num_of_heights):
    if(heights[i] >= 59.95 and heights[i] < 61.95):
        frequencies_of_heights_in_each_interval[0] += 1
    elif(heights[i] >= 61.95 and heights[i] < 63.95):
        frequencies_of_heights_in_each_interval[1] += 1
    elif(heights[i] >= 63.95 and heights[i] < 65.95):
        frequencies_of_heights_in_each_interval[2] += 1
    elif(heights[i] >= 65.95 and heights[i] < 67.95):
        frequencies_of_heights_in_each_interval[3] += 1
    elif(heights[i] >= 67.95 and heights[i] < 69.95):
        frequencies_of_heights_in_each_interval[4] += 1
    elif(heights[i] >= 69.95 and heights[i] < 71.95):
        frequencies_of_heights_in_each_interval[5] += 1
    elif(heights[i] >= 71.95 and heights[i] < 73.95):
        frequencies_of_heights_in_each_interval[6] += 1
    elif(heights[i] >= 73.95 and heights[i] <= 75.95):
        frequencies_of_heights_in_each_interval[7] += 1

print("frequencies_of_heights_in_each_interval:")
print(frequencies_of_heights_in_each_interval)
print()

relative_frequencies_of_heights_in_each_interval = [0] * num_of_intervals_of_heights

for i in range(0, num_of_intervals_of_heights):
    relative_frequencies_of_heights_in_each_interval[i] = frequencies_of_heights_in_each_interval[i]/num_of_heights

print("relative_frequencies_of_heights_in_each_interval:")
print(relative_frequencies_of_heights_in_each_interval)
print()

table = []
table.append(intervals_of_heights)
table.append(frequencies_of_heights_in_each_interval)
table.append(relative_frequencies_of_heights_in_each_interval)
table = matrix_transpose(table)
column_names = ["intervals_of_heights", "frequencies_of_heights_in_each_interval", "relative_frequencies_of_heights_in_each_interval"]
table_string = table_to_string(column_names, table, 0, num_of_intervals_of_heights, 0, 3)
print(table_string)
print()

plt.bar(intervals_of_heights, relative_frequencies_of_heights_in_each_interval, color = "steelblue", width = 0.5)
plt.xlabel("intervals_of_heights")
plt.ylabel("relative_frequencies_of_heights_in_each_interval")
plt.title("relative frequencies of heights of the sample group of people")

#label each bar with its y-value
label_bars(plt, intervals_of_heights, relative_frequencies_of_heights_in_each_interval)

plt.show()



    
