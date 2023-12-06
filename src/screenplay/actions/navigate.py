from src.screenplay.abilities.UseTheBrowser import UseTheBrowser


class Navigate:
    def __init__(self, url) -> None:
        self.url = url

    @classmethod
    def to(cls, url: str):
        return cls(url=url)

    def perform_as(self, the_actor) -> None:
        browser = the_actor.uses_ability_to(UseTheBrowser).get_driver()
        browser.get(self.url)
