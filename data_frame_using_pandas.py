import pandas as pd

data = {
         "Name": ["Amit", "Raj", "Neha"],
         "Age": [28, 34, 25],
         "City": ["Delhi", "Mumbai", "Pune"]
}
df = pd.DataFrame(data) 
print("DataFrame created:")
print(df)

df.to_csv("output.csv", index=False)
print("DataFrame saved to output.csv")

# Using the pandas to do some opertions of the dataframe
column_count = df.shape[0] 
rows_count= df.shape[1]
print(f"Number of rows: {rows_count}, Number of columns: {column_count}")
#The steps is to print all the columns name in the dataset
columnName = df.columns.tolist()
print("Column names in the DataFrame:")
print(columnName)

df.describe()