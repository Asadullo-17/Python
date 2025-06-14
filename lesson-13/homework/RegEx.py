#1-task

from datetime import datetime
from dateutil.relativedelta import relativedelta
birthdate=input('Enter birthdate(YYYY-mm-dd): ')
dob=datetime.strptime(birthdate, '%Y-%m-%d')
today=datetime.today()
age=relativedelta(today,dob)
print(f'Your age is: {age.years} years,{age.months} months,{age.days} days')

#2-task
from datetime import datetime
from dateutil.relativedelta import relativedelta
birthdate=input('Enter birthdate(YYYY-mm-dd): ')
dob=datetime.strptime(birthdate,'%Y-%m-%d')
today=datetime.today()

new_dob=dob.replace(year=today.year)
if new_dob<today:
    new_dob=new_dob.replace(year=today.year+1) 

days=(new_dob-today).days

print(f'{days} days until your next birthday')

#3-task
from datetime import datetime,timedelta
current=input("Enter the current date and time (YYYY-mm-dd HH:MM:SS) : ")
duration=input("Enter duration of the meeting in hours and minutes(HH:MM): ")
cur=datetime.strptime(current,'%Y-%m-%d %H:%M:%S')
h,m=map(int, duration.split(':'))
dur=timedelta(hours=h,minutes=m)
end=cur+dur
print(end)

#4-task

from datetime import datetime
from zoneinfo import ZoneInfo

dt_input = input("Enter the date and time (YYYY-mm-dd HH:MM:SS): ")
from_tz = input("Enter your current timezone (e.g., Asia/Kolkata): ")
to_tz = input("Enter the target timezone (e.g., America/New_York): ")

naive_dt = datetime.strptime(dt_input, "%Y-%m-%d %H:%M:%S")

aware_dt = naive_dt.replace(tzinfo=ZoneInfo(from_tz))

converted_dt = aware_dt.astimezone(ZoneInfo(to_tz))

print(f"\nOriginal time ({from_tz}): {aware_dt}")
print(f"Converted time ({to_tz}): {converted_dt}")

#5-task  

from datetime import datetime
import time
import sys

target_input = input("Enter future date and time (YYYY-mm-dd HH:MM:SS): ")
target_time = datetime.strptime(target_input, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    remaining = target_time - now

    if remaining.total_seconds() <= 0:
        print("\n Time's up!")
        break

    total_seconds = int(remaining.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    sys.stdout.write(f"\rTime remaining: {hours:02d}:{minutes:02d}:{seconds:02d}")
    sys.stdout.flush()
    time.sleep(1)

#6-task

import re

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = input("Enter an email address to validate: ")
if re.match(pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")

#7-task

import re

num=input('Enter the number: ')
pattern=re.sub(r'\D','',num)
formatted=f'({pattern[:3]}) {pattern[3:6]}-{pattern[6:]}'
print(f'The number you wrote: {num} \nFormatted version is: {formatted}') 

#8-task

#8-task
import re

password=input('Enter the password: ')
length=len(password)>=8
lower=re.search(r'[a-z]',password)
upper=re.search(r'[A-Z]',password)
digit=re.search(r'\d',password)
if lower and upper and digit:
    print('Your password is strong')
else:
    print('Your password is weak,so you should make:')
    if not length:
        print('At least 8 characters')
    if not lower:
        print('At least one lowercase letter')
    if not upper:
        print('At least one uppercase letter')
    if not digit:
        print('At least one digit')

#9-task

import re

text='Hello everybody, welcome to the party'
word=input('Enter the word to search: ')
found_word=re.search(word,text)
if found_word:
    print(f'Found word: \'{word}\' on {found_word.span()} order')
else:
    print(f'The word \'{word}\' you`re searching is not found. Enter other word.')

#10-task

import re

def find_dates(text):
    patterns=r'\b\d{1,2}/\d{1,2}/\d{4}\b|\b\d{4}/\d{1,2}/\d{1,2}\b|\b\d{4}-\d{1,2}-\d{1,2}\b|\b\d{1,2}-\d{1,2}-\d{4}\b|\b[Jan|Feb|Mar|Apr|May|Jun|July|Aug|Sep|Oct|Nov|Dec]\s+\d{1,2}\s+\d{4}\b'
    matches=re.findall(patterns,text)
    return matches

input_text=input('Enter the text to extract dates: ')
dates=find_dates(input_text)
if dates:
    print('Dates found: \n')
    for date in dates:
        print(f'{date}')

else:
    print('No dates found in your text') 




