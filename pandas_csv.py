import pandas as pd
# Operations with csv files using pandas
# Reading a csv file
data = pd.read_csv('chc.csv')
# to csv
#print(data.to_json())

# to html format 
#print(data.to_html())

# To String
# print(data.to_string())

# To read first 5 rows including columns
#print(data.head()) 

#To print only first 5 rows of name column
#print(data['Name'])

# Print name by custom code 
# result = data['Name']
# sr = 1
# for i in range(len(result)):
#     print(f"{sr} = {result[i]}")
#     sr = sr+1

