#Lesson-2

#1-task
from datetime import datetime

name=input('Enter your name:')
year_of_birth=int(input('Enter your year of birth:'))
current_year=datetime.now().year
year=current_year-year_of_birth

print(f'Your name is {name}, you are {year} years old')

#2-task
from collections import Counter


txt = 'LMaasleitbtui'.lower()
txt_counter=Counter(txt)
cars=['malibu','lasetti','matiz','tiko','nexia']
found_cars = []
for car in cars:
    if not Counter(car) - txt_counter:
        found_cars.append(car)

print('cars available',found_cars)

#3-task
from collections import Counter

txt = 'MsaatmiazD'.lower()
txt_counter=Counter(txt)
cars=['malibu','lasetti','matiz','damas','nexia']
found_cars=[]

for car in cars:
    if not Counter(car)-txt_counter:
        found_cars.append(car)
print(f'available cars:{found_cars}')


#4-task
txt = "I'am John. I am from London"
residence=txt.split('I am from')[1]
print(residence)

#5-task
txt=input()
print(txt[::-1])

#6-task
text = "Asadullo"
count=0
vowels = "aeiouAEIOU"
for char in text:
    if char in vowels:
       count+=1

print(count)

#7-task
nums=list(map(int,input('Enter numbers:').split()))
print(max(nums))

#8-task
text=input('Enter the text:')
if text==text[::-1]:
    print('text is palindrome')
else:
    print('text is not palindrome')
    
#9-task
email=input('Enter your email:')
sep=email.split('@')[1]
print(sep)

#10-task

import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$"
password = ""
for _ in range(12):
    password += chars[random.randint(0, len(chars)-1)]

print(password)

