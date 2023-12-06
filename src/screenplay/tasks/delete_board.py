from src.locators.trello_delete_page import *
from src.screenplay.actions import Click


class DeleteBoard:

    def perform_as(self, the_actor):
        the_actor.attempts_to(Click.on(HORIZONTAL_MENU_BUTTON))
        the_actor.attempts_to(Click.on(CLOSE_BOARD_BUTTON))
        the_actor.attempts_to(Click.on(CONFIRM_CLOSE_BUTTON))
        the_actor.attempts_to(Click.on(PERMANENTLY_DELETE_BUTTON))
        the_actor.attempts_to(Click.on(CONFIRM_DELETE_BUTTON))
