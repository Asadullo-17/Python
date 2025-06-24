#HOMEWORK 2

#1-task

import pandas as pd

stock=pd.read_csv('D:\MAAB\PYTHON LESSONS\Lesson18\stockoverflow.txt')
stock.head()
stock['creationdate']=pd.to_datetime(stock['creationdate'])
before2014=stock[stock['creationdate']<'2014-01-01']
print(before2014)

#2-task

scores=stock[stock['score']>50]
print(scores)

#3-task

mediums=stock[(stock['score']>50) & (stock['score']<100)]
print(mediums)

#4-task
names=stock[stock['ans_name']=='Scott Boston']
print(names)

#5-task
users=['Demitri','doug','Mike Pennington','HYRY','Joe Kington']
names2=stock[stock['ans_name'].isin(users)]
print(names2)

#6-task

search=stock[(stock['creationdate']>='2014-03-01')&(stock['creationdate']<='2014-10-31')&(stock['ans_name']=='Unutbu')&(stock['score']<5)]
print(search)

#7-task

scores2=stock[((stock['score']>5)&(stock['score']<10))|(stock['viewcount']>10000)]
print(scores2)

#8-task

not_ans=stock[~(stock['ans_name']=='Scott Boston')]
print(not_ans)




#HOMEWORK 3

#1-task

import pandas as pd

titanic=pd.read_csv(r'D:\MAAB\PYTHON LESSONS\Lesson18\titanic.txt')
print(titanic)
select=titanic[((titanic['Sex']=='female')&(titanic['Pclass']==1))&((titanic['Age']>20)&(titanic['Age']<30))]
print(select)

#2-task

fare=titanic[titanic['Fare']>100]
dataframe2=pd.DataFrame(fare)
print(dataframe2)

#3-task

survived=titanic[(titanic['Survived']==0)&(titanic['SibSp']==0)&(titanic['Parch']==0)]
print(survived)

#4-task

embarking=titanic[(titanic['Embarked']=='C')&(titanic['Fare']>50)]
dataframe3=pd.DataFrame(embarking)
print(dataframe3)

#5-task

not_alone=titanic[(titanic['SibSp']==1)&(titanic['Parch']==1)]
print(not_alone)

#6-task

youngsters=titanic[(titanic['Survived']==1)&(titanic['Age']<=15)]
dataframe4=pd.DataFrame(youngsters)
print(dataframe4)

#7-task

cabins=titanic[(titanic['Cabin'].notna())&(titanic['Fare']>200)]
print(cabins)

#8-task

odds=titanic[titanic['PassengerId']%2==1]
dataframe5=pd.DataFrame(odds)
print(dataframe5)

#9-task

ticket_counts = titanic['Ticket'].value_counts()
unique_tickets = ticket_counts[ticket_counts == 1].index
unique_ticket_passengers = titanic[titanic['Ticket'].isin(unique_tickets)]
dataframe6=pd.DataFrame(unique_ticket_passengers)
print(dataframe6)

#10-task

female=titanic[(titanic['Name'].str.contains('Miss',na=False))&(titanic['Pclass']==1)]
dataframe7=pd.DataFrame(female)
print(dataframe7)
