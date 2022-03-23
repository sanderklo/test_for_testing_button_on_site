link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_for_adding_product_to_cart(browser):
    browser.get(link)
    button = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert button.is_displayed(), "Button add to cart, not displayed on web site"
