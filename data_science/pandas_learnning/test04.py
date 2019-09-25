'''
import csv

with open('cupcakes.csv','a') as fw:
	wr =csv.writer(fw)
	wr.writerow(['name','cake_flavor','frosting_flavor','topping'])
	for x in range(3):
		wr.writerow(['Devil\'s Food','chocolate','chocolate','chocolate shavings'])
'''

import pandas as pd

df = pd.read_csv('cupcakes.csv')
print(df)
print(df.info())

df1 = pd.DataFrame([[1, 'San Diego', 100],
					[2, 'Los Angeles', 120],
					[3, 'San Francisco', 90],
					[4,' Sacramento', 115]],
					columns=['Store ID', 'location', 'Number of Employees'
							])

df1.to_csv('Employees_data.csv')