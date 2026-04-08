import pandas as pd
# Create a sample DataFrame
data = {
    "name": ["Vasim", "Ali", "Ahmed", "Sara"],
    "age": [25, 30, 35, 28],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"]
}

result = pd.DataFrame(data)
print(result)