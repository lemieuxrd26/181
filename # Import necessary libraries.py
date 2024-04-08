# Import necessary libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Load the dataset
file_path = r'C:\Users\lemieuxrd26\Downloads\Restaurant Revenue.xlsx'
data = pd.read_excel(file_path)

# Define features and target variable
X = data[['Number_of_Customers', 'Menu_Price', 'Marketing_Spend', 
          'Average_Customer_Spending', 'Promotions', 'Reviews']]
y = data['Monthly_Revenue']

# Add constant to the features
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Print regression statistics
print(model.summary())
"GO BREWERS"