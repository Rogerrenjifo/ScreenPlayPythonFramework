from screenplay.abilities.UseTheBrowser import UseTheBrowser


class Text:
    target = ""

    @classmethod
    def of_the(cls, target):
        return cls(target=target)

    def answered_by(self, the_actor):
        browser = the_actor.ability_to(UseTheBrowser).get_driver()
        return browser.find_element(self.target).text

    def __init__(self, target) -> None:
        self.target = target
