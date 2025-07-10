# Import necessary libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


#Step 1: Load the dataset
datas = {    'age': [10, 20, 30, 40, 50, 60,70, 80, 90, 100  ],'income': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000]}  
#Step 2: Create a DataFrame
df = pd.DataFrame(datas)
#Step 3: Display the DataFrame
print(df)
#Step 4: Split the dataset into training and testing sets
X = df[['age']]
y = df[['income']]

#Step 5: Train a logistic regression model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=5000)
model.fit(X_train.values, y_train.values.ravel()) 
# Step 6: Make predictions
score = model.predict([[33]])
# Step 7: Print the prediction

print("============================")
print("Prediction for age 33:", score[0])