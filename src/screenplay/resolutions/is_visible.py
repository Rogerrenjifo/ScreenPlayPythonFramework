from selenium.webdriver.support import expected_conditions as EC


class IsVisible:
    def resolve(self):
        return EC.visibility_of
