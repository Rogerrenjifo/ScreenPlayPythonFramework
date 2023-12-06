from src.screenplay.abilities import UseTheBrowser


class Write:
    def __init__(self, text) -> None:
        self.text = text
        self.target = None
        self.locator = None
    @classmethod
    def the_text(cls, text: str):
        return cls(text=text)

    def into_the(self, locator):
        self.locator = locator
        return self

    def perform_as(self, the_actor) -> None:
        browser = the_actor.uses_ability_to(UseTheBrowser).get_driver()
        strategy, locator = self.locator
        element = browser.find_element(strategy, locator)
        element.send_keys(self.text)
