from selenium.webdriver.support.ui import WebDriverWait
from src.screenplay.abilities.UseTheBrowser import UseTheBrowser


class Verify:
    def __init__(self, question, resolution) -> None:
        self.question = question
        self.resolution = resolution

    @classmethod
    def the(cls, question, resolution):
        return cls(question, resolution)

    def perform_as(self, the_actor):
        value = self.question.answered_by(the_actor)
        driver = the_actor.uses_ability_to(UseTheBrowser).get_driver()
        condition = self.resolution.resolve()
        wait = WebDriverWait(driver, 10)
        wait.until(condition(value))
