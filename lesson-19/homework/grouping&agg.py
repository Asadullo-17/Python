#HOMEWORK ASSIGNMENT 1

#1-task

import pandas as pd

file=pd.read_csv('D:\MAAB\PYTHON LESSONS\Lesson19\sales_data.csv')
category=(file
    .groupby('Category')
    .agg(total_qty=pd.NamedAgg(column='Quantity', aggfunc='sum'),
          avg_price=pd.NamedAgg(column='Price', aggfunc='mean'),
          max_qty=pd.NamedAgg(column='Quantity', aggfunc='max'))
 )
print(category.reset_index())

#2-task

identify=file.groupby(['Category','Product'])['Quantity'].sum().reset_index()
top=identify.sort_values(['Category','Quantity'], ascending=[True,False])
top_sales=top.groupby('Category').head(1)
print(top_sales.reset_index())

#3-task

file['total_sale']=file['Quantity']*file['Price']
date=file.groupby('Date')['total_sale'].sum().reset_index()
maxdate=date.loc[date['total_sale'].idxmax()]
print(maxdate)



#HOMEWORK ASSIGNMENT 2

#1-task
orders=pd.read_csv('D:\MAAB\PYTHON LESSONS\Lesson19\customer_orders.csv')
orders
group=orders.groupby('CustomerID').size()
filtered=group[group>=20]
print(filtered)

#2-task

orders['price_per_unit']=orders['Price']/orders['Quantity']
avg=orders.groupby('CustomerID')['price_per_unit'].mean()
greater_than=avg[avg>120]
print(greater_than)

#3-task

group=orders.groupby('Product').agg(
    total_price=pd.NamedAgg(column='Price', aggfunc='sum'),
    total_qty=pd.NamedAgg(column='Quantity', aggfunc='sum')
)
filtered=group[group['total_qty']>=5]
print(filtered)




#HOMEWORK ASSIGNMENT 3

#1-task

import sqlite3 
import pandas as pd
import numpy as np


with sqlite3.connect(r'C:\Users\User\Downloads\population.db') as connection:
    population=pd.read_sql_query('select * from population',connection)

#2-task

groups = []
for i in range(1, 11):
    groups.append(f'Group {i}')

bins = [0, 200_000, 400_000, 600_000, 800_000, 1_000_000, 1_200_000, 1_400_000, 1_600_000, 1_800_000, float(np.inf)]
population['Salary Group'] = pd.cut(population['salary'], bins=bins)
population_group = population.groupby('Salary Group').count()['first_name']

population_pct = (population_group/population_group.sum()*100)
print(population_pct)

avg_salary=population.dropna().groupby('Salary Group').mean('salary').round(2)
print(avg_salary)

median_salary=population.dropna().groupby('Salary Group').median('salary')
print(median_salary)

population_number=population.dropna().groupby('Salary Group').count()['first_name']
print(population_number)

#3-task

state_group=population.groupby('state')
state_prcntg=state_group['first_name'].count()/population['first_name'].count()*100

state_avg=state_group['salary'].mean().round(2)

state_median=state_group['salary'].median()

state_num=state_group['first_name'].count()
