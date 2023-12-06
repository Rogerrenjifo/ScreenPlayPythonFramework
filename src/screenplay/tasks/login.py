from src.locators.login_page import USERNAME_TEXTBOX,PASSWORD_TEXTBOX, CONTINUE_BUTTON, LOGIN_BUTTON
from src.locators.trello_home_page import TRELLO_LOGIN_BUTTON
from src.screenplay.actions import Click, Write


class Login:
    def __init__(self, username) -> None:
        self.username = username
        self.password = ""

    @classmethod
    def with_username(cls, username):
        return cls(username=username)

    def and_password(self, password):
        self.password = password
        return self

    def perform_as(self, the_actor):
        the_actor.attempts_to(Click.on(TRELLO_LOGIN_BUTTON))
        the_actor.attempts_to(Write.the_text(self.username).into_the(USERNAME_TEXTBOX))
        the_actor.attempts_to(Click.on(CONTINUE_BUTTON))
        the_actor.attempts_to(Write.the_text(self.password).into_the(PASSWORD_TEXTBOX))
        the_actor.attempts_to(Click.on(LOGIN_BUTTON))
