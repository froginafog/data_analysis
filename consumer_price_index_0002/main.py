import pandas
import matplotlib.pyplot as plt
import csv

def table_to_string(table_name, row_names, column_names, matrix):
    row_names_copy = row_names.copy()
    num_rows = len(row_names_copy)
    for i in range(0, num_rows):
        if(type(row_names_copy[i]) != str and type(row_names_copy[i]) != int):
            integer, fraction = divmod(row_names_copy[i], 1)
            if fraction == 0:
                row_names_copy[i] = int(integer)
    #------------------------------------------------------            
    num_columns = len(column_names)
    column_names_copy = column_names.copy()
    for j in range(0, num_columns):
        if(type(column_names_copy[j]) != str and type(column_names_copy[j]) != int):
            integer, fraction = divmod(column_names_copy[j], 1)
            if fraction == 0:
                column_names_copy[j] = int(integer)
    #------------------------------------------------------ 
    column_0_width_max = len(table_name)
    for i in range(0, num_rows):
        width = len(str(row_names_copy[i]))
        if(width > column_0_width_max):
            column_0_width_max = width     
    temp_matrix = []
    for i in range(0, num_rows):
        temp_matrix.append(matrix[i].copy())
    column_widths_max = []
    for j in range(0, num_columns):
        column_widths_max.append(len(str(column_names_copy[j])))  
    for i in range(0, num_rows):
        for j in range(0, num_columns):
            temp_matrix[i][j] = str(temp_matrix[i][j])
            if(len(temp_matrix[i][j]) > column_widths_max[j]):
                column_widths_max[j] = len(temp_matrix[i][j])
    num_dashes = column_0_width_max + 4
    dashes_for_column_0 = ""
    for n in range(0, num_dashes):
        dashes_for_column_0 = dashes_for_column_0 + '-'
    output = dashes_for_column_0 + " "
    num_dashes = 0
    for n in range(0, num_columns):
        num_dashes = num_dashes + column_widths_max[n] + 3
    num_dashes += 1
    dashes = ""
    for n in range(0, num_dashes):
        dashes = dashes + '-'
    output = output + dashes + "\n|"
    s = " %" + str(column_0_width_max) + "s "
    s = s % table_name
    output = output + s + "| |"
    for j in range(0, num_columns):
        s = " %" + str(column_widths_max[j]) + "s "
        s = s % column_names_copy[j]
        output = output + s + "|"
    output = output + "\n" + dashes_for_column_0 + " " + dashes + "\n" + dashes_for_column_0 + " " + dashes + "\n"
    for i in range(0, num_rows):
        output = output + "|"
        s = " %" + str(column_0_width_max) + "s "
        s = s % row_names_copy[i]
        output = output + s + "| |"
        for j in range(0, num_columns):
            s = " %" + str(column_widths_max[j]) + "s "
            s = s % temp_matrix[i][j]
            output = output + s + "|"
        output = output + "\n" + dashes_for_column_0 + " " + dashes + "\n"
    return output

def csv_to_pandas(filepath):
    df = pandas.read_csv(filepath)
    pandas.options.display.max_rows = None
    pandas.options.display.max_columns = None
    return df

def pandas_to_table(df):
    table_name = df.columns[0]
    num_rows = df.shape[0]
    row_names = []
    for i in range(0, num_rows):
        row_names.append(df.loc[i][0])
    num_columns = df.shape[1]
    temp_column_names = df.columns.tolist()
    column_names = []
    for j in range(0, num_columns - 1):
        column_names.append(temp_column_names[j + 1])
    temp_matrix = df.values.tolist()
    matrix = []
    for i in range(0, num_rows):
        row = []
        for j in range(1, num_columns):
            row.append(temp_matrix[i][j])
        matrix.append(row)
    row_names_copy = row_names.copy()
    #----------------------------------------------------------
    num_rows = len(row_names_copy)
    for i in range(0, num_rows):
        if(type(row_names_copy[i]) != str and type(row_names_copy[i]) != int):
            integer, fraction = divmod(row_names_copy[i], 1)
            if fraction == 0:
                row_names_copy[i] = int(integer)
    #------------------------------------------------------            
    num_columns = len(column_names)
    column_names_copy = column_names.copy()
    for j in range(0, num_columns):
        if(type(column_names_copy[j]) != str and type(column_names_copy[j]) != int):
            integer, fraction = divmod(column_names_copy[j], 1)
            if fraction == 0:
                column_names_copy[j] = int(integer)
     #------------------------------------------------------ 
    return table_name, row_names_copy, column_names, matrix

