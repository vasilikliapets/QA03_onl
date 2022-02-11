import requests
import json

host = 'https://petstore.swagger.io/v2/pet'


def test_add_pet():
    global host
    add_pet = requests.post(host,
                            json={
                                "id": 0,
                                "category": {
                                    "id": 0,
                                    "name": "string"
                                },
                                "name": "doggie",
                                "photoUrls": [
                                    "string"
                                ],
                                "tags": [
                                    {
                                        "id": 0,
                                        "name": "string"
                                    }
                                ],
                                "status": "available"
                            })
    assert add_pet.status_code == 200, 'Error adding pet'

    pet_id = json.loads(add_pet.content)['id']
    get_pet_by_id = requests.get(f'{host}/{pet_id}')
    assert get_pet_by_id.status_code == 200, 'Error getting pet'

    delete_pet = requests.delete(f'{host}/{pet_id}')
    assert delete_pet.status_code == 200, 'Error deleting pet'

    get_pet_after_delete = requests.get(f'{host}/{pet_id}')
    # В API ошибка: при попытке получить удаленный элемент - возвращается случайный элемент
    if get_pet_after_delete.status_code == 200:
        assert json.loads(get_pet_after_delete.content)['id'] != pet_id
    assert get_pet_after_delete.status_code == 404
