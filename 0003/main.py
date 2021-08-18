import matplotlib.pyplot as plt

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

def calculate_median(data):
    num_elements = len(data)
    data.sort()
    if(num_elements % 2 == 0):  #num_elements is even
        return (data[int(num_elements/2) - 1] + data[int(num_elements/2)])/2
    else:  #num_elements is odd
        return data[int((num_elements + 1)/2) - 1]

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

years = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012]
num_years = len(years)    

#CPI = consumer prices index
CPI_table = [
                ["2003", 181.7, 183.1, 184.2, 183.8, 183.5, 183.7, 183.9, 184.6, 185.2, 185.0, 184.5, 184.3],
                ["2004", 185.2, 186.2, 187.4, 188.0, 189.1, 189.7, 189.4, 189.5, 189.9, 190.9, 191.0, 190.3],
                ["2005", 190.7, 191.8, 193.3, 194.6, 194.4, 194.5, 195.4, 196.4, 198.8, 199.2, 197.6, 196.8],
                ["2006", 198.3, 198.7, 199.8, 201.5, 202.5, 202.9, 203.5, 203.9, 202.9, 201.8, 201.5, 201.8],
                ["2007", 202.4, 203.5, 205.4, 206.7, 208.0, 208.4, 208.3, 207.9, 208.4, 208.9, 210.2, 210.0],
                ["2008", 211.1, 211.7, 213.5, 214.8, 216.6, 218.8, 220.0, 219.1, 218.8, 216.6, 212.4, 210.2],
                ["2009", 211.1, 212.2, 212.7, 213.2, 213.9, 215.7, 215.4, 215.8, 216.0, 216.2, 216.3, 216.0],
                ["2010", 216.7, 216.7, 217.6, 218.0, 218.2, 218.0, 218.0, 218.3, 218.4, 218.7, 218.8, 219.2],
                ["2011", 220.2, 221.3, 223.5, 224.9, 226.0, 225.7, 225.9, 226.6, 226.9, 226.4, 226.2, 225.7],
                ["2012", 226.7, 227.7, 229.4, 230.1, 229.8, 229.5, 229.1, 230.4, 231.4, 231.3, 230.2, 229.6]
            ]

num_rows = len(CPI_table)
num_columns = len(CPI_table[0])

column_names = ["year", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
CPI_table_string = table_to_string(column_names, CPI_table, 0, num_rows, 0, num_columns)
print(CPI_table_string)

#------------------------------------------------------------

for i in range(0, num_rows):
    for j in range(1, num_columns):
        CPI_table[i][j] = float(CPI_table[i][j])

#------------------------------------------------------------

average_CPI_of_each_year = []

for i in range(0, num_rows):
    average = calculate_mean(CPI_table[i][1:num_columns])
    average = round(average, 1)
    average_CPI_of_each_year.append(average)

print("average_CPI_of_each_year:")
print(average_CPI_of_each_year)
print()

#------------------------------------------------------------

median_of_each_year = []

for i in range(0, num_rows):
    median = calculate_median(CPI_table[i][1:num_columns])
    median = round(median, 1)
    median_of_each_year.append(median)
    
print("median_of_each_year:")
print(median_of_each_year)
print()

#------------------------------------------------------------

standard_deviation_of_each_year = []

for i in range(0, num_rows):
    standard_deviation = calculate_standard_deviation(CPI_table[i][1:num_columns])
    standard_deviation = round(standard_deviation, 1)
    standard_deviation_of_each_year.append(standard_deviation)
    
print("standard_deviation_of_each_year:")
print(standard_deviation_of_each_year)
print()

#------------------------------------------------------------

years = []
for i in range(0, num_rows):
    years.append(int(CPI_table[i][0]))

#------------------------------------------------------------

b_1_of_average_annual_CPI = calculate_slope_of_regression_line(years, average_CPI_of_each_year)    #slope of regression line
b_0_average_annual_CPI = calculate_mean(average_CPI_of_each_year) - b_1_of_average_annual_CPI * calculate_mean(years) #intercept of regression line

average_of_each_year_predicted = []
for n in years:
    average_of_each_year_predicted.append(calculate_predicted_y(n, b_0_average_annual_CPI, b_1_of_average_annual_CPI))

R_of_average_annual_CPI  = calculate_correlation_coefficient(average_CPI_of_each_year, average_of_each_year_predicted) #correlation coefficient
print("correlation coefficient R_of_average_annual_CPI:", R_of_average_annual_CPI)

x_min_of_average_annual_CPI = years[0]
x_max_of_average_annual_CPI = years[len(years) - 1]
x_data_regression_line_of_average_annual_CPI = []
y_data_regression_line_of_average_annual_CPI = []
x = x_min_of_average_annual_CPI
while(x <= x_max_of_average_annual_CPI):
    x_data_regression_line_of_average_annual_CPI.append(x)
    y_data_regression_line_of_average_annual_CPI.append(calculate_predicted_y(x, b_0_average_annual_CPI, b_1_of_average_annual_CPI))
    x = x + 1/12

#------------------------------------------------------------

time_line = []
x = x_min_of_average_annual_CPI
for i in range(0, num_rows):
    for j in range(1, num_columns):
        time_line.append(round(x,2))
        x = x + 1/12  #each year interval has 12 months

#------------------------------------------------------------

monthly_CPI = []

for i in range(0, num_rows):
    for j in range(1, num_columns):
        monthly_CPI.append(CPI_table[i][j])

#------------------------------------------------------------

b_1_of_monthly_CPI = calculate_slope_of_regression_line(time_line, monthly_CPI)    #slope of regression line
b_0_monthly_CPI = calculate_mean(monthly_CPI) - b_1_of_monthly_CPI * calculate_mean(time_line) #intercept of regression line

monthly_CPI_predicted = []
for n in time_line:
    monthly_CPI_predicted.append(calculate_predicted_y(n, b_0_monthly_CPI, b_1_of_monthly_CPI))

R_of_monthly_CPI  = calculate_correlation_coefficient(monthly_CPI, monthly_CPI_predicted) #correlation coefficient
print("correlation coefficient R_of_monthly_CPI:", R_of_monthly_CPI)

x_min_of_monthly_CPI = time_line[0]
x_max_of_monthly_CPI = time_line[len(time_line) - 1]
x_data_regression_line_of_monthly_CPI = []
y_data_regression_line_of_monthly_CPI = []
x = x_min_of_monthly_CPI
while(x <= x_max_of_monthly_CPI):
    x_data_regression_line_of_monthly_CPI.append(x)
    y_data_regression_line_of_monthly_CPI.append(calculate_predicted_y(x, b_0_monthly_CPI, b_1_of_monthly_CPI))
    x = x + 1/12

#------------------------------------------------------------

plt.scatter(years, average_CPI_of_each_year, color = "red", label = "average annual CPI")
plt.plot(x_data_regression_line_of_average_annual_CPI , y_data_regression_line_of_average_annual_CPI, color = "red", label = "regression line for average annual CPI")

plt.scatter(time_line, monthly_CPI, color = "blue", label = "monthly CPI")
plt.plot(x_data_regression_line_of_monthly_CPI , y_data_regression_line_of_monthly_CPI, color = "blue", label = "regression line for monthly CPI")

plt.xlabel("Year")
plt.ylabel("CPI")
plt.legend(loc = "upper left")
plt.xticks(years)
plt.title("Consumer Price Index CPI")
plt.show()

#------------------------------------------------------------