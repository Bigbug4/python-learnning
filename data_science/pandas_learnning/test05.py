import numpy as np

my_list = [92, 94, 88, 91, 87]
test_1 = np.array(my_list)
print(test_1)

import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

df.to_csv('clinic_data.csv')
print(type(df))
print(df)

clinic_north = df.clinic_north
print(type(clinic_north))
print(clinic_north)

clinic_north_south = df[['clinic_north', 'clinic_south']]
print(type(clinic_north_south))
print(clinic_north_south)

march = df.iloc[2]
print(type(march))
print(march)

april_may_june = df.iloc[3:6]
print(april_may_june)
print(type(df.iloc))

january = df[df.month =='January']
print(january)

march_april = df[(df.month =='March') | (df.month =='April')]
print(march_april)

january_february_march = df[df.month.isin(['January','February','March'])]
print(january_february_march)

df2 = df.loc[[1, 3, 5]].reset_index(drop=True,inplace=False)
print(df2)
print(df2.drop(0,axis=0))