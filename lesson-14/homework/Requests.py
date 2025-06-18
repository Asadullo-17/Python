#1-task
import json

with open('students.json','r') as f:
    students=json.load(f)

for student in students:
    print('Students:')
    for key, value in student.items():
        print(f'{key}:{value}')

#2-task


import requests

api_key='3e23r43r'
city='Tashkent'
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
data = response.json()
temperature = data['main']['temp']
humidity = data['main']['humidity']
weather = data['weather'][0]['description']
if response.status_code==200:    
    print(f'Weather: {city}')
    print(f'Temperature: {temperature}')
    print(f'Humidity: {humidity}')
    print(f'Condition : {weather}')
else:
    print('Failed to get data:',response.status_code)


#3-task

import json

def load_books():
    with open('books.json','r') as f:
        return json.load(f)

    
def save_books(books):
    with open('books.json','w') as f:
        return json.dump(books,f)
    
def add_book():
    title=input('Enter the title of the book to add: ')
    books=load_books()
    if title in books:
        print(f'The book {title} already exists. Try again')
    else:
        books.append(title)
        print('Book added successfully.\n')  

def update_books():
    books=load_books()
    title=input('Enter the title of the book to update: ')
    for book in books:
        if book['title'].lower()==title.lower():
            book[f'author']=input("Enter new author(current: {book['author']}")
            save_books(books)
            print('Book updated successfully\n')
            return
    print('Book not found\n')

def delete_book():
    books=load_books()
    title=input('Enter the title of the book to delete: ')
    new_books=[book for book in books if book['title'].lower()!=title.lower()]
    if len(new_books)<len(books):
        save_books(new_books)
        print('Book deleted successfully\n')
    else:
        print('Book not found')

def menu():
    while True:
        print('Menu:')
        print('1. Add new books')
        print('2. Update existing book')
        print('3. Delete books')
        print('4. Menu')
        choice=int(input('Enter the number(1-4): '))
        if choice==1:
            add_book()
        elif choice==2:
            update_books()
        elif choice==3:
            delete_book()
        elif choice==4:
            menu()
        else:
            print('Wrong choice. Please choose a number between 1 and 4')


if __name__=='__main__':
    menu()


#4-task

import requests
import random

api_key = 'fba21dc0'
url = 'http://www.omdbapi.com/'

sample_titles = [
    "Inception", "The Matrix", "Titanic", "The Godfather", "Pulp Fiction",
    "Forrest Gump", "The Dark Knight", "Fight Club", "Interstellar", "Gladiator"
]

genre = input('Enter the genre of the movie: ').strip().lower()

movies = []

for title in sample_titles:
    response = requests.get(url, params={'t': title, 'apikey': api_key})
    if response.status_code == 200:
        data = response.json()
        if 'Genre' in data:
            genres = [g.strip().lower() for g in data['Genre'].split(',')]
            if genre in genres:
                movies.append(data)

if movies:
    random_movie = random.choice(movies)
    print(f"\n🎬 Recommended Movie: {random_movie['Title']}")
else:
    print("❌ No movies found for that genre.")

