from screenplay.tasks import CreateBoard, Login, DeleteBoard
from screenplay.abilities import UseTheBrowser
from screenplay.actions import Verify, Navigate
from screenplay.resolutions import IsVisible
from screenplay.questions import Element
from screenplay.actor import Actor
from test_data.data import TRELLO_HOME_PAGE, USERNAME, PASSWORD, BOARD_NAME
from locators.trello_home_page import USER_BUTTON
from locators.trello_delete_page import BOARD_DELETED_MESSAGE, BOARD_NAME_TEXTBOX


Roger = Actor("Roger")
Roger.who_can(UseTheBrowser())

Roger.attempts_to(Navigate.to(TRELLO_HOME_PAGE))
Roger.attempts_to(Login.with_username(USERNAME).and_password(PASSWORD))
Roger.attempts_to(Verify(Element(USER_BUTTON), IsVisible()))

Roger.attempts_to(CreateBoard.called(BOARD_NAME))
Roger.attempts_to(Verify(Element(BOARD_NAME_TEXTBOX), IsVisible()))

Roger.attempts_to(DeleteBoard())
Roger.attempts_to(Verify(Element(BOARD_DELETED_MESSAGE), IsVisible()))

print("Finished")
