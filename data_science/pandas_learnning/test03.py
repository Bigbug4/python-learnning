import pandas as pd
import numpy as np

ser = pd.Series([4.5,7.2,-5.3,3.6], index=['d','b','a','c'])
print(ser)

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  # add Product Name and Color here
  'Product Name': ['t-shirt', 't-shirt', 'skirt','skirt'],
  'Color': ['blue', 'green', 'red','black'],
})

print(df1)
print("\n")

df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  # Fill in rows 3 and 4
  [3, 'San Francisco', 90],
  [4,' Sacramento', 115]
],
  columns=[
    #add column names here
    'Store ID', 'location', 'Number of Employees'
  ])

print(df2)
print("\n")

df3 = pd.DataFrame(np.arange(9).reshape(3,3), index=['a','c','d'], columns=['oh','te','ca'])
print(df3)