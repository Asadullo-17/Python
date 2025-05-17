#Lesson-3

#1-task
fruits=['apple','banana','pear','cherry','pomegranate']
print(fruits[2])

#2-task
evens=[2,4,6,8]
odds=[1,3,5,7,9]
numbers=evens+odds
print(numbers)

#3-task
odds=[1,3,5,7,9]
first=odds[0]
middle=odds[len(odds)//2]
last=odds[-1]
print(first,middle,last)

#4-task
movies=['interstellar','the big','17','smth','smn']
movies1=tuple(movies)
print(movies1)

#5-task
cities=['London','Paris','Berlin','NewYork','Tashkent']
if 'Paris' in cities:
    print('Yes, Paris is in the list')
else :
    print('No, Paris is not in the list')

#6-task
evens1=[2,4,6,8]
evens2=evens1.copy()
evens=evens1+evens2
print(evens)

#7-task
cities=['London','Paris','Berlin','NewYork','Tashkent']
cities[0],cities[4]=cities[4],cities[0]
print(cities)

#8-task
numbers=tuple(range(1,10))
sliced=numbers[3:7]
print(sliced)

#9-task
colors=['red','blue','purple','yellow','blue','green']
print(colors.count('blue'))

#10-task
animals=('lion','snake','elephant','bear')
print(animals.index('bear'))

#11-task
evens=(2,4,6,8)
odds=(1,3,5,7,9)
numbers=evens+odds
print(numbers)

#12-task
list=[2,4,6,8]
tuple=(1,3,5,7,9)
print(f'length of list is:{len(list)}')
print(f'length of tuple is:{len(tuple)}')

#13-task
tuple=(1,3,5,7,9)
listed=list(tuple)
print(listed)

#14-task
numbers=tuple(range(1,10))
max=max(numbers)
min=min(numbers)
print(f'max nummber is:{max}')
print(f'min nummber is:{min}')

#15-task
animals=('lion','snake','elephant','bear')
reversed=animals[::-1]
print(reversed)
