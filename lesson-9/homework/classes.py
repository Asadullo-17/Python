#Lesson-9

#1-task
class Circle:
    def __init__(self,radius):
        self.pi=3.14
        self.radius=radius


    def area(self):
        s=self.pi*self.radius**2
        print(f'Circle`s area is {s}')

    def perimeter(self):
        p=2*self.pi*self.radius
        print(f'Circle`s perimeter is {p}')

ex1=Circle(12)
ex1.area()
ex1.perimeter()

#2-task
from datetime import datetime
class Person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
    def get_age(self):
        age=datetime.today().year-self.dob
        return age
p1=Person('Komiljon','Uzbekistan',2006)
print(f'{p1.name}`s age is {p1.get_age()}')

#3-task
class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        s=self.num1+self.num2
        print(f'{self.num1}+{self.num2}= {s}')
    def subtract(self):
        s=self.num1-self.num2
        print(f'{self.num1}-{self.num2}= {s}')
    def multiply(self):
        s=self.num1*self.num2
        print(f'{self.num1}*{self.num2}= {s}')
    def divide(self):
        s=self.num1/self.num2
        print(f'{self.num1}/{self.num2}= {s}')

e1=Calculator(45,24)
e1.add()
e1.subtract()
e1.multiply()
e1.divide()

#4-task
class Shape:
    def __init__(self,shape):
        self.shape=shape
class Circle(Shape):
    def __init__(self,radius):
        self.pi=3.14
        self.radius=radius
        
    def circle_area(self):
        s=self.pi*self.radius**2
        print(f'Circle`s area is {s}')

    def circle_perimeter(self):
        p=2*self.pi*self.radius
        print(f'Circle`s perimeter is {p}')

class Triangle(Shape):
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
  
    def triangle_area(self):
        import math
        if self.side1+self.side2>self.side3 and self.side2+self.side3>self.side1 and self.side1+self.side3>self.side2:
            p=(self.side1+self.side2+self.side3)/2
            area=math.sqrt(p*(p-self.side1)*(p-self.side2)*(p-self.side3))
            print(f'Triangle`s area is {area}')
        else:
            print('invalid')

    def triangle_perimeter(self):
        p=self.side1+self.side2+self.side3
        print(f'Triangle`s perimeter is {p}')

class Square(Shape):
    def __init__(self,side):
        self.side=side

    def square_area(self):
        area=self.side**2
        print(f'Square`s area is {area}')

    def square_perimeter(self):
        p=self.side*4
        print(f'Square`s perimeter is {p}')

e1=Shape(Circle)
e1=Circle(5)
e1.circle_area()
e1.circle_perimeter()
e2=Shape(Triangle)
e2=Triangle(3,4,5)
e2.triangle_area()
e2.triangle_perimeter()
e3=Shape(Square)
e3=Square(5)
e3.square_area()
e3.square_perimeter()

#5-task
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
    
        def _insert(current, value):
            if current is None:
                return Node(value)
            if value < current.value:
                current.left = _insert(current.left, value)
            elif value > current.value:
                current.right = _insert(current.right, value)
            return current

        self.root = _insert(self.root, value)

    def search(self, value):
        
        def _search(current, value):
            if current is None:
                return False
            if current.value == value:
                return True
            elif value < current.value:
                return _search(current.left, value)
            else:
                return _search(current.right, value)

        return _search(self.root, value)


bst = BinarySearchTree()
elements = [50, 30, 70, 20, 40, 60, 80]

for el in elements:
    bst.insert(el)

print("Search 60:", bst.search(60))  
print("Search 25:", bst.search(25))  

#6-task
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        item = self.items.pop()
        print(f"Popped: {item}")
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack (top → bottom):", list(reversed(self.items)))


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

stack.pop()
stack.display()

#7-task
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Insert a new node at the end"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, key):
        """Delete the first node with given value"""
        current = self.head
        prev = None

        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"Value {key} not found in the list.")
            return

        if prev is None:
            # Deleting the head node
            self.head = current.next
        else:
            prev.next = current.next

        print(f"Deleted node with value {key}.")

    def display(self):
        """Display all node values"""
        current = self.head
        if not current:
            print("Linked list is empty.")
            return

        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()

ll.delete(20)
ll.display()

ll.delete(50) 

#8-task
class Shop:
    def __init__(self):
        self.items={}
        
    def add(self,name,price,quantity=1):
        if name in self.items:
            self.items[name][1]+=quantity
        else:
            self.items[name]=[price,quantity]
        print(f'Added {quantity} x {name} at ${price} each')

    def remove(self,name):
        if name in self.items:
            del self.items[name]
            print(f'{name} is removed from cart')
        else:
            print(f'{name} is not found from cart')

    def total(self):
        total=sum(price*quantity for price,quantity in self.items.values())
        return total

    def display_cart(self):
        if not self.items:
            print('Shopping cart is empty')
            return

        print('\nItems in cart:')
        for name,(price,quantity) in self.items.items():
            print(f'{name}:{quantity}x{price:.3f}=${price*quantity:.3f}')
        print(f'Total:${self.total():.3f}\n')

cart = Shop()
cart.add("Apple", 0.999, 4)
cart.add("Milk", 2.499, 2)
cart.display_cart()

cart.remove("Milk")
cart.display_cart()

print("Final total:", cart.total())

#9-task
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        item = self.items.pop()
        print(f"Popped: {item}")
        return item

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack (top → bottom):")
            for item in reversed(self.items):
                print(item)

    def is_empty(self):
        return len(self.items) == 0


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    stack.display()

    stack.pop()
    stack.display()

#10-task
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item) 
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.items.pop(0)  
        print(f"Dequeued: {item}")
        return item

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue (front → rear):", self.items)

    def is_empty(self):
        return len(self.items) == 0


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    queue.display()

    queue.dequeue()
    queue.display()

#11-task
class CustomerAccount:
    def __init__(self, name, account_number, balance=0.0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.name}: Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print(f"{self.name}: Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{self.name}: Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_balance(self):
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, account_number, initial_balance=0.0):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = CustomerAccount(name, account_number, initial_balance)
            print(f"Account created for {name} (#{account_number}) with balance ${initial_balance:.2f}")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def show_all_accounts(self):
        if not self.accounts:
            print("No accounts found.")
        else:
            for acc in self.accounts.values():
                print(f"{acc.name} (#{acc.account_number}): Balance = ${acc.get_balance():.2f}")


if __name__ == "__main__":
    bank = Bank()

    bank.create_account("Alice", "001", 500)
    bank.create_account("Bob", "002", 1000)

    acc1 = bank.get_account("001")
    acc1.deposit(200)
    acc1.withdraw(100)

    acc2 = bank.get_account("002")
    acc2.withdraw(1200)  

    bank.show_all_accounts()







