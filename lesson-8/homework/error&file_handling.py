#Lesson 8

#1-task
try:
    1/0
except ZeroDivisionError:
    print('There is ZeroDivisionError')

#2-task
try:
    value=int(input('Enter a value:'))
except ValueError:
    raise ValueError('Please enter a valid value')

#3-task
try:
    myfile=open('myfile.txt')
except FileNotFoundError:
    print('File not found')

#4-task
try:
    number=int(input('enter the number:'))
except ValueError:
    print('your number is not numerical')

#5-task
try:
    myfile=open('myfile.txt')
except PermissionError:
    print('you have no permission to open this file')

#6-task
mylist=[1,2,3,4,5]
try:
    index=int(input('enter an index(0-4):'))
    print(f'element at index {index}: {mylist[index]}')
except IndexError:
    print('Wrong choise. Please, choose between 0-4')

#7-task
try:
    number=int(input('enter the number:'))
except KeyboardInterrupt:
    print('you cancelled the input')

#8-task
try:
    a,b=map(int, input('Enter two numbers to divide(a/b):').split())
    a/b

except ArithmeticError:
    print('There is an arithmetical error')

#9-task
try:
    myfile=open('myfile.txt')
except UnicodeDecodeError:
    print('there is an encoding issue')

#10-task
try:
    mylist=[1,2,3,4,5]
    mylist.push(6)
except AttributeError as e:
    print('That  attribute does not exist')

File Input/Output exercises

#1-task
myfile=open('myfile.txt','r')

#2-task
n=int(input('enter the number of lines:'))
with open('myfile.txt', 'r',) as file:
            print(f"First {n} line(s) of the file:\n")
            for i in range(n):
                line = file.readline()
                if not line:
                    break
                print(line, end='')

#3-task
with open('myfile.txt','a') as file:
    text=input('write text to append:')
    myfile.write(text)
    print('Appended!!!.Now the text is\n')

with open('myfile.txt','r') as file:
    myfile.read()

#4-task
with open('myfile.txt','r') as file:
    file.seek(0,2)
    file.read()

#5-task
lines=[]
with open('myfile.txt','r') as file:
    for line in file:
        lines.append(line.rstrip('\n'))
return lines

#6-task
with open(file_path, 'r') as file:
      return [line.rstrip('\n') for line in file]

#7-task
with open('myfile.txt','r') as file:
array=[line.strip() for line in file]
return array

#8-task
with open('myfile.txt','r') as file:
    for i in file:
        a=max(len(i))
    print(a)

#9-task
with open('myfile.txt','r') as file:
    lines=file.readlines()
    print(len(lines))

#10-task
with open('filename.txt') as f:
    words = f.read().split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)

#11-task
with open('myfile.txt','r') as file:
    file.seek(0,2)
    size=file.tell()
    print(size)
 
#12-task
mylist=['hello','hi']
with open('myfile.txt','w') as file:
    for item in mylist:
        file.write(item+'\n')

#13-task
with open('myfile1.txt','r') as file1, open('myfile2.txt','w') as file2:
    for line in file1:
        file2.write(line)

#14-task
with open('myfile1.txt','r') as file1, open('myfile2.txt','w') as file2:
    for line1,line2 in added(file1,file2):
        file2.write(line1+' '+line2)

#15-task
with open('filename.txt') as f:
    lines = f.readlines()

import random
print(random.choice(lines).strip())

#16-task
f=open('myfile.txt')
print(f.closed)
print('the file is not closed')
f.close()
print(f.closed)
print('the file is now closed')

#17-task
with open('input.txt', 'r') as f:
    content = f.read().replace('\n', '')

with open('input.txt', 'w') as f:
    f.write(content)

#18-task
filename = input("Enter the filename: ")
with open(filename, 'r') as f:
    text = f.read()
for ch in ",.;:!?":
    text = text.replace(ch, ' ')
words = text.split()
print("Number of words:", len(words))

#19-task
filenames = ['file1.txt', 'file2.txt', 'file3.txt']  # list your files here

chars = []
for fname in filenames:
    with open(fname, 'r') as f:
        chars.extend(f.read())

print(chars)

#20-task
for i in range(26):
    filename = chr(65 + i) + '.txt' 
    with open(filename, 'w') as f:
        pass  

#21-task
letters_per_line = int(input("Enter number of letters per line: "))

with open('alphabet.txt', 'w') as f:
    for i in range(26):
        f.write(chr(65 + i))
        if (i + 1) % letters_per_line == 0:
            f.write('\n')
    if 26 % letters_per_line != 0:
        f.write('\n')






