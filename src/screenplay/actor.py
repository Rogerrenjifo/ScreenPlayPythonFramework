class Actor:
    def __init__(self, name) -> None:
        self.name = name
        self.abilities = []
        self.ordered_cleanup_tasks = []
        self.independent_cleanup_tasks = []

    def __repr__(self) -> str:
        return self.name

    def who_can(self, *abilities):
        self.abilities.extend(abilities)
        return self

    def uses_ability_to(self, ability):
        for a in self.abilities:
            if isinstance(a, ability):
                return a
            return None

    def attempts_to(self, *actions) -> None:
        for action in actions:
            self.perform(action)

    def perform(self, action) -> None:
        """Perform an Action."""
        action.perform_as(self)
