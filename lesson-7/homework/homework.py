#Lesson-7

#1-task

def isPrime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input('Enter n:'))
print(isPrime(n))

#2-task

def digit_sum(k):

a=int(input())
numbers=[]
b=str(a)
for i in b:
    numbers.append(int(i))
print(sum(numbers))

#3-task
def powers(b):
    for i in range(1,b+1):
        s=2**i
        if b>=s:
            print(s)
b=int(input())
powers(b)
