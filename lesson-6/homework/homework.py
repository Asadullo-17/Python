#Lesson-6

#1-task

def insert_underscores(txt: str) -> str:
    vowels = set('aeiouAEIOU')
    result = []
    count = 0
    i = 0
    while i < len(txt):
        ch = txt[i]
        result.append(ch)
        count += 1

        if count % 3 == 0:
            if i + 1 >= len(txt):
                break

            if ch in vowels or (i + 1 < len(txt) and txt[i + 1] == '_'):
                pass
            else:
                result.append('_')

        i += 1

    if result and result[-1] == '_':
        result.pop()

    return ''.join(result)

if __name__ == "__main__":
    test_inputs = [
        "hello",
        "assalom",
        "abcabcabcdeabcdefabcdefg",
        "abecidofu",
        "abcdefg",
    ]

    for inp in test_inputs:
        print(f"Input: {inp}")
        print(f"Output: {insert_underscores(inp)}\n")

#2-task

n=int(input('Enter n:'))
for i in range(0,n):
        print(i**2)
        

#3-task

#Exercise1

n=1
naturals=[]
while n<=10:
    naturals.append(n)
    n+=1
print(naturals)

#Exercise2

n=int(input('Enter n:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()


#Exercise3

n=int(input('Enter number:'))
s=0
for i in range(1,n+1):
    s+=i
print(f'Sum is:{s}')
    

#Exercise4

n=int(input('Enter number:'))
for i in range(1,11):
    s=n*i
    print(s)

#Exercise5

numbers = [12, 75, 150, 180, 145, 525, 50]
n=len(numbers)//2
for i in range(0,n+1):
    s=2*4*i
    if s<len(numbers):
        print(numbers[s])

#Exercise6

n=int(input('Enter number:'))
a=len(str(n))
print(a)

#Exercise7

n=int(input('Enter n:'))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j, end=' ')
    print()

#Exercise8

list1 = [10, 20, 30, 40, 50]
rev=list1[::-1]
for i in rev:
    print(i)

#Exercise9

for i in range(-10,0):
    print(i)

#Exercise10

n=int(input('Enter ending number:'))
for i in range(0,n):
    print(i)
print('Done!')

#Exercise11

def isPrime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def ranges(start,end):
    for num in range(start,end+1):
        if isPrime(num):
            print(num,end=' ')
start,end= map(int , input().split())
print('Prime numbers between {start} and {end}:')
ranges(start,end)

#Exercise12

def fibonnaci(n):
    a,b=0,1
    for i in range(n):
        print(a,end=' ')
        a,b=b,a+b
n=int(input())
fibonnaci(n)

#Exercise13

def fact(n):
    s=1
    for i in range(1,n+1):
       s=s*i
    
    print(n,'!=',s)
n=int(input())     
fact(n)

#4-task

def lists(list1, list2):
    list1_copy=list[:]
    for i in list2:
        if i in list
