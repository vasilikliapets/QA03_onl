import json
import requests
from pprint import pprint


# получаем список авторов
def get_authors():
    response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Authors')
    print(response)
    pprint(response.text)


# получаем автора по конкретному айди
def get_author_by_id():
    response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Authors/2')
    print(response)
    pprint(response.text)


# добавляем новую книгу
def post_new_book():
    new_book = {
        "id": 0,
        "title": "string",
        "description": "string",
        "pageCount": 0,
        "excerpt": "string",
        "publishDate": "2022-01-12T12:43:44.950Z"
    }
    response = requests.post('https://fakerestapi.azurewebsites.net/api/v1/Books', json=new_book)
    print(response)
    pprint(response.text)


# добавляем нового пользователя
def post_new_user():
    new_user = {
        "id": 0,
        "userName": "string",
        "password": "string"
    }
    response = requests.post('https://fakerestapi.azurewebsites.net/api/v1/Users', json=new_user)
    print(response)
    pprint(response.text)


# обновляем данные для книги под номером 10
def put_new_data():
    new_data = {
        "id": 10,
        "title": "Mu-Mu",
        "description": "Man is killing the dog",
        "pageCount": 15,
        "excerpt": "bla-bla",
        "publishDate": "2022-01-12T12:43:44.950Z"
    }
    response = requests.put('https://fakerestapi.azurewebsites.net/api/v1/Books/10', json=new_data)
    print(response)
    pprint(response.text)


# удаляем пользователя под номером 4
def delete_user4():
    response = requests.delete('https://fakerestapi.azurewebsites.net/api/v1/Users/4')
    print(response)


# get_authors()
# get_author_by_id()
# put_new_data()
# post_new_user()
# post_new_book()
# delete_user4()