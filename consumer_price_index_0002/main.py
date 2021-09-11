import pandas
import matplotlib.pyplot as plt
import csv
from numpy.polynomial import Chebyshev

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
    for i in range(0, y_data_size):
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

def get_second_quartile(data): #The second quartile is the median.
    copy_of_data = data.copy()
    num_elements = len(copy_of_data)
    copy_of_data.sort()
    if(num_elements % 2 == 0):  #num_elements is even
        return (copy_of_data[int(num_elements/2) - 1] + copy_of_data[int(num_elements/2)])/2
    else:  #num_elements is odd
        return copy_of_data[int((num_elements + 1)/2) - 1]

def get_first_quartile(data): #The median on the subset of data on the left hand side of the second quartile.
    copy_of_data = data.copy()
    num_elements = len(copy_of_data)
    copy_of_data.sort()
    subset_of_data = []
    if(num_elements % 2 == 0):  #num_elements is even
        num_elements = int(num_elements/2)
        for i in range(0, num_elements):
            subset_of_data.append(copy_of_data[i])
        num_elements = len(subset_of_data)
        if(num_elements % 2 == 0):  #num_elements is even
            return (subset_of_data[int(num_elements/2) - 1] + data[int(num_elements/2)])/2
        else:  #num_elements is odd
            return subset_of_data[int((num_elements + 1)/2) - 1]
    else:  #num_elements is odd
        index_of_median = int(num_elements/2)
        for i in range(0, index_of_median):
            subset_of_data.append(copy_of_data[i])
        num_elements = len(subset_of_data)
        if(num_elements % 2 == 0):  #num_elements is even
            return (subset_of_data[int(num_elements/2) - 1] + subset_of_data[int(num_elements/2)])/2
        else:  #num_elements is odd
            return subset_of_data[int((num_elements + 1)/2) - 1]

def get_third_quartile(data): #The median on the subset of data on the right hand side of the second quartile.
    copy_of_data = data.copy()
    num_elements = len(data)
    copy_of_data.sort()
    subset_of_data = []
    if(num_elements % 2 == 0):  #num_elements is even
        for i in range(int(num_elements/2), num_elements):
            subset_of_data.append(copy_of_data[i])
        num_elements = len(subset_of_data)
        if(num_elements % 2 == 0):  #num_elements is even
            return (subset_of_data[int(num_elements/2) - 1] + subset_of_data[int(num_elements/2)])/2
        else:  #num_elements is odd
            return subset_of_data[int((num_elements + 1)/2) - 1]
    else:  #num_elements is odd
        index_of_median = int(num_elements/2)
        for i in range(index_of_median + 1, num_elements):
            subset_of_data.append(data[i])
        num_elements = len(subset_of_data)
        if(num_elements % 2 == 0):  #num_elements is even
            return (subset_of_data[int(num_elements/2) - 1] + subset_of_data[int(num_elements/2)])/2
        else:  #num_elements is odd
            return subset_of_data[int((num_elements + 1)/2) - 1]

def calculate_interquartile_range(data):
    copy_of_data = data.copy()
    first_quartile = get_first_quartile(copy_of_data)
    third_quartile = get_third_quartile(copy_of_data)
    interquartile_range = third_quartile - first_quartile
    return interquartile_range

def get_outliers(data):
    copy_of_data = data.copy()
    interquartile_range = calculate_interquartile_range(copy_of_data)
    first_quartile = get_first_quartile(copy_of_data)
    third_quartile = get_third_quartile(copy_of_data)
    lower_bound = first_quartile - 1.5 * interquartile_range
    upper_bound = third_quartile + 1.5 * interquartile_range
    outliers = []
    for value in data:
        if(value < lower_bound):
            outliers.append(value)
        if(value > upper_bound):
            outliers.append(value)
    return outliers

def remove_outliers(x_data, y_data):
    outliers = get_outliers(y_data)
    x_data_without_outliers = []
    y_data_without_outliers = []
    indices_at_which_outliers_are_removed = []
    num_data_points = len(y_data)
    num_outliers = len(outliers)
    for i in range(0, num_data_points):
        is_outlier = False
        for j in range(0, num_outliers):
            if(y_data[i] == outliers[j]):
                is_outlier = True
                indices_at_which_outliers_are_removed.append(i)
                break
        if(is_outlier == False):
            x_data_without_outliers.append(x_data[i])
            y_data_without_outliers.append(y_data[i])
    return x_data_without_outliers, y_data_without_outliers, indices_at_which_outliers_are_removed

