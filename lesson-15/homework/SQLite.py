#Lesson-15

#1-task

import sqlite3

with sqlite3.connect('Hometask_table.db') as connection:
    cursor=connection.cursor()
    cursor.execute('drop table if exists Roster')
    cursor.execute(''' 
    create table Roster(
        Name text,
        Species text,
        Age int
    )''')

print('Roster table created successfully!')
#2-task

import sqlite3

with sqlite3.connect('Hometask_table.db') as connection:
    cursor=connection.cursor()
    data=[('Benjamin Sisko','Human',40),
          ('Jadzia Dax','Trill',300),
          ('Kira Nerys','Bajoran',29)]
    cursor.executemany('insert into Roster values(?,?,?)',data)
    
print('Data inserted successfully!')
    
#3-task

import sqlite3

with sqlite3.connect('Hometask_table.db') as connection:
    cursor=connection.cursor()
    cursor.execute(''' 
    update Roster 
    set Name='Ezri Dax'
    where Name='Jadzia Dax' and Species='Trill'
    ''')
    
print('Name updated successfully!')

#4-task

import sqlite3

with sqlite3.connect('Hometask_table.db') as connection:
    cursor=connection.cursor()
    cursor.execute('''
    select Name, Age from Roster
    where Species='Bajoran'
    ''')
    result=cursor.fetchall()
    for row in result:
        print(row)
print('Success!')
