import requests

requests.get('https://fakerestapi.azurewebsites.net/api/v1/Authors')  # Получение всех авторов
author_id = 1
requests.get(f'https://fakerestapi.azurewebsites.net/api/v1/Authors/{author_id}')  # Получение атора по id

# Запрос POST с телом в формате json
requests.post('https://fakerestapi.azurewebsites.net/api/v1/Books',
              json={"id": 1,"title": "Название","description": "Описание","pageCount": 200,"excerpt": "Выписка","publishDate": "2022-01-17T20:08:06.351Z"}
              )
requests.post('https://fakerestapi.azurewebsites.net/api/v1/Users',
              json={
  "id": 1,
  "userName": "shurpach",
  "password": "Admin123"
}
              )

requests.get('https://fakerestapi.azurewebsites.net/api/v1/Books/10',
             json={
  "id": 10,
  "title": "Измененное название",
  "description": "Описание",
  "pageCount": 350,
  "excerpt": "Выписка",
  "publishDate": "2022-01-17T20:20:24.490Z"
}
             )


# Удаление пользователя с id=4
requests.delete('https://fakerestapi.azurewebsites.net/api/v1/Users/4')
