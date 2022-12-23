import allure

from FinalProj1.pages.http_steps import create_user, login_user, get_user_info, do_logout, del_user


@allure.story("Creation of new user")
def test_create_user():
    """
    This test checks creation of user by status code and user id
    """
    new_user = {
        "id": 666,
        "username": "User_1",
        "firstName": "Andrei",
        "lastName": "Hlebko",
        "email": "tms@tut.by",
        "password": "1234567890",
        "phone": "987654321",
        "userStatus": 0
    }
    response = create_user(new_user)
    with allure.step('Send request. Check status code'):
        assert response.status_code == 200, "Wrong status code"
    with allure.step('Check user id in response body'):
        assert '666' in response.text, 'No such user id'


@allure.story("Login new user")
def test_login_user():
    """
    This test checks user login
    """
    username = 'User_1'
    password = '1234567890'
    response = login_user(username, password)
    with allure.step('Send request. Check status code'):
        assert response.status_code == 200, "Wrong status code"
    with allure.step('Check message in response body'):
        assert 'logged in user session' in response.text, "User wasn't login"


@allure.story("Get user information")
def test_get_user_info():
    """
    This test checks user information
    """
    username = 'User_1'
    response = get_user_info(username)
    with allure.step('Send request. Check status code'):
        assert response.status_code == 200, "Wrong status code"
    with allure.step('Check user information in response body'):
        assert 'Andrei' in response.text and 'Hlebko' in response.text, "No such user information"


@allure.story("User logout")
def test_user_logout():
    """
    This test checks user logout
    """
    response = do_logout()
    with allure.step('Send request. Check status code'):
        assert response.status_code == 200, "Wrong status code"
    with allure.step('Check message in response body'):
        assert 'ok' in response.text, "User wasn't logout"


@allure.story("Delete user")
def test_del_user():
    """
    This test checks user delete
    """
    username = 'User_1'
    response = del_user(username)
    with allure.step('Send request. Check status code'):
        assert response.status_code == 200, "Wrong status code"
    with allure.step('Check the name of deleted user in response body'):
        assert 'User_1' in response.text, "User wasn't delete"
        # assert f'{username}' in response.text, "User wasn't delete" #а так пишут?что бы не дублировать в ассерте юзернэйм
