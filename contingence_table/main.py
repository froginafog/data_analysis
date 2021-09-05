#contingence table

import pandas

def table_to_string(table_name, row_names, column_names, matrix):
    num_rows = len(row_names)
    column_0_width_max = len(table_name)
    for i in range(0, num_rows):
        width = len(row_names[i])
        if(width > column_0_width_max):
            column_0_width_max = width     
    temp_matrix = []
    for i in range(0, num_rows):
        temp_matrix.append(matrix[i].copy())
    column_widths_max = []
    num_columns = len(column_names)
    for j in range(0, num_columns):
        column_widths_max.append(len(column_names[j]))  
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
        s = s % column_names[j]
        output = output + s + "|"
    output = output + "\n" + dashes_for_column_0 + " " + dashes + "\n" + dashes_for_column_0 + " " + dashes + "\n"
    for i in range(0, num_rows):
        output = output + "|"
        s = " %" + str(column_0_width_max) + "s "
        s = s % row_names[i]
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
    return table_name, row_names, column_names, matrix

filepath = "contingence_table_data.csv"
df = csv_to_pandas(filepath)
print("pandas dataframe:")
print(df)
print()

table_name, row_names, column_names, matrix_num_items = pandas_to_table(df)

string_table_num_items = table_to_string(table_name, row_names, column_names, matrix_num_items)
print("table of number of items with different intersecting R and C features:")
print(string_table_num_items)

num_rows = len(row_names)
num_columns = len(column_names)

total_num_items = 0
for i in range(0, num_rows):
    for j in range(0, num_columns):
        print("number of items of (" + str(row_names[i]) + " AND " + str(column_names[j]) + ") is " + str(matrix_num_items[i][j]))
        total_num_items += matrix_num_items[i][j]

print()

print("total number of items:", total_num_items)
print()

#probabilities of each (R AND C)

matrix_probabilities_num_items = [] 

for i in range(0, num_rows):
    row = []
    for j in range(0, num_columns):
        probability_item = matrix_num_items[i][j]/total_num_items
        probability_item = round(probability_item, 6)
        row.append(probability_item)
    matrix_probabilities_num_items.append(row)

table_name = "probabilities of number of items"
string_table_probabilities_num_items = table_to_string(table_name, row_names, column_names, matrix_probabilities_num_items)
print("table of probabilities of number of items with different intersecting R and C features:")
print(string_table_probabilities_num_items)

#probabilities of (R AND C)

for i in range(0, num_rows):
    for j in range(0, num_columns):
        probability_R_AND_C = matrix_probabilities_num_items[i][j]
        print("probability of (" + str(row_names[i]) + " AND " + str(column_names[j]) + "): " + str(probability_R_AND_C))
        
print()

#probabilities of R

probability_each_R = [] 

for i in range(0, num_rows):
    total_in_row = 0
    for j in range(0, num_columns):
        total_in_row += matrix_probabilities_num_items[i][j]
    probability_each_R.append(round(total_in_row, 6))   

for i in range(0, num_rows):
    print("probability of " + str(row_names[i]) + ": " + str(probability_each_R[i]))

#probabilities of C

probability_each_C = [] 

for j in range(0, num_columns):
    total_in_column = 0
    for i in range(0, num_rows):
        total_in_column += matrix_probabilities_num_items[i][j]
    probability_each_C.append(round(total_in_column, 6))

for j in range(0, num_columns):
    print("probability of " + str(column_names[j]) + ": " + str(probability_each_C[j]))

print()

#check if each pair of R and C are mutually independent
#if P(R AND C) = P(R) * P(C), then R and C are mutually independent

for i in range(0, num_rows):
    for j in range(0, num_columns):
        if(matrix_probabilities_num_items[i][j] == probability_each_R[i] * probability_each_C[j]):
            print(str(row_names[i]) + " and " + str(column_names[j]) + " are mutually independent")
        else:
            print(str(row_names[i]) + " and " + str(column_names[j]) + " are not mutually independent") 

print()

#probabilities of (R OR C)
#P(R AND C) + P(R OR C) = P(R) + P(C)
#P(R OR C) = P(R) + P(C) - P(R AND C)

for i in range(0, num_rows):
    for j in range(0, num_columns):
        probability_R_OR_C = probability_each_R[i] + probability_each_C[j] - matrix_probabilities_num_items[i][j]
        probability_R_OR_C = round(probability_R_OR_C, 6)
        print("probability of (" + str(row_names[i]) + " OR " + str(column_names[j]) + "): " + str(probability_R_OR_C))

print()

#probabilities of if C occurred then R occurs 
#P(R|C) = P(R AND C)/P(C)
    
for i in range(0, num_rows):
    for j in range(0, num_columns):
        probability_if_C_then_R = matrix_probabilities_num_items[i][j] / probability_each_C[j]
        probability_if_C_then_R = round(probability_if_C_then_R, 6)
        print("probability of if " + str(column_names[j]) + " then " + str(row_names[i]) + ": " + str(probability_if_C_then_R))

print()

#probabilities of if R occurred then C occurs
#P(C|R) = P(R AND C)/P(R)
    
for i in range(0, num_rows):
    for j in range(0, num_columns):
        probability_if_R_then_C = matrix_probabilities_num_items[i][j] / probability_each_R[i]
        probability_if_R_then_C = round(probability_if_R_then_C, 6)
        print("probability of if " + str(row_names[i]) + " then " + str(column_names[j]) + ": " + str(probability_if_R_then_C))

print()















    