def copy_matrix(matrix): 
    num_rows = len(matrix)
    copy_of_matrix = []
    for i in range(0, num_rows):
        copy_of_matrix.append(matrix[i].copy()) #to create an actual copy 
    return copy_of_matrix

def print_table_info(table_name, row_names, column_names, matrix):
    num_rows = len(row_names)
    num_columns = len(column_names)
    print("table_name:", table_name)
    print()
    print("row_names:", row_names)
    print()
    print("column_names:", column_names)
    print()
    print("num_rows:", num_rows)
    print()
    print("num_columns:", num_columns)
    print()
    print("matrix:", matrix)
    print()

def sum_each_row(column_names, matrix, original_matrix, num_digits_after_decimal_point):
    column_names.append("sum of each row") 
    num_rows_original_matrix = len(original_matrix)
    for i in range(0, num_rows_original_matrix):
        num_columns_original_matrix = len(original_matrix[i])
        total = 0
        for j in range(0, num_columns_original_matrix):
            total += original_matrix[i][j]
        total = round(total, num_digits_after_decimal_point)
        matrix[i].append(total)
    num_rows_matrix = len(matrix)
    num_rows_difference = num_rows_matrix - num_rows_original_matrix
    while(num_rows_difference > 0):
        matrix[num_rows_matrix - num_rows_difference].append("")
        num_rows_difference -= 1

def sum_each_column(row_names, matrix, original_matrix, num_digits_after_decimal_point):
    row_names.append("sum of each column")
    num_rows_original_matrix = len(original_matrix)
    num_columns_original_matrix = len(original_matrix[0]) 
    sums_of_each_column = []
    for j in range(0, num_columns_original_matrix):
        total = 0
        for i in range(0, num_rows_original_matrix):
            total += original_matrix[i][j]
        total = round(total, num_digits_after_decimal_point)
        sums_of_each_column.append(total)
    num_rows_matrix = len(matrix)
    num_columns_matrix = len(matrix[0])
    num_columns_difference = num_columns_matrix - num_columns_original_matrix
    while(num_columns_difference > 0):
        sums_of_each_column.append("")
        num_columns_difference -= 1
    matrix.append(sums_of_each_column)

def calculate_mean(data):
    num_elements = len(data)
    total = 0
    for i in range(0, num_elements):
        total += data[i]
    return total/num_elements

def mean_each_row(column_names, matrix, original_matrix, num_digits_after_decimal_point):
    column_names.append("mean of each row")
    num_rows_original_matrix = len(original_matrix)
    for i in range(0, num_rows_original_matrix):
        num_columns_original_matrix = len(original_matrix[i])
        total = 0
        for j in range(0, num_columns_original_matrix):
            total += original_matrix[i][j]
        average = total/num_columns_original_matrix
        average = round(average, num_digits_after_decimal_point)
        matrix[i].append(average)
    num_rows_matrix = len(matrix)
    num_rows_difference = num_rows_matrix - num_rows_original_matrix
    while(num_rows_difference > 0):
        matrix[num_rows_matrix - num_rows_difference].append("")
        num_rows_difference -= 1

def mean_each_column(row_names, matrix, original_matrix, num_digits_after_decimal_point):
    row_names.append("mean of each column")
    num_rows_original_matrix = len(original_matrix)
    num_columns_original_matrix = len(original_matrix[0])
    column_means = []
    for j in range(0, num_columns_original_matrix):
        total = 0
        for i in range(0, num_rows_original_matrix):
            total += original_matrix[i][j]
        average = total/num_rows_original_matrix
        average = round(average, num_digits_after_decimal_point)
        column_means.append(average)
    num_columns_matrix = len(matrix[0])
    num_columns_difference = num_columns_matrix - num_columns_original_matrix
    while(num_columns_difference > 0):
        column_means.append("")
        num_columns_difference -= 1
    matrix.append(column_means)

