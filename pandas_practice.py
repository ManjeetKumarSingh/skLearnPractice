

import numpy as np
import sys
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load the dataset
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1)

# Preprocess the dataset
load_data = load_data('org.csv')
print("Data loaded successfully.")
# print(load_data.head())

# print(load_data.Country.unique())

print(load_data.columns.tolist())

rows= load_data.shape[0];
columns= load_data.shape[1];
print(f"Number of rows: {rows}, Number of columns: {columns}")  

#Getting about thedata types 
print("Data types of each column:")
print(load_data.dtypes)