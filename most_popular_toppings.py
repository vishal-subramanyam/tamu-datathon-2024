import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('all_data.csv')
num_orders = 0

toppings = set()
meats = set()
cheeses = set()
drizzles = set()

cheese_dict = {'Cheddar' : 0, 'Gouda' : 0, 'NO CHEESE' : 0, 'Pepper Jack' : 0, 'MIX' : 0, 'Alfredo' : 0}
meats_dict = {'Brisket' : 0, 'No Meat' : 0, 'Pulled Pork' : 0, 'Grilled Chicken' : 0, 'Ham' : 0, 'Bacon' : 0}
toppings_dict = {'Broccoli' : 0, 'Mushrooms' : 0, 'Tomatoes' : 0, 'Jalapenos' : 0, 'Pineapple' : 0, 'Onions' : 0, 'No Toppings' : 0, 'Corn' : 0, 'Parmesan' : 0, 'Breadcrumbs' : 0, 'Bell Peppers' : 0}
drizzles_dict = {'Buffalo' : 0, 'Garlic Parmesan' : 0, 'Ranch' : 0, 'Pesto' : 0, 'BBQ' : 0, 'Hot Honey' : 0, 'No Drizzle' : 0}

parent_selections = set()
for i in range(len(df)):
    if (df['Parent Menu Selection'][i] == 'Mac and Cheese' or df['Parent Menu Selection'][i] == 'Grilled Cheese Sandwich'):
        if df['Option Group Name'][i] == 'Choose Your Cheese':
            #cheeses.add(df['Modifier'][i])
            cheese_dict[df['Modifier'][i]] += 1
        if df['Option Group Name'][i] == 'Choose Your Meats':
            #meats.add(df['Modifier'][i])
            meats_dict[df['Modifier'][i]] += 1
        if df['Option Group Name'][i] == 'Choose Your Toppings':
            #toppings.add(df['Modifier'][i])
            toppings_dict[df['Modifier'][i]] += 1
        if df['Option Group Name'][i] == 'Choose Your Drizzles':
            #drizzles.add(df['Modifier'][i])
            drizzles_dict[df['Modifier'][i]] += 1
        if (i == len(df) - 1 or df['Order ID'][i] != df['Order ID'][i+1]):
            num_orders += 1
        #parent_selections.add(df['Parent Menu Selection'][i])

cheese_totals = []
meat_totals = []
topping_totals = []
drizzle_totals = []

for value in cheese_dict.values():
    cheese_totals.append(value/num_orders * 100)
for value in meats_dict.values():
    meat_totals.append(value / num_orders * 100)
for value in toppings_dict.values():
    topping_totals.append(value / num_orders * 100)
for value in drizzles_dict.values():
    drizzle_totals.append(value / num_orders * 100)

cheese_lbls = ['Cheddar', 'Gouda', 'No Cheese', 'Pepper Jack', 'Mixed', 'Alfredo']
plt.figure()
plt.pie(cheese_totals, labels=cheese_lbls, autopct='%1.1f%%')
plt.title('Percentage of cheese orders')
plt.show()

meat_lbls = ['Brisket', 'No Meat', 'Pulled Pork', 'Grilled Chicken', 'Ham', 'Bacon']
plt.figure()
plt.pie(meat_totals, labels=meat_lbls, autopct='%1.1f%%')
plt.title('Percentage of meat orders')
plt.show()

topping_lbls = ['Broccoli', 'Mushrooms', 'Tomatoes', 'Jalapenos', 'Pineapple', 'Onions', 'No Toppings', 'Corn', 'Parmesan', 'Breadcrumbs', 'Bell Peppers']
plt.figure()
plt.pie(topping_totals, labels=topping_lbls, autopct='%1.1f%%')
plt.title('Percentage of topping orders')
plt.show()

drizzle_lbls = ['Buffalo', 'Garlic Parmesan', 'Ranch', 'Pesto', 'BBQ', 'Hot Honey', 'No Drizzle']
plt.figure()
plt.pie(drizzle_totals, labels=drizzle_lbls, autopct='%1.1f%%')
plt.title('Percentage of drizzle orders')
plt.show()

#print('Cheeses:', cheeses, '\nMeats:', meats, '\nToppings:', toppings, '\nDrizzles:', drizzles,'\nParent selections:', parent_selections)