def derivative_of_data_points(x_data, y_data):
    num_x_data_points = len(x_data)
    num_y_data_points = len(y_data)
    if(num_x_data_points != num_y_data_points):
        print("Error: the number of x_data points is not equal to the number of y_data points.")
    else:
        derivative_of_y_data = []
        for i in range(0, num_x_data_points - 1):
            dx = x_data[i + 1] - x_data[i]
            dy = y_data[i + 1] - y_data[i]
            derivative_of_y_data.append(dy/dx)       
        x_data_for_derivative_of_y_data = x_data[0:(num_x_data_points - 1)].copy()
        return x_data_for_derivative_of_y_data, derivative_of_y_data
        
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
    print("y_predicted = " + str(round(b_1_of_cpi, 3)) + " * x + " + str(round(b_0_of_cpi, 3)))
else:  
    print("y_predicted = " + str(round(b_1_of_cpi, 3)) + " * x - " + str(round(abs(b_0_of_cpi), 3)))
print()

cpi_predicted_data = []
for t in timeline:
    cpi_predicted_data.append(calculate_predicted_y(t, b_0_of_cpi, b_1_of_cpi))

x_data_regression_line_of_cpi = timeline
y_data_regression_line_of_cpi = cpi_predicted_data

#--------------------------------------------------------------------------

correlation_coefficient_cpi = calculate_correlation_coefficient(cpi_data, cpi_predicted_data)
print("correlation coefficient between cpi and the predicted cpi:", correlation_coefficient_cpi)
print()

#--------------------------------------------------------------------------

#finding a relationship between data-points
#and to draw a line of polynomial regression
degree = 88 #degree of the fitting polynomial
model_polynomial_for_cpi = Chebyshev.fit(timeline, cpi_data, degree)
print("model_polynomial_for_cpi:")
print(model_polynomial_for_cpi)
print()

x_data_for_model_polynomial_for_cpi = timeline
y_data_for_model_polynomial_for_cpi = []

for x in x_data_for_model_polynomial_for_cpi:
    y_data_for_model_polynomial_for_cpi.append(model_polynomial_for_cpi(x))

#--------------------------------------------------------------------------

outliers_of_cpi_data = get_outliers(cpi_data)
print("outliers_of_cpi_data:", outliers_of_cpi_data)
print()

#--------------------------------------------------------------------------

x_data_for_first_derivative_of_cpi, y_data_for_first_derivative_of_cpi = derivative_of_data_points(timeline, cpi_data)

#--------------------------------------------------------------------------

b_1_of_first_derivative_of_cpi = calculate_slope_of_regression_line(x_data_for_first_derivative_of_cpi, y_data_for_first_derivative_of_cpi) #slope of regression line
b_0_of_first_derivative_of_cpi = calculate_intercept_of_regression_line(b_1_of_first_derivative_of_cpi, x_data_for_first_derivative_of_cpi, y_data_for_first_derivative_of_cpi) #intercept of regression line

if(b_0_of_first_derivative_of_cpi >= 0):
    print("first_derivative_of_y_predicted = " + str(round(b_1_of_first_derivative_of_cpi, 3)) + " * x + " + str(round(b_0_of_first_derivative_of_cpi, 3)))
else:  
    print("first_derivative_of_y_predicted = " + str(round(b_1_of_first_derivative_of_cpi, 3)) + " * x - " + str(round(abs(b_0_of_first_derivative_of_cpi), 3)))
print()

y_data_for_first_derivative_of_cpi_predicted = []
for x in x_data_for_first_derivative_of_cpi:
    y_data_for_first_derivative_of_cpi_predicted.append(calculate_predicted_y(t, b_0_of_first_derivative_of_cpi, b_1_of_first_derivative_of_cpi))

x_data_regression_line_of_first_derivative_of_cpi = x_data_for_first_derivative_of_cpi
y_data_regression_line_of_first_derivative_of_cpi = y_data_for_first_derivative_of_cpi_predicted

#--------------------------------------------------------------------------

correlation_coefficient_first_derivative_cpi = calculate_correlation_coefficient(y_data_for_first_derivative_of_cpi, y_data_for_first_derivative_of_cpi_predicted)
print("correlation coefficient between the first derivative of cpi and the first derivative of the predicted cpi:", correlation_coefficient_first_derivative_cpi)
print()

