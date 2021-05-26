from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self): # Проверяем кликабельность
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) # *MainPageLocators.LOGIN_LINK указываем, что селектор для теста находится в locators
        login_link.click()                                                   #  символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать

    def should_be_login_link(self): # Проверяем наличие
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Ссылка на вход не обнаружена"