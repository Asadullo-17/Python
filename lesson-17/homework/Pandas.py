#HOMEWORK 1

#1-task

import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
df.rename(columns={'First Name':'first_name','Age':'age'},inplace=True)

#2-task
print('First 3 rows:\n')
print(df.head(3))

#3-task

print('The mean age of individuals:',df['age'].mean())

#4-task

print(df[['first_name','City']])

#5-task
import numpy as np
df['Salary']=np.random.randint(50000,100000,size=len(df))

#6-task

print(df.describe(include='all'))

#HOMEWORK 2

#1-task

sales_and_expenses=pd.DataFrame({'Month':['Jan','Feb','Mar','Apr'],'Sales':[5000,6000,7500,8000],'Expenses':[3000,3500,4000,4500]})

#2-task

print('The max expense:',sales_and_expenses['Expenses'].max())
print('The max sale:',sales_and_expenses['Sales'].max())

#3-task

print('The min expense:',sales_and_expenses['Expenses'].min())
print('The min sale:',sales_and_expenses['Sales'].min())

#4-task

print('The average expense:',sales_and_expenses['Expenses'].mean())
print('The average sale:',sales_and_expenses['Sales'].mean())

#HOMEWORK 3

#1-task

import pandas as pd

expenses=pd.DataFrame({'Category':['Rent','Utilities','Groceries','Entertainment'],'January':[1200,200,300,150],'February':[1300,220,320,160],'March':[1400,240,330,170],'April':[1500,250,350,180]})
expenses.set_index('Category',inplace=True)
print(expenses)

#2-task

print('Max expense:\n',expenses[['January','February','March','April']].max())

#3-task

print('The min expense:\n',expenses[['January','February','March','April']].min())

#4-task

print('Average expense:\n',expenses[['January','February','March','April']].mean())
