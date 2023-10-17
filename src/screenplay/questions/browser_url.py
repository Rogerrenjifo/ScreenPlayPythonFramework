from screenplay.abilities.UseTheBrowser import UseTheBrowser


class BrowserUrl:
    def answered_by(self, the_actor) -> str:
        browser = the_actor.uses_ability_to(UseTheBrowser).get_driver()
        url = browser.current_url
        return url
