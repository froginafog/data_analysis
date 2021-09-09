import pandas

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
    num_elements = len(data)
    data.sort()
    if(num_elements % 2 == 0):  #num_elements is even
        return (data[int(num_elements/2) - 1] + data[int(num_elements/2)])/2
    else:  #num_elements is odd
        return data[int((num_elements + 1)/2) - 1]

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
        
filepath = "CPI_table_input.csv"
df = csv_to_pandas(filepath)
#print("pandas dataframe:")
#print(df)
#print()

original_table_name, original_row_names, original_column_names, original_matrix = pandas_to_table(df)

table_string = table_to_string(original_table_name, original_row_names, original_column_names, original_matrix)

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

#--------------------------------------------------------------------------

median_each_row(column_names, matrix, original_matrix, num_digits_after_decimal_point)

#--------------------------------------------------------------------------

table_string = table_to_string(table_name, row_names, column_names, matrix)
print("table_string:")
print(table_string)
print()
