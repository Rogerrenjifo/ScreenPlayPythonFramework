# from selenium.webdriver import Edge
from selenium.webdriver import Remote
from selenium.webdriver import EdgeOptions


class UseTheBrowser:
    def __init__(self) -> None:
        remote_url = "http://localhost:4444/wd/hub"
        self.driver = Remote(command_executor=remote_url, options=EdgeOptions())
        # self.driver = Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(50)

    def get_driver(self):
        return self.driver
