# Data-Cleaning

## importing work libraries

````python
import pandas as pd
import numpy as np
````

## reading the dataset
```python
df = pd.read_csv("heart.csv")
```
## displaying the first 10 rows of the dataset
```python
df.head(10)
```
## displaying the last 10 rows
```python
df.tail(10)
```

## dropping unused columns
```python
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
```

## renaming the columns
```python
new_name = {'age': 'Age',
           'sex': 'Sex',
           'trestbps': 'Bps',
           'chol': 'Cholesterol'
            }

df.rename(columns = new_name, inplace = True)
df.head()
```
## replacing the values with new significant codes
```python
replace_values = {0: 'F', 1: 'M'}
df = df.replace({"Sex": replace_values})                                                                                     df.head()
```
