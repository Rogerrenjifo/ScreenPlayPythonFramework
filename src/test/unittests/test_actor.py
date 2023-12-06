import unittest


from unittest.mock import MagicMock
from src.screenplay.actor import Actor

class TestActor(unittest.TestCase):

    def test_actor_initialization(self):
        actor = Actor("John")
        self.assertEqual(actor.name, "John")
        self.assertEqual(actor.abilities, [])
        self.assertEqual(actor.ordered_cleanup_tasks, [])
        self.assertEqual(actor.independent_cleanup_tasks, [])

    def test_who_can(self):
        actor = Actor("John")
        actor.who_can("sing")
        self.assertEqual(actor.abilities, ["sing"])

    def test_attempts_to(self):
        actor = Actor("John")
        action_mock = MagicMock()
        actor.attempts_to(action_mock)
        action_mock.perform_as.assert_called_once_with(actor)


if __name__ == '__main__':
    unittest.main()
