import time


def test_add_to_basket_button(browser):
    browser.get(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(20)
    button = len(browser.find_elements_by_class_name(
        "btn.btn-lg.btn-primary.btn-add-to-basket"))
    assert button > 0, 'Отсутствует кнопка "Добавить в корзину"'
