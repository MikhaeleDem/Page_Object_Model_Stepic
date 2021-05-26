import time

from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):    # реализуйте проверку на корректный url адрес
        login_url = self.browser.find_element(*MainPageLocators.LOGIN_LINK) # перешли на главную страницу
        time.sleep(1)
        login_url.click() # кликнули на ссылку логина
        time.sleep(1)
        assert "login" in self.browser.current_url, "URL не содержит login"

    def should_be_login_form(self):    # реализуйте проверку, что есть форма логина
        login_url = self.browser.find_element(*MainPageLocators.LOGIN_LINK) # перешли на главную страницу
        time.sleep(1)
        login_url.click() # кликнули на ссылку логина
        time.sleep(1)
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина отсутствует"

    def should_be_register_form(self):    # реализуйте проверку, что есть форма регистрации на странице
        login_url = self.browser.find_element(*MainPageLocators.LOGIN_LINK) # перешли на главную страницу
        time.sleep(1)
        login_url.click() # кликнули на ссылку логина
        time.sleep(1)
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации отсутствует"