def calculate_median(data):
    data_copy = data.copy()
    num_elements = len(data_copy)
    data_copy.sort()
    if(num_elements % 2 == 0):  #num_elements is even
        return (data_copy[int(num_elements/2) - 1] + data_copy[int(num_elements/2)])/2
    else:  #num_elements is odd
        return data_copy[int((num_elements + 1)/2) - 1]

def median_each_row(column_names, matrix, original_matrix, num_digits_after_decimal_point):
    column_names.append("median of each row")
    num_rows_original_matrix = len(original_matrix)
    num_columns_original_matrix = len(original_matrix[0])
    for i in range(0, num_rows_original_matrix):
        median = calculate_median(original_matrix[i])
        median = round(median, num_digits_after_decimal_point)
        matrix[i].append(median)
    num_rows_matrix = len(matrix)
    num_rows_original_matrix = len(original_matrix)
    num_rows_difference = num_rows_matrix - num_rows_original_matrix
    while(num_rows_difference > 0): 
        matrix[num_rows_matrix - num_rows_difference].append("")
        num_rows_difference -= 1

def median_each_column(row_names, matrix, original_matrix, num_digits_after_decimal_point):
    row_names.append("median of each column")
    num_rows_original_matrix = len(original_matrix)
    num_columns_original_matrix = len(original_matrix[0])
    medians = []
    for j in range(0, num_columns_original_matrix):
        column = []
        for i in range(0, num_rows_original_matrix):
            column.append(original_matrix[i][j])
        median = calculate_median(column)
        median = round(median, num_digits_after_decimal_point)
        medians.append(median)
    num_columns_matrix = len(matrix[0])
    num_columns_difference = num_columns_matrix - num_columns_original_matrix
    while(num_columns_difference > 0):
        medians.append("")
        num_columns_difference -= 1
    matrix.append(medians)

def calculate_standard_deviation(data):
    N = len(data)  #size of the sample
    total = 0
    for n in data:
        total = total + n
    mean = total/N
    total = 0
    for n in data:
        total = total + (n - mean)**2
    sample_standard_deviation = (total/(N-1))**(1/2)
    return sample_standard_deviation

def standard_deviation_each_row(column_names, matrix, original_matrix, num_digits_after_decimal_point):
    column_names.append("std dev of each row")
    num_rows_original_matrix = len(original_matrix)
    for i in range(0, num_rows_original_matrix):
        std_dev = calculate_standard_deviation(original_matrix[i])
        std_dev = round(std_dev, num_digits_after_decimal_point)
        matrix[i].append(std_dev)
    num_rows_matrix = len(matrix)
    num_rows_difference = num_rows_matrix - num_rows_original_matrix
    while(num_rows_difference > 0):
        matrix[num_rows_matrix - num_rows_difference].append("")
        num_rows_difference -= 1

def standard_deviation_each_column(row_names, matrix, original_matrix, num_digits_after_decimal_point):
    row_names.append("std dev for each column")
    num_rows_original_matrix = len(original_matrix)
    num_columns_original_matrix = len(original_matrix[0])
    standard_deviations = []
    for j in range(0, num_columns_original_matrix):
        column = []
        for i in range(0, num_rows_original_matrix):
            column.append(original_matrix[i][j])
        std_dev = calculate_standard_deviation(column)
        std_dev = round(std_dev, num_digits_after_decimal_point)
        standard_deviations.append(std_dev)
    num_columns_matrix = len(matrix[0])
    num_columns_difference = num_columns_matrix - num_columns_original_matrix
    while(num_columns_difference > 0):
        standard_deviations.append("")
        num_columns_difference -= 1
    matrix.append(standard_deviations)

def table_to_csv(table_name, row_names, column_names, matrix, filepath):
    table = []
    row = []
    row.append(table_name)
    for column_name in column_names:
        row.append(column_name)
    table.append(row)
    num_rows = len(matrix)
    for i in range(0, num_rows):
        row = []
        row.append(row_names[i])
        for element in matrix[i]:
            row.append(element)
        table.append(row)
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(table)

