# importing work libraries
import pandas as pd
import numpy as np


# reading the dataset
df = pd.read_csv("heart.csv")

# displaying the first 10 rows of the dataset
df.head(10)

# last 10 rows
df.tail(10)


# dropping unused columns
to_drop = ['cp',
          'fbs',
          'restecg',
          'thalach',
          'exang',
          'oldpeak',
          'slope',
          'thal',
           'target', 
          'ca']

df.drop(to_drop, inplace = True, axis = 1)
df.head(10)


# renaming the columns
new_name = {'age': 'Age',
           'sex': 'Sex',
           'trestbps': 'Bps',
           'chol': 'Cholesterol'
            }

df.rename(columns = new_name, inplace = True)
df.head()

# replacing the values with new significant codes
replace_values = {0: 'F', 1: 'M'}

df = df.replace({"Sex": replace_values})                                                                                             

df.head()


