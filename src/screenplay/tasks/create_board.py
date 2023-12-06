from src.locators.trello_home_page import (
    CREATE_BOARD_BUTTON,
    BOARD_TITLE_TEXTBOX,
    CREATE_BUTTON,
    CREATE_BOARD_SUBMIT_BUTTON,
)
from src.screenplay.actions import Click, Write


class CreateBoard:
    def __init__(self, board_name) -> None:
        self.board_name = board_name

    @classmethod
    def called(cls, board_name):
        return cls(board_name=board_name)

    def perform_as(self, the_actor):
        the_actor.attempts_to(Click.on(CREATE_BUTTON))
        the_actor.attempts_to(Click.on(CREATE_BOARD_BUTTON))
        the_actor.attempts_to(
            Write.the_text(self.board_name).into_the(BOARD_TITLE_TEXTBOX)
        )
        the_actor.attempts_to(Click.on(CREATE_BOARD_SUBMIT_BUTTON))