def calculate_slope_of_regression_line(x_data, y_data): #b_1 = slope of the regression line
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
    return numerator_total / denominator_total

def calculate_intercept_of_regression_line(slope_of_regression_line, x_data, y_data):
    return calculate_mean(y_data) - slope_of_regression_line * calculate_mean(x_data)  #b_0 = intercept of the regression line 

#y_predicted = b_0 + b_1*x
def calculate_predicted_y(x, b_0, b_1):
    return b_0 + b_1*x
        
filepath = "CPI_table_input.csv"
df = csv_to_pandas(filepath)
#print("pandas dataframe:")
#print(df)
#print()

original_table_name, original_row_names, original_column_names, original_matrix = pandas_to_table(df)
table_string = table_to_string(original_table_name, original_row_names, original_column_names, original_matrix)
print("original table:")
print(table_string)
print()

#--------------------------------------------------------------------------

table_name = original_table_name
row_names = original_row_names.copy()
column_names = original_column_names.copy()
matrix = copy_matrix(original_matrix)

#--------------------------------------------------------------------------

num_digits_after_decimal_point = 1
sum_each_row(column_names, matrix, original_matrix, num_digits_after_decimal_point)
sum_each_column(row_names, matrix, original_matrix, num_digits_after_decimal_point)
mean_each_row(column_names, matrix, original_matrix, num_digits_after_decimal_point)
mean_each_column(row_names, matrix, original_matrix, num_digits_after_decimal_point)
median_each_row(column_names, matrix, original_matrix, num_digits_after_decimal_point)
median_each_column(row_names, matrix, original_matrix, num_digits_after_decimal_point)
standard_deviation_each_row(column_names, matrix, original_matrix, num_digits_after_decimal_point)
standard_deviation_each_column(row_names, matrix, original_matrix, num_digits_after_decimal_point)

#--------------------------------------------------------------------------

table_string = table_to_string(table_name, row_names, column_names, matrix)
print("table_string:")
print(table_string)
print()

#--------------------------------------------------------------------------

filepath = "CPI_table_output.csv"
table_to_csv(table_name, row_names, column_names, matrix, filepath)

#--------------------------------------------------------------------------

years = []
for year in original_row_names:
    years.append(year)

timeline = []
num_rows = len(original_matrix)
for i in range(0, num_rows):
    time = years[i]
    num_columns = len(original_matrix[i])
    for j in range(0, num_columns):
        timeline.append(time)
        time = time + 1 / num_columns

#--------------------------------------------------------------------------

cpi_data = []
for i in range(0, num_rows):
    for j in range(0, num_columns):
        cpi_data.append(original_matrix[i][j])

#--------------------------------------------------------------------------

b_1_of_cpi = calculate_slope_of_regression_line(timeline, cpi_data) #slope of regression line
b_0_of_cpi = calculate_intercept_of_regression_line(b_1_of_cpi, timeline, cpi_data) #intercept of regression line

if(b_0_of_cpi >= 0):
    print("y_predicted = " + str(b_1_of_cpi) + " * x + " + str(b_0_of_cpi))
else:  
    print("y_predicted = " + str(b_1_of_cpi) + " * x - " + str(abs(b_0_of_cpi)))

cpi_predicted = []
for t in timeline:
    cpi_predicted.append(calculate_predicted_y(t, b_0_of_cpi, b_1_of_cpi))

x_data_regression_line_of_cpi = timeline
y_data_regression_line_of_cpi = cpi_predicted

#--------------------------------------------------------------------------

plot_1 = plt.figure(1)
plt.scatter(timeline, cpi_data, color = "blue", label = "CPI")
plt.plot(x_data_regression_line_of_cpi , y_data_regression_line_of_cpi, color = "blue", label = "regression line for CPI")
plt.legend(loc = "upper left")
plt.xticks(years)
plt.xlabel("Year")
plt.ylabel("CPI")
plt.grid()
plt.show()
