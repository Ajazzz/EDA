
'''To find duplicates in a Pandas DataFrame in Python, you can use the duplicated() method, 
 which returns a boolean Series indicating whether each row is a duplicate or not.
# Here's an example code snippet to find duplicates in a DataFrame using Python: '''


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


# This code creates a sample DataFrame with columns for name, age, and city, and then checks for duplicates using the duplicated() method. 
# The resulting DataFrame duplicates contains only the rows that are duplicates of previous rows based on all columns.

# If you want to check for duplicates based on specific columns, you can pass a list of column names to the subset parameter of the duplicated() method. 
# For example, to check for duplicates based only on the "Name" and "City" columns, you could modify the code like this:


# check for duplicates based on specific columns
duplicates = df[df.duplicated(subset=['Name', 'City'])]
# This would return a DataFrame containing only the rows that have the same "Name" and "City" values as previous rows.
