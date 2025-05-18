#Lesson-5

#1-task
def is_leap(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        print(f'Yes, {year} is a leap year')
        
    else:
        print(f'No, {year} is not a leap year')
year=int(input('Enter the year:'))
is_leap(year)

#2-task
n=int(input('Enter the n between 1 and 100:'))
if n%2==1:
    print('Weird')
elif n%2==0 and 2<=n<=5:
    print('Not Weird')
elif n%2==0 and 6<=n<=20:
    print('Weird')
elif n%2==0 and n>20:
    print('Not Weird')

#3-task

#Solution1

def even_numbers(a,b):
    if b>a:
        if a%2!=0:
            a+=1
    elif a>b:
        return []
    return [a]+even_numbers(a+2,b)

    
a=int(input('Enter starting value:'))
b=int(input('Enter ending value:'))
print(even_numbers(a,b))

#Solution2
a=int(input('Enter starting value:'))
b=int(input('Enter ending value:'))

start=a+(a%2)
start, end= sorted((start,b))
evens=list(range(start,end+1,2))
print(evens)




















