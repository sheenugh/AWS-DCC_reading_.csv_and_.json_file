# ========= IMPORT/S =========
import json

# ========= PSEUDO CODE =========
# - Code for opening the file
# First Approach: In one line Only
with open('example2.json', 'r') as file:
    sample_text = json.load(file)
    print(sample_text) # - Code for printing the content of the json file
