
from c2_cms.Page.login_page import LoginPage

class TestLogin:
    def setup_class(self):
        self.brower = LoginPage()



    def test_login(self):
        self.brower.login()