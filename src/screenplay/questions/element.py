from src.screenplay.abilities.UseTheBrowser import UseTheBrowser


class Element:
    def __init__(self, locator) -> None:
        self.locator = locator

    def answered_by(self, the_actor) -> str:
        browser = the_actor.uses_ability_to(UseTheBrowser).get_driver()

        strategy, locator = self.locator
        element = browser.find_element(strategy, locator)
        return element
