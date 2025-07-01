#Dataframe 1: Student Grades 

import pandas as pd
import matplotlib.pyplot as plt

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

#1-task

df1['Average']=df1[['Math','English','Science']].mean(axis=1).round(2)
print(df1)

#2-task

highest_avg=df1.sort_values('Average',ascending=False).head(1)
print(highest_avg)

#3-task

df1['Total']=df1[['Math','English','Science']].sum(axis=1)
print(df1)

#4-task

subjects=df1[['Math','English','Science']].mean(axis=0)
plt.bar(subjects.index,subjects.values,color=['g','b','y'])
plt.title('Average grades per subject')
plt.xlabel('Subject')
plt.ylabel('Grades')
plt.tight_layout()
plt.show()


#Dataframe 2: Sales Data

import pandas as pd
import matplotlib.pyplot as plt

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

#1-task

df2['Total sales']=df2[['Product_A','Product_B','Product_C']].sum(axis=1)
print(df2)

#2-task

highest_sales = df2.loc[df2['Total sales'].idxmax()]
print(highest_sales)

#3-task

pct_change=df2[['Product_A','Product_B','Product_C']].pct_change()*100
pct_change['Date']=df2['Date']
pct_change=pct_change[['Date','Product_A','Product_B','Product_C']]
print(pct_change)

#4-task

plt.figure(figsize=(10,6))
plt.plot(df2['Date'],df2['Product_A'],label='Product A')
plt.plot(df2['Date'],df2['Product_B'],label='Product B')
plt.plot(df2['Date'],df2['Product_C'],label='Product C')

plt.title('Sales trends')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.show()


#Datframe 3: Employee information

import pandas as pd
import matplotlib.pyplot as plt

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

#1-task

avg_salary=df3.groupby('Department')['Salary'].mean().round(2)
print(avg_salary)

#2-task

max_experience = df3.loc[df3['Experience (Years)'].idxmax()]
print(max_experience)

#3-task

min_salary=df3['Salary'].min()
df3['Salary Increase (%)']=(((df3['Salary']-min_salary)/min_salary)*100).round(2)
print(df3)

#4-task

count=df3.groupby('Department')['Department'].count()
plt.figure(figsize=(4,6))
plt.bar(count.index,count.values,color=['r','b','y'],label='Distribution of employees')
plt.xlabel('Department')
plt.ylabel('Number of employees')
plt.tight_layout()
plt.show()

#Dataframe 4: Customer Orders
import pandas as pd
import matplotlib.pyplot as plt

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

#1-task

total_revenue=df4['Total_Price'].sum()
print(total_revenue)

#2-task
orders=df4.groupby('Product')['Quantity'].sum().idxmax()
counts=df4.groupby('Product')['Quantity'].sum()
print(f'Most ordered product:{orders}' )

#3-task

count=df4['Quantity'].mean()
print(count)

#4-task

totals=df4.groupby('Product')['Total_Price'].sum()
plt.pie(totals.values,labels=['Product A','Product B','Product C'],colors=['r','b','y'],)
plt.title('Distribution of sales')
plt.legend()
plt.show()






