from eugene_shurpach.diploma.tools.constants import HOST_PET, PET_ID
from eugene_shurpach.diploma.tools.api_steps import add_pet, get_pet_by_id, delete_pet, get_content
import allure


@allure.story("Check add, get and delete pet")
def test_add_pet():
    with allure.step("Add new pet"):
        add_new_pet = add_pet(HOST_PET, {"id": PET_ID, "name": "test_pet"})
        assert add_new_pet.status_code == 200, 'Error adding pet'
    with allure.step('Get pet by ID'):
        get_my_pet = get_pet_by_id(HOST_PET, PET_ID)
        assert get_content(get_my_pet)['id'] == PET_ID, 'Error getting pet'
    with allure.step('Delete pet'):
        delete_my_pet = delete_pet(HOST_PET, PET_ID)
        assert delete_my_pet.status_code == 200, 'Error deleting pet'
    with allure.step('Check pet does not exist'):
        get_my_pet_after_del = get_pet_by_id(HOST_PET, PET_ID)
        assert get_my_pet_after_del.status_code == 404
