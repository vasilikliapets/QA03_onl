from eugene_shurpach.Lesson26.homework26.tools.main_page import MainPage


def test_fiction_page(driver):
    page = MainPage(driver)
    page.open()
    fic_page = page.open_fiction_page()
    assert 'Fiction' in fic_page.get_header().text, "Title doesn't contain Fiction"