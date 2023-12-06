from selenium.webdriver.common.action_chains import ActionChains
from src.screenplay.abilities.UseTheBrowser import UseTheBrowser


class Move:
    def __init__(self, source_locator) -> None:
        self.source_locator = source_locator
        self.target_locator = None

    @classmethod
    def the(cls, source_locator):
        return cls(source_locator=source_locator)

    def into(self, target_locator):
        self.target_locator = target_locator
        return self

    def perform_as(self, the_actor) -> None:
        browser = the_actor.uses_ability_to(UseTheBrowser).get_driver()

        source_strategy, source_locator = self.source_locator
        source_element = browser.find_element(source_strategy, source_locator)
        target_strategy, target_locator = self.target_locator
        target_element = browser.find_element(target_strategy, target_locator)

        action_chains = ActionChains(browser)
        action_chains.move_to_element(source_element).move_by_offset(-3, -3).perform()
        action_chains.click_and_hold(source_element).move_to_element(target_element).perform()
