#Lession-4

#Dictionaries

#1-task
my_dict = {'apple': 3, 'banana': 1, 'cherry': 5, 'date': 2}
asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))
desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Ascending:", asc_sorted)
print("Descending:", desc_sorted)

#2-task
mydict={0: 10, 1: 20}
mydict[2]=30
print(mydict)

#3-task
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {**dic1, **dic2, **dic3}
print(result)

#4-task
n=int(input('Enter n:'))
mydict={x:x*x for x in range(1,n+1)}
print(mydict)

#5-task
n=15
mydict={x:x*x for x in range(1,n+1)}
print(mydict)

#Sets

#1-task
set={1,2,3,4,5}
print(set)

#2-task
set={1,2,3,4,5}
for item in set:
    print(item)

#3-task
set={1,2,3}
set.add(4)
set.update([5,6])
print(set)

#4-task
set={1,2,3,4,5}
items_to_remove={1,2}
set.remove(5)
set.difference_update(items_to_remove)
print(set)

#5-task
set={1,2,3,4,5}
if 5 in set:
    set.remove(5)
    print(set)
