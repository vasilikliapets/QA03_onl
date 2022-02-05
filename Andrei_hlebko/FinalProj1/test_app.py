from FinalProj1.db_steps import create_group, get_group_name
from FinalProj1.pages.main_page import MainPage


def test_group(driver, connect_to_db):
    create_group(connect_to_db)
    page = MainPage(driver)
    page.open()
    login_page = page.open_login_page()
    admin_page = login_page.try_to_login()
    admin_groups = admin_page.open_groups()
    assert 'Group_1' in admin_groups.get_first_group().text


def test_change_group_name(driver, connect_to_db):
    page = MainPage(driver)
    page.open()
    admin_page = page.open_admin_page()
    admin_groups = admin_page.open_groups()
    change_group = admin_groups.open_change_group()
    name_field = change_group.get_group_name_field()
    name_field.send_keys('_changed')
    change_group.click_save_btn()
    get_group_name(connect_to_db)
    assert "Group_1_changed" in connect_to_db.fetchall()[0]
