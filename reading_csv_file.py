
# ========== IMPORTS/S ==========
import csv

# ========= PSEUDO CODE =========
# First Approach: This approach is without assigning a header, which it will automatically have a column name in the output/when printing
# - Code for opening the original csv file
with open('example1.csv', 'r') as file:
    sample_file = csv.reader(file)

# - Displaying the output using for loop
    for i in sample_file:
        print(i[0])


print("---------------------------------------------------------------------------------------------------------------------------------------")
# Second Approach: This approach is without assigning a header, which it will display an output of the first column content
# - Code for opening the original csv file
with open('example1.csv', 'r') as file:
    sample_file2 = csv.reader(file)
    
    next(sample_file2)
    
# - Displaying the output using for loop
    for i in sample_file2:
        print(i[0])