import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('all_data.csv')
num_sales_per_month = [0] * 7

for i in range(len(df)):
    if not isinstance(df['Sent Date'][i], str):
        continue
    month = df['Sent Date'][i].split(' ')[0].split('-')[1]
    if (i == len(df) - 1 or df['Order ID'][i] != df['Order ID'][i+1]):
        num_sales_per_month[int(month) - 4] += 1

plt.plot(num_sales_per_month)
plt.title('Number of sales by month')
x_labels = ['April', 'May', 'June', 'July', 'August', 'September', 'October']
plt.xticks(ticks=[0,1,2,3,4,5,6],labels=x_labels)
plt.xlabel('Month')
plt.ylabel('Number of orders')
plt.show()