#--------------------------------------------------------------------------

#finding a relationship between data-points
#and to draw a line of polynomial regression
degree = 87 #degree of the fitting polynomial
model_polynomial_for_first_derivative_of_cpi = Chebyshev.fit(x_data_for_first_derivative_of_cpi, y_data_for_first_derivative_of_cpi, degree)
print("model_polynomial_for_first_derivative_of_cpi:")
print(model_polynomial_for_first_derivative_of_cpi)
print()

x_data_for_model_polynomial_for_first_derivative_of_cpi = x_data_for_first_derivative_of_cpi
y_data_for_model_polynomial_for_first_derivative_of_cpi = []

for x in x_data_for_model_polynomial_for_first_derivative_of_cpi:
    y_data_for_model_polynomial_for_first_derivative_of_cpi.append(model_polynomial_for_first_derivative_of_cpi(x))

#--------------------------------------------------------------------------

outliers_of_first_derivative_of_cpi = get_outliers(y_data_for_first_derivative_of_cpi)
print("outliers_of_first_derivative_of_cpi:", outliers_of_first_derivative_of_cpi)
print()

#--------------------------------------------------------------------------

x_data_for_second_derivative_of_cpi, y_data_for_second_derivative_of_cpi = derivative_of_data_points(x_data_for_first_derivative_of_cpi, y_data_for_first_derivative_of_cpi)

#--------------------------------------------------------------------------

b_1_of_second_derivative_of_cpi = calculate_slope_of_regression_line(x_data_for_second_derivative_of_cpi, y_data_for_second_derivative_of_cpi) #slope of regression line
b_0_of_second_derivative_of_cpi = calculate_intercept_of_regression_line(b_1_of_second_derivative_of_cpi, x_data_for_second_derivative_of_cpi, y_data_for_first_derivative_of_cpi) #intercept of regression line

if(b_0_of_second_derivative_of_cpi >= 0):
    print("second_derivative_of_y_predicted = " + str(round(b_1_of_second_derivative_of_cpi, 3)) + " * x + " + str(round(b_0_of_second_derivative_of_cpi, 3)))
else:  
    print("second_derivative_of_y_predicted = " + str(round(b_1_of_second_derivative_of_cpi, 3)) + " * x - " + str(round(abs(b_0_of_second_derivative_of_cpi), 3)))
print()

y_data_for_second_derivative_of_cpi_predicted = []
for x in x_data_for_second_derivative_of_cpi:
    y_data_for_second_derivative_of_cpi_predicted.append(calculate_predicted_y(t, b_0_of_second_derivative_of_cpi, b_1_of_second_derivative_of_cpi))

x_data_regression_line_of_second_derivative_of_cpi = x_data_for_second_derivative_of_cpi
y_data_regression_line_of_second_derivative_of_cpi = y_data_for_second_derivative_of_cpi_predicted

#--------------------------------------------------------------------------

correlation_coefficient_second_derivative_cpi = calculate_correlation_coefficient(y_data_for_second_derivative_of_cpi, y_data_for_second_derivative_of_cpi_predicted)
print("correlation coefficient between the second derivative of cpi and the second derivative of the predicted cpi:", correlation_coefficient_second_derivative_cpi)
print()

#--------------------------------------------------------------------------

#finding a relationship between data-points
#and to draw a line of polynomial regression
degree = 87 #degree of the fitting polynomial
model_polynomial_for_second_derivative_of_cpi = Chebyshev.fit(x_data_for_second_derivative_of_cpi, y_data_for_second_derivative_of_cpi, degree)
print("model_polynomial_for_second_derivative_of_cpi:")
print(model_polynomial_for_second_derivative_of_cpi)
print()

x_data_for_model_polynomial_for_second_derivative_of_cpi = x_data_for_second_derivative_of_cpi
y_data_for_model_polynomial_for_second_derivative_of_cpi = []

for x in x_data_for_model_polynomial_for_second_derivative_of_cpi:
    y_data_for_model_polynomial_for_second_derivative_of_cpi.append(model_polynomial_for_second_derivative_of_cpi(x))

#--------------------------------------------------------------------------

outliers_of_second_derivative_of_cpi = get_outliers(y_data_for_second_derivative_of_cpi)
print("outliers_of_second_derivative_of_cpi:", outliers_of_second_derivative_of_cpi)
print()

#--------------------------------------------------------------------------

