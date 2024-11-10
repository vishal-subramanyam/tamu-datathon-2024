import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# total sales
df = pd.read_csv('data/all_data.csv')
num_sales_per_month = [0] * 7
hourly_sales = {'07':0,'08':0,'09':0,'10':0, '11':0, '12':0, '13':0, '14':0, '15':0, '16':0, '17':0, '18':0, '19':0, '20':0, '21':0, '22':0, '23':0, '00':0}


for i in range(len(df)):
    if not isinstance(df['Sent Date'][i], str):
        continue
    month = df['Sent Date'][i].split(' ')[0].split('-')[1]
    hour = df['Sent Date'][i].split(' ')[1].split(':')[0]
    if (i == len(df) - 1 or df['Order ID'][i] != df['Order ID'][i+1]):
        num_sales_per_month[int(month) - 4] += 1
        hourly_sales[hour] += 1

hourly_sales_list = list(hourly_sales.values())


plt.figure()
plt.plot(num_sales_per_month)
plt.title('Number of sales by month')
x_labels = ['April', 'May', 'June', 'July', 'August', 'September', 'October']
plt.xticks(ticks=[0,1,2,3,4,5,6],labels=x_labels, fontsize=9)
plt.xlabel('Month')
plt.ylabel('Number of orders')
plt.show()

plt.figure()
plt.plot(hourly_sales_list)
plt.title('Number of sales by hour')
x_labels = ['7am','8am','9am', '10am', '11am', '12pm', '1pm', '2pm', '3pm', '4pm', '5pm', '6pm', '7pm', '8pm', '9pm', '10pm', '11pm', '12am']
plt.xticks(ticks=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17], labels=x_labels, fontsize=6)
plt.xlabel('Time')
plt.ylabel('Number of orders')
plt.show()
# sales per hour




