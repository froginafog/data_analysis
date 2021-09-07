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
    return table_name, row_names, column_names, matrix

filepath = "table_data.csv"
df = csv_to_pandas(filepath)
#print("pandas dataframe:")
#print(df)
#print()

table_name, row_names, column_names, matrix = pandas_to_table(df)

print("table_name:", table_name)
print()

print("row_names:", row_names)
print()

print("column_names:", column_names)
print()

print("matrix:", matrix)
print()

table_string = table_to_string(table_name, row_names, column_names, matrix)

print("table_string:")
print(table_string)
print()
    
