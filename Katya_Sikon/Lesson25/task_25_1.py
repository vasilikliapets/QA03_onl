import requests

main_url = 'https://fakerestapi.azurewebsites.net/'

print('Получение списка авторов')

authors = requests.get(main_url + '/api/v1/Authors')
print(authors.content)

print('\nПолучение конкретного автора по его id')

author3 = requests.get(main_url + '/api/v1/Authors/3')
print(author3.content)

print('\nДобавить новую книгу')

new_book_data = {'id': 0,
                 'title': 'Паспорт человека мира.',
                 'description': 'Истории из жизни, Книги о путешествиях',
                 'pageCount': 420,
                 'excerpt': 'string',
                 'publishDate': '2022-01-24T10:20:47.408Z'}

new_book = requests.post(main_url + '/api/v1/Books', json=new_book_data)
print(new_book.status_code)
print(new_book.content)

print('\nДобавить нового пользователя')

new_user_data = {"id": 0,
                 "userName": "KS123",
                 "password": "123Aa"
                 }

new_user = requests.post(main_url + '/api/v1/Users', json=new_user_data)
print(new_user.status_code)
print(new_user.content)

print('\nОбновить данные для книги под номером 10')

new_book10_data = {"id": 10,
                   "title": "Харпер Ли. Убить пересмешника",
                   "description": "История маленького сонного городка на юге Америки, поведанная маленькой девочкой. "
                                  "История ее брата Джима, друга Дилла и ее отца – честного, принципиального адвоката "
                                  "Аттикуса Финча, одного из последних и лучших представителей старой «южной "
                                  "аристократии». История судебного процесса по делу чернокожего парня, обвиненного в "
                                  "насилии над белой девушкой. Но прежде всего – история переломной эпохи, когда "
                                  "ксенофобия, расизм, нетерпимость и ханжество, присущие американскому югу, "
                                  "постепенно уходят в прошлое. «Ветер перемен» только-только повеял над Америкой. "
                                  "Что он принесет?..",
                   "pageCount": 350,
                   "excerpt": "",
                   "publishDate": "2022-01-14T10:43:58.4740716+00:00"
                   }

new_book10 = requests.put(main_url + '/api/v1/Books/10', json=new_book10_data)
print(new_book10.status_code)
print(new_book10.content)

print('\nУдалить пользователя под номером 4')

delete_user4 = requests.delete(main_url + '/api/v1/Users/4')
print(delete_user4.status_code)