from test_data.data import *
from screenplay.abilities import UseTheBrowser
from screenplay.actions import Click, Write, Navigate, Verify
from screenplay.resolutions import IsVisible
from screenplay.questions import Element
from screenplay.actor import Actor
from locators.login_page import (
    USERNAME_TEXTBOX,
    PASSWORD_TEXTBOX,
    CONTINUE_BUTTON,
    LOGIN_BUTTON,
)
from locators.trello_delete_page import (
    HORIZONTAL_MENU_BUTTON,
    CLOSE_BOARD_BUTTON,
    CONFIRM_CLOSE_BUTTON,
    PERMANENTLY_DELETE_BUTTON,
    CONFIRM_DELETE_BUTTON,
    BOARD_DELETED_MESSAGE,
    BOARD_NAME_TEXTBOX,
)
from locators.trello_home_page import (
    CREATE_BOARD_BUTTON,
    CREATE_BUTTON,
    CREATE_BOARD_SUBMIT_BUTTON,
    TRELLO_LOGIN_BUTTON,
    USER_BUTTON,
    BOARD_TITLE_TEXTBOX,
)
from dotenv import load_dotenv


load_dotenv()


# Create the actor
Roger = Actor("Roger")

# Add new ability Use the browser
Roger.who_can(UseTheBrowser())

# Perform actions to login
Roger.attempts_to(Navigate.to(TRELLO_HOME_PAGE))
Roger.attempts_to(Click.on(TRELLO_LOGIN_BUTTON))
Roger.attempts_to(Write.the_text(USERNAME).into_the(USERNAME_TEXTBOX))
Roger.attempts_to(Click.on(CONTINUE_BUTTON))
Roger.attempts_to(Write.the_text(PASSWORD).into_the(PASSWORD_TEXTBOX))
Roger.attempts_to(Click.on(LOGIN_BUTTON))

# Verify the element user button is visible
Roger.attempts_to(Verify(Element(USER_BUTTON), IsVisible()))

# perform actions Create a new Board
Roger.attempts_to(Click.on(CREATE_BUTTON))
Roger.attempts_to(Click.on(CREATE_BOARD_BUTTON))
Roger.attempts_to(Write.the_text(BOARD_NAME).into_the(BOARD_TITLE_TEXTBOX))
Roger.attempts_to(Click.on(CREATE_BOARD_SUBMIT_BUTTON))

# Verify the name of the board is visible
Roger.attempts_to(Verify(Element(BOARD_NAME_TEXTBOX), IsVisible()))

# Perform actions to delete the board
Roger.attempts_to(Click.on(HORIZONTAL_MENU_BUTTON))
Roger.attempts_to(Click.on(CLOSE_BOARD_BUTTON))
Roger.attempts_to(Click.on(CONFIRM_CLOSE_BUTTON))
Roger.attempts_to(Click.on(PERMANENTLY_DELETE_BUTTON))
Roger.attempts_to(Click.on(CONFIRM_DELETE_BUTTON))

# Verify the Board deleted message is displayed
Roger.attempts_to(Verify(Element(BOARD_DELETED_MESSAGE), IsVisible()))

print("Finished")
