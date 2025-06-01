#Lesson-10

#1-task
class Task:
    def __init__(self,title,description,due_date,status):
        self.title=title
        self.description=description
        self.due_date=due_date
        self.status=status

class ToDoList:
    def __init__(self):
        self.tasks={}

    def add_task(self,task: Task):
        if task.title in self.tasks:
            print('Task already exists')
        else:
            self.tasks[task.title]=task
            print(f'{task.title} is added to ToDoList')

    def mark_task(self,title):
        if title in self.tasks:
            self.tasks[title].status='Complete'
            print(f'{title} marked as complete')
        else:
            print('Task not found')
            

            
    def incomplete_tasks(self):
        print('Incomplete tasks:')
        for task in self.tasks.values():
            if task.status!='Complete':
                print(f'{task.title}: (Due:{task.due_date})-{task.status}')


    def display(self):
        if not self.tasks:
            print('There is no any task')
            return
        for task in self.tasks.values():
            print(f'{task.title}: {task.description} (Due:{task.due_date})-{task.status}')
            

def menu():
        print('\nToDoList menu: ')
        print('1. See the list of tasks')
        print('2. Add a new task')
        print('3. Mark as complete')
        print('4. See incomplete tasks')
        print('5. Show Menu')
        print('6. Exit')

def main():
    todolist=ToDoList()
    
    task1 = Task("Buy groceries", "Milk, eggs, bread, and fruits", "2025-06-05", "Pending")
    task2 = Task("Finish project report", "Complete and email the report", "2025-06-03", "In Progress")
    task3 = Task("Book dentist appointment", "Call and schedule for next week", "2025-06-07", "Pending")
    task4 = Task("Clean the garage", "Organize tools and remove old items", "2025-06-10", "Not Started")

    todolist.add_task(task1)
    todolist.add_task(task2)
    todolist.add_task(task3)
    todolist.add_task(task4)

  

    while True:
        menu()
        choice=input('Enter your choice(0-6): ')

        if choice=='1':
            print('\nList of tasks: ')
            todolist.display()

        elif choice == '2':
            title = input('Enter task title: ')
            description = input('Enter task description: ')
            due_date = input('Enter due date (YYYY-MM-DD): ')
            status = input('Enter status (Pending/In Progress/Not Started): ')
            new_task = Task(title, description, due_date, status)
            todolist.add_task(new_task)

        elif choice == '3':
            title = input('Enter the title of the task to mark as complete: ')
            todolist.mark_task(title)

        elif choice=='4':
            print('\nIncomplete tasks: ')
            todolist.incomplete_tasks()

        elif choice=='5':
            menu()

        elif choice=='6':
            print('\nExiting program. Goodbye!!!')
            break
        else:
            print('\nInvalid choice. Please choose (1-6)')

if __name__=="__main__":
    main()
                
#2-task
from datetime import datetime

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()

    def __str__(self):
        return f'"{self.title}" by {self.author} on {self.created_at.strftime("%Y-%m-%d %H:%M:%S")}\n{self.content}'


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post: Post):
        self.posts.append(post)
        print(f'Post "{post.title}" added.')

    def list_posts(self):
        if not self.posts:
            print("No posts available.")
            return
        print("All Posts:")
        for i, post in enumerate(self.posts, 1):
            print(f"{i}. {post.title} by {post.author}")

    def posts_by_author(self, author):
        filtered = [p for p in self.posts if p.author.lower() == author.lower()]
        if not filtered:
            print(f"No posts found by author: {author}")
            return
        print(f"Posts by {author}:")
        for post in filtered:
            print(post)
            print("-" * 40)

    def delete_post(self, title):
        for i, post in enumerate(self.posts):
            if post.title.lower() == title.lower():
                del self.posts[i]
                print(f'Post "{title}" deleted.')
                return
        print(f'Post "{title}" not found.')

    def edit_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                print(f'Editing post "{title}" (leave blank to keep current):')
                new_title = input("New title: ").strip()
                new_content = input("New content: ").strip()
                new_author = input("New author: ").strip()
                if new_title:
                    post.title = new_title
                if new_content:
                    post.content = new_content
                if new_author:
                    post.author = new_author
                print(f'Post "{title}" updated.')
                return
        print(f'Post "{title}" not found.')

    def latest_posts(self, count=5):
        if not self.posts:
            print("No posts available.")
            return
        sorted_posts = sorted(self.posts, key=lambda p: p.created_at, reverse=True)
        print(f"Latest {count} posts:")
        for post in sorted_posts[:count]:
            print(post)
            print("-" * 40)


