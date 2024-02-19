# ========= IMPORT/S =========
import json

# ========= PSEUDO CODE =========
# - Code for opening the file
# First Approach: Printing in one line Only
with open('example2.json', 'r') as file:
    sample_text = json.load(file)
    print(sample_text) # - Code for printing the content of the json file

print("\n")
print('-----------------------------')
print("\n")

# Second Approach: Printing what it is in the json file including the arrangement of datas.
# - Code for opening the file
with open('example2.json', 'r') as file:
    sample = json.load(file)
    
# Code for printing the output
    output = json.dumps(sample, indent=2) 
    print(output)
    
