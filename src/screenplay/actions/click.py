from selenium.webdriver.common.by import By
from src.screenplay.abilities.UseTheBrowser import UseTheBrowser


class Click:
    def __init__(self, locator) -> None:
        self.locator = locator

    @classmethod
    def on(cls, locator):
        return cls(locator=locator)

    def perform_as(self, the_actor) -> None:
        browser = the_actor.uses_ability_to(UseTheBrowser).get_driver()
        strategy, locator = self.locator
        element = browser.find_element(strategy, locator)
        element.click()
