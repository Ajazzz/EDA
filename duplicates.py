
# To find duplicates in a Pandas DataFrame in Python, you can use the duplicated() method, 
# which returns a boolean Series indicating whether each row is a duplicate or not.
# Here's an example code snippet to find duplicates in a DataFrame using Python:


import pandas as pd

# create a sample DataFrame
df = pd.DataFrame({
    'Name': ['John', 'Mary', 'Bob', 'Mary', 'Sarah'],
    'Age': [25, 31, 28, 31, 29],
    'City': ['New York', 'Boston', 'Chicago', 'Boston', 'Chicago']
})

# check for duplicates based on all columns
duplicates = df[df.duplicated()]

# print the duplicate rows
print(duplicates)
