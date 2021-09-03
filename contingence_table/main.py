#contingence table

import pandas

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

def csv_to_pandas(filepath):
    df = pandas.read_csv(filepath)
    pandas.options.display.max_rows = None
    pandas.options.display.max_columns = None
    return df

def pandas_to_table(df):
    column_names = df.columns.tolist()
    table = df.values.tolist()
    return column_names, table

filepath = "contingence_table_data.csv"
df = csv_to_pandas(filepath)
print("pandas dataframe:")
print(df)
print()

num_rows = df.shape[0]
num_columns = df.shape[1]
print("num_rows:", num_rows)
print("num_columns:", num_columns)
print()

column_names, table_of_num_of_items = pandas_to_table(df)

string_of_table_of_num_of_items = table_to_string(column_names, table_of_num_of_items, 0, num_rows, 0, num_columns)
print("table of number of items with different intersecting R and C features:")
print(string_of_table_of_num_of_items)

total_num_of_items = 0
for i in range(0, num_rows):
    for j in range(1, num_columns):
        print("number of items of (" + str(table_of_num_of_items[i][0]) + " AND " + str(column_names[j]) + ") is " + str(table_of_num_of_items[i][j]))
        total_num_of_items += table_of_num_of_items[i][j]
    print()

print("total number of items:", total_num_of_items)
print()

table_of_probabilities_of_num_of_items = []

for i in range(0, num_rows):
    row = []
    row.append(table_of_num_of_items[i][0])
    for j in range(1, num_columns):
        probability_of_item = table_of_num_of_items[i][j]/total_num_of_items
        row.append(probability_of_item)
    table_of_probabilities_of_num_of_items.append(row)

string_of_table_of_probabilities_of_num_of_items = table_to_string(column_names, table_of_probabilities_of_num_of_items, 0, num_rows, 0, num_columns)
print("table of probabilities of number of items with different intersecting R and C features:")
print(string_of_table_of_probabilities_of_num_of_items)

#probabilities of R

probability_of_each_R = [] 

for i in range(0, num_rows):
    total_in_row = 0
    for j in range(1, num_columns):
        total_in_row += table_of_probabilities_of_num_of_items[i][j]
    probability_of_each_R.append(round(total_in_row, 2))   

for i in range(0, num_rows):
    print("probability of " + table_of_num_of_items[i][0] + ": " + str(probability_of_each_R[i]))

print()

#probabilities of C

probability_of_each_C = [] 

for j in range(1, num_columns):
    total_in_column = 0
    for i in range(0, num_rows):
        total_in_column += table_of_probabilities_of_num_of_items[i][j]
    probability_of_each_C.append(round(total_in_column, 2))

for j in range(1, num_columns):
    print("probability of " + column_names[j] + ": " + str(probability_of_each_C[j - 1]))

print()


