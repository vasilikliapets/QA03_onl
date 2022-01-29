"""
https://fakerestapi.azurewebsites.net/index.html
GET:
Получение списка авторов
Получение конкретного автора по его id
"""
import requests
from pprint import pprint

# GET
# Получение авторов
response_get = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Authors')
pprint(response_get.text)

# Получение автора по ID
response_get2 = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Authors/2')
print(response_get2.text)

# POST
# 1)Добавить новую книгу
book1 = {
    "id": 12345,
    "title": "MyBook",
    "description": "My_Life",
    "pageCount": 99,
    "excerpt": "Python",
    "publishDate": "1999-01-01T15:03:05.600Z"
}
add_book = requests.post('https://fakerestapi.azurewebsites.net/api/v1/Books', json=book1)
print(add_book)  # Проверяем тип запроса/Response [200]
print(add_book.text)  # Проверяем наши данные

# 2) Добавить нового пользователя
user1 = {
    "id": 556677,
    "idBook": 1234567890,
    "firstName": "Andry",
    "lastName": "Python"
}
add_user = requests.post('https://fakerestapi.azurewebsites.net/api/v1/Users', json=user1)
print(add_user)  # Проверяем тип запроса/Response [200]
print(add_user.text)  # Проверяем наши данные



# PUT
# Обновить данные для книги под номером 10
new_book_10 = {
  "id": 11111,
  "title": "UpdateBook",
  "description": "UpdateBook",
  "pageCount": 111,
  "excerpt": "MyExcerpt",
  "publishDate": "2022-01-14T20:59:30.038Z"
}

update_book_10 = requests.put('https://fakerestapi.azurewebsites.net/api/v1/Books/10', json=new_book_10)
print(update_book_10)
print(update_book_10.text)


# DEL
# Удалить пользователя под номером 4
del_user_4 = requests.delete('https://fakerestapi.azurewebsites.net/api/v1/Users/4')
print(del_user_4)