def menu():
    print("\nBlog System Menu:")
    print("1. List all posts")
    print("2. Add a new post")
    print("3. Display posts by author")
    print("4. Delete a post")
    print("5. Edit a post")
    print("6. Show latest posts")
    print("7. Exit")


def main():
    blog = Blog()

    while True:
        menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == '1':
            blog.list_posts()

        elif choice == '2':
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)

        elif choice == '3':
            author = input("Enter author name to filter: ")
            blog.posts_by_author(author)

        elif choice == '4':
            title = input("Enter the title of the post to delete: ")
            blog.delete_post(title)

        elif choice == '5':
            title = input("Enter the title of the post to edit: ")
            blog.edit_post(title)

        elif choice == '6':
            blog.latest_posts()

        elif choice == '7':
            print("Exiting Blog System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()

#3-task
class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self.balance += amount
        print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print("Insufficient funds. Overdraft not allowed.")
            return False
        self.balance -= amount
        print(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}")
        return True

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: {self.balance:.2f}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account: Account):
        if account.account_number in self.accounts:
            print("Account number already exists.")
            return False
        self.accounts[account.account_number] = account
        print(f"Account {account.account_number} added successfully.")
        return True

    def find_account(self, account_number):
        return self.accounts.get(account_number, None)

    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            print(f"Balance for account {account_number}: {account.balance:.2f}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def transfer(self, from_acc_num, to_acc_num, amount):
        from_account = self.find_account(from_acc_num)
        to_account = self.find_account(to_acc_num)
        if not from_account:
            print(f"Source account {from_acc_num} not found.")
            return
        if not to_account:
            print(f"Destination account {to_acc_num} not found.")
            return
        if from_account.withdraw(amount):
            to_account.deposit(amount)
            print(f"Transferred {amount:.2f} from {from_acc_num} to {to_acc_num}.")

    def display_account(self, account_number):
        account = self.find_account(account_number)
        if account:
            account.display()
        else:
            print("Account not found.")


def menu():
    print("""
Simple Banking System Menu:
1. Add new account
2. Check balance
3. Deposit money
4. Withdraw money
5. Transfer money
6. Display account details
7. Exit
""")


def main():
    bank = Bank()

    while True:
        menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            acc_num = input("Enter account number: ").strip()
            holder = input("Enter account holder name: ").strip()
            try:
                initial_balance = float(input("Enter initial balance: "))
            except ValueError:
                print("Invalid balance amount.")
                continue
            account = Account(acc_num, holder, initial_balance)
            bank.add_account(account)

        elif choice == '2':
            acc_num = input("Enter account number to check balance: ").strip()
            bank.check_balance(acc_num)

        elif choice == '3':
            acc_num = input("Enter account number to deposit money: ").strip()
            try:
                amount = float(input("Enter amount to deposit: "))
            except ValueError:
                print("Invalid amount.")
                continue
            bank.deposit(acc_num, amount)

        elif choice == '4':
            acc_num = input("Enter account number to withdraw money: ").strip()
            try:
                amount = float(input("Enter amount to withdraw: "))
            except ValueError:
                print("Invalid amount.")
                continue
            bank.withdraw(acc_num, amount)

        elif choice == '5':
            from_acc = input("Enter source account number: ").strip()
            to_acc = input("Enter destination account number: ").strip()
            try:
                amount = float(input("Enter amount to transfer: "))
            except ValueError:
                print("Invalid amount.")
                continue
            bank.transfer(from_acc, to_acc, amount)

        elif choice == '6':
            acc_num = input("Enter account number to display details: ").strip()
            bank.display_account(acc_num)

        elif choice == '7':
            print("Thank you for using the Simple Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()
