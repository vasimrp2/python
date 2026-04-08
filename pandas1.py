import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],  
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

for i in range(len(data['Name'])):
    print(f"Name: {data['Name'][i]}, Age: {data['Age'][i]}, City: {data['City'][i]}")

    