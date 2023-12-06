from selenium.webdriver import Edge


class UseTheBrowser:
    def __init__(self) -> None:
        self.driver = Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def get_driver(self):
        return self.driver