plt.figure(1)
plt.scatter(timeline, cpi_data, color = "midnightblue", label = "CPI")
plt.plot(x_data_regression_line_of_cpi , y_data_regression_line_of_cpi, color = "blue", label = "regression line for CPI")
plt.plot(x_data_for_model_polynomial_for_cpi, y_data_for_model_polynomial_for_cpi, color = "lightblue", label = "polynomial fit for CPI")
plt.legend(loc = "upper left")
plt.xticks(years)
plt.xlabel("Year")
plt.ylabel("CPI")
plt.grid()

#--------------------------------------------------------------------------

plt.figure(2)
plt.scatter(x_data_for_first_derivative_of_cpi, y_data_for_first_derivative_of_cpi, color = "darkgreen", label = "first derivative of CPI")
plt.plot(x_data_regression_line_of_first_derivative_of_cpi, y_data_regression_line_of_first_derivative_of_cpi, color = "green", label = "regression line for the first derivative of CPI")
plt.plot(x_data_for_model_polynomial_for_first_derivative_of_cpi, y_data_for_model_polynomial_for_first_derivative_of_cpi, color = "lightgreen", label = "polynomial fit for the first derivative of CPI")
plt.legend(loc = "lower left")
plt.xticks(years)
plt.xlabel("Year")
plt.ylabel("first derivative of CPI")
plt.grid()

#--------------------------------------------------------------------------

plt.figure(3)
plt.scatter(x_data_for_second_derivative_of_cpi, y_data_for_second_derivative_of_cpi, color = "darkgreen", label = "second derivative of CPI")
plt.plot(x_data_regression_line_of_second_derivative_of_cpi, y_data_regression_line_of_second_derivative_of_cpi, color = "green", label = "regression line for the second derivative of CPI")
plt.plot(x_data_for_model_polynomial_for_second_derivative_of_cpi, y_data_for_model_polynomial_for_second_derivative_of_cpi, color = "lightgreen", label = "polynomial fit for the second derivative of CPI")
plt.legend(loc = "upper left")
plt.xticks(years)
plt.xlabel("Year")
plt.ylabel("second derivative of CPI")
plt.grid()

#--------------------------------------------------------------------------

plt.figure(4)

plt.subplot(3, 1, 1) #plt.subplot(number of rows of plots, number of columns of plots, plot number)
plt.scatter(timeline, cpi_data, color = "midnightblue", label = "CPI")
plt.plot(x_data_regression_line_of_cpi , y_data_regression_line_of_cpi, color = "blue", label = "regression line for CPI")
plt.plot(x_data_for_model_polynomial_for_cpi, y_data_for_model_polynomial_for_cpi, color = "lightblue", label = "polynomial fit for CPI")
plt.legend(loc = "upper left")
plt.xticks(years)
plt.xlabel("Year")
plt.ylabel("CPI")
plt.grid()

plt.subplot(3, 1, 2)
plt.scatter(x_data_for_first_derivative_of_cpi, y_data_for_first_derivative_of_cpi, color = "darkgreen", label = "first derivative of CPI")
plt.plot(x_data_regression_line_of_first_derivative_of_cpi, y_data_regression_line_of_first_derivative_of_cpi, color = "green", label = "regression line for the first derivative of CPI")
plt.plot(x_data_for_model_polynomial_for_first_derivative_of_cpi, y_data_for_model_polynomial_for_first_derivative_of_cpi, color = "lightgreen", label = "polynomial fit for the first derivative of CPI")
plt.legend(loc = "lower left")
plt.xticks(years)
plt.xlabel("Year")
plt.ylabel("first derivative of CPI")
plt.grid()

plt.subplot(3, 1, 3)
plt.scatter(x_data_for_second_derivative_of_cpi, y_data_for_second_derivative_of_cpi, color = "darkgreen", label = "second derivative of CPI")
plt.plot(x_data_regression_line_of_second_derivative_of_cpi, y_data_regression_line_of_second_derivative_of_cpi, color = "green", label = "regression line for the second derivative of CPI")
plt.plot(x_data_for_model_polynomial_for_second_derivative_of_cpi, y_data_for_model_polynomial_for_second_derivative_of_cpi, color = "lightgreen", label = "polynomial fit for the second derivative of CPI")
plt.legend(loc = "upper left")
plt.xticks(years)
plt.xlabel("Year")
plt.ylabel("second derivative of CPI")
plt.grid()

#--------------------------------------------------------------------------

plt.show()
