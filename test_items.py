from selenium.webdriver.common.by import By


def test_guest_should_see_login_link(browser):
    browser.get(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    element = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
    assert element, 'Not found'