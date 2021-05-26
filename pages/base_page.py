from selenium.common.exceptions import NoSuchElementException # Импортировали исключение(сообщение об ошибке) при получении которого получаем ошибку


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what): # Прописали, что при получении "Такого" исключения выдавать ошибку см. main_page
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
