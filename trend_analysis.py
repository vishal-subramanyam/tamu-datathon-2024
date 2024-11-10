# model to predict toppings based on ones already selected

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/all_data.csv')
meats = {'Brisket':{'April':0, 'May':0, 'June':0, 'July':0, 'August':0, 'September':0, 'October':0},
         'No Meat':{'April':0, 'May':0, 'June':0, 'July':0, 'August':0, 'September':0, 'October':0},
         'Pulled Pork':{'April':0, 'May':0, 'June':0, 'July':0, 'August':0, 'September':0, 'October':0},
         'Grilled Chicken':{'April':0, 'May':0, 'June':0, 'July':0, 'August':0, 'September':0, 'October':0},
         'Ham':{'April':0, 'May':0, 'June':0, 'July':0, 'August':0, 'September':0, 'October':0},
         'Bacon':{'April':0, 'May':0, 'June':0, 'July':0, 'August':0, 'September':0, 'October':0}}

totals = {'April':0, 'May':0, 'June':0, 'July':0, 'August':0, 'September':0, 'October':0}

month = -1
for i in range(len(df)):
    if (df['Parent Menu Selection'][i] == 'Mac and Cheese' or df['Parent Menu Selection'][i] == 'Grilled Cheese Sandwich'):
        if (df['Sent Date'][i].split(' ')[0].split('-')[1] == '04'):
            month = 'April'
        elif (df['Sent Date'][i].split(' ')[0].split('-')[1] == '05'):
            month = 'May'
        elif (df['Sent Date'][i].split(' ')[0].split('-')[1] == '06'):
            month = 'June'
        elif (df['Sent Date'][i].split(' ')[0].split('-')[1] == '07'):
            month = 'July'
        elif (df['Sent Date'][i].split(' ')[0].split('-')[1] == '08'):
            month = 'August'
        elif (df['Sent Date'][i].split(' ')[0].split('-')[1] == '09'):
            month = 'September'
        else:
            month = 'October'
        if df['Option Group Name'][i] == 'Choose Your Meats':
            meats[df['Modifier'][i]][month] += 1
            totals[month] += 1

meatData = {
    'Month': pd.date_range(start='2024-04-13', periods=7, freq='M'),
    'Total_Orders': totals.values(),
    'Brisket_Count': meats['Brisket'].values(),
    'No_Meat_Count': meats['No Meat'].values(),
    'Pulled_Pork_Count': meats['Pulled Pork'].values(),
    'Grilled_Chicken_Count': meats['Grilled Chicken'].values(),
    'Ham_Count': meats['Ham'].values(),
    'Bacon_Count': meats['Bacon'].values()
}
meatDf = pd.DataFrame(meatData)
meatDf['Month_Num'] = meatDf['Month'].dt.month
meatDf['Brisket_Percent'] = (meatDf['Brisket_Count'] / meatDf['Total_Orders']) * 100
meatDf['No_Meat_Percent'] = (meatDf['No_Meat_Count'] / meatDf['Total_Orders']) * 100
meatDf['Pulled_Pork_Percent'] = (meatDf['Pulled_Pork_Count'] / meatDf['Total_Orders']) * 100
meatDf['Grilled_Chicken_Percent'] = (meatDf['Grilled_Chicken_Count'] / meatDf['Total_Orders']) * 100
meatDf['Ham_Percent'] = (meatDf['Ham_Count'] / meatDf['Total_Orders']) * 100
meatDf['Bacon_Percent'] = (meatDf['Bacon_Count'] / meatDf['Total_Orders']) * 100

X = meatDf[['Month_Num']]
brisketY = meatDf['Brisket_Percent']
noMeatY = meatDf['No_Meat_Percent']
pulledPorkY = meatDf['Pulled_Pork_Percent']
grilledChickenY = meatDf['Grilled_Chicken_Percent']
hamY = meatDf['Ham_Percent']
baconY = meatDf['Bacon_Percent']
              
model = LinearRegression()
model.fit(X, brisketY)
meatDf['Predicted_Brisket_Percent'] = model.predict(X)
model.fit(X, noMeatY)
meatDf['Predicted_No_Meat_Percent'] = model.predict(X)
model.fit(X, pulledPorkY)
meatDf['Predicted_Pulled_Pork_Percent'] = model.predict(X)
model.fit(X, grilledChickenY)
meatDf['Predicted_Grilled_Chicken_Percent'] = model.predict(X)
model.fit(X, hamY)
meatDf['Predicted_Ham_Percent'] = model.predict(X)
model.fit(X, baconY)
meatDf['Predicted_Bacon_Percent'] = model.predict(X)
meatDf.to_csv('meat_linear_regression.csv', index=False)

sns.lineplot(data=meatDf, x='Month', y='Brisket_Percent', marker='o', label="Actual Brisket %")
sns.lineplot(data=meatDf, x='Month', y='Predicted_Brisket_Percent', marker='o', label="Predicted Trend", linestyle="--")

plt.title("Brisket Popularity Trend Over Time (as Percentage of Orders)")
plt.xlabel("Month")
plt.ylabel("Brisket % of Total Orders")
plt.legend()
plt.show()

sns.lineplot(data=meatDf, x='Month', y='No_Meat_Percent', marker='o', label="Actual No-Meat %")
sns.lineplot(data=meatDf, x='Month', y='Predicted_No_Meat_Percent', marker='o', label="Predicted Trend", linestyle="--")

plt.title("No-Meat Popularity Trend Over Time (as Percentage of Orders)")
plt.xlabel("Month")
plt.ylabel("No-Meat % of Total Orders")
plt.legend()
plt.show()

sns.lineplot(data=meatDf, x='Month', y='Pulled_Pork_Percent', marker='o', label="Actual Pulled Pork %")
sns.lineplot(data=meatDf, x='Month', y='Predicted_Pulled_Pork_Percent', marker='o', label="Predicted Trend", linestyle="--")

plt.title("Pulled Pork Popularity Trend Over Time (as Percentage of Orders)")
plt.xlabel("Month")
plt.ylabel("Pulled Pork % of Total Orders")
plt.legend()
plt.show()

sns.lineplot(data=meatDf, x='Month', y='Grilled_Chicken_Percent', marker='o', label="Actual Grilled Chicken %")
sns.lineplot(data=meatDf, x='Month', y='Predicted_Grilled_Chicken_Percent', marker='o', label="Predicted Trend", linestyle="--")

plt.title("Grilled Chicken Popularity Trend Over Time (as Percentage of Orders)")
plt.xlabel("Month")
plt.ylabel("Grilled Chicken % of Total Orders")
plt.legend()
plt.show()

sns.lineplot(data=meatDf, x='Month', y='Ham_Percent', marker='o', label="Actual Ham %")
sns.lineplot(data=meatDf, x='Month', y='Predicted_Ham_Percent', marker='o', label="Predicted Trend", linestyle="--")

plt.title("Ham Popularity Trend Over Time (as Percentage of Orders)")
plt.xlabel("Month")
plt.ylabel("Ham % of Total Orders")
plt.legend()
plt.show()

sns.lineplot(data=meatDf, x='Month', y='Bacon_Percent', marker='o', label="Actual Bacon %")
sns.lineplot(data=meatDf, x='Month', y='Predicted_Bacon_Percent', marker='o', label="Predicted Trend", linestyle="--")

plt.title("Bacon Popularity Trend Over Time (as Percentage of Orders)")
plt.xlabel("Month")
plt.ylabel("Bacon % of Total Orders")
plt.legend()
plt.show()
