import pandas as pd

dataset = pd.read_csv('C:/Users/devarajan/Downloads/Telegram Desktop/index.csv')

'''
#this part is checking does the data is read 
print(dataset.head())

#this part is cleaning the data 
print(dataset.isnull().values.any())
'''

coffee_order_counts = dataset['coffee_name'].value_counts()
print("\nNumber of orders for each coffee type:")
print(coffee_order_counts)

coffee_revenue = dataset.groupby('coffee_name')['money'].sum().sort_values(ascending = False)
print(coffee_revenue)

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
coffee_revenue.plot(kind = 'bar')
plt.title('Total Revenue by coffee type')
plt.xlabel('Coffee Type')
plt.ylabel('Total Revenue in $')
plt.xticks(rotation = 45)
plt.show()
