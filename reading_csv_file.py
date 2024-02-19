
# ========== IMPORTS/S ==========
import csv

# ========= PSEUDO CODE =========
# This approach is without assigning a header, which it will automatically have a column name in the output/when printing
# - Code for opening the original csv file
with open('example1.csv', 'r') as file:
    sample_file = csv.reader(file)

# - Displaying the output using for loop
    for i in sample_file:
        print(i[0])
        

        
