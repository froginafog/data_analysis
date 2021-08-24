import matplotlib.pyplot as plt

def table_to_string(names_of_columns, table, starting_row, ending_row, starting_column, ending_column):
    num_rows = len(table)
    temp_table = []
    for i in range(0, num_rows):
        temp_table.append(table[i].copy())
    max_column_lengths = [0] * len(column_names)
    for j in range(starting_column, ending_column):
        max_column_lengths[j] = len(column_names[j])
    for i in range(starting_row, ending_row):
        for j in range(starting_column, ending_column):
            temp_table[i][j] = str(temp_table[i][j])
            if(len(temp_table[i][j]) > max_column_lengths[j]):
                max_column_lengths[j] = len(temp_table[i][j])
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
            s = s % temp_table[i][j]
            output = output + s + "|"
        output = output + "\n"
    output = output + dashes + "\n"
    return output

#push array 'a' into the last column of matrix 'A'
def push_back_column(a, A):
    num_elements_in_a = len(a)
    num_elements_in_A = len(A)
    if(num_elements_in_A == 0):
        for i in range(0, num_elements_in_a):
            A.append([])
    num_elements_in_A = len(A)
    if(num_elements_in_A != num_elements_in_a):
        print("num_elements_in_A != num_elements_in_a")
    for i in range(0, num_elements_in_a):
            A[i].append(a[i])

def get_percentile(data, k): #k = k th percentile
    num_points = len(data)
    index_of_k_percentile_lower = int(k * (num_points + 1) / 100) - 1
    index_of_k_percentile_upper = int(k * (num_points + 1) / 100)
    k_percentile = (data[index_of_k_percentile_lower] + data[index_of_k_percentile_upper])/2 
    return k_percentile

def label_bars(plt, x_data, y_data):
    num_items = len(x_data)
    for i in range(0, num_items):
        plt.text(x_data[i], y_data[i], str(y_data[i]), ha = "center")

#-------------------------------------------------------

num_of_hours_of_sleep = [4, 5, 6, 7, 8, 9, 10] 
frequencies = [2, 5, 7, 12, 14, 7, 3] #each value represents the number of people with respect to the number of hours of sleep
num_rows = len(num_of_hours_of_sleep)

#-------------------------------------------------------

num_people = 0
for i in range(0, num_rows):
    num_people = num_people + frequencies[i]

#-------------------------------------------------------

cumulative_frequencies = []
total = 0
for i in range(0, num_rows):
    total = total + frequencies[i]
    cumulative_frequencies.append(total)

#-------------------------------------------------------

relative_frequencies = []
for i in range(0, num_rows):
    relative_frequencies.append(round(frequencies[i]/num_people, 3))

#-------------------------------------------------------

cumulative_relative_frequencies = []
total = 0
for i in range(0, num_rows):
    total = total + relative_frequencies[i]
    cumulative_relative_frequencies.append(round(total, 3))
    
#-------------------------------------------------------

table = []
push_back_column(num_of_hours_of_sleep, table)
push_back_column(frequencies, table)
push_back_column(cumulative_frequencies, table)
push_back_column(relative_frequencies, table)
push_back_column(cumulative_relative_frequencies, table)

#-------------------------------------------------------

column_names = ["num_of_hours_of_sleep", "frequencies", "cumulative_frequencies", "relative_frequencies", "cumulative_relative_frequencies"]
table_string = table_to_string(column_names, table, 0, len(table), 0, len(table[0]))
print(table_string)

#-------------------------------------------------------

data_of_num_of_hours_of_sleep = []
num_items = len(num_of_hours_of_sleep)
for i in range(0, num_items):
    for n in range(0, frequencies[i]):
        data_of_num_of_hours_of_sleep.append(num_of_hours_of_sleep[i])

percentile_50 = get_percentile(data_of_num_of_hours_of_sleep, 50)
print("percentile_50:", percentile_50)

percentile_28 = get_percentile(data_of_num_of_hours_of_sleep, 28)
print("percentile_28:", percentile_28)

percentile_90 = get_percentile(data_of_num_of_hours_of_sleep, 90)
print("percentile_90:", percentile_90)

percentile_25 = get_percentile(data_of_num_of_hours_of_sleep, 25) #first quartile
print("percentile_25:", percentile_25)

#-------------------------------------------------------

plt.bar(num_of_hours_of_sleep, relative_frequencies, color = "steelblue", width = 0.5)
plt.xlabel("num_of_hours_of_sleep")
plt.ylabel("relative_frequencies")
plt.title("Relative Frequencies Of Number Of Hours Of Sleep Of The Sample Group Of People")

#label each bar with its y-value
label_bars(plt, num_of_hours_of_sleep, relative_frequencies)

plt.show()
