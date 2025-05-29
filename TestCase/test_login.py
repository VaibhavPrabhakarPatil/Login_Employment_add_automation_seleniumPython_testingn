import time
from PageObjects.LoginPage import Login
from PageObjects.Dashboard import dashboard
from Utilities.logger import logclass

class TestLogin(logclass):
    def test_001(self,setup):
        log = self.getthelogs()
        self.driver = setup
        lg = Login(self.driver)
        db = dashboard(self.driver)
        self.driver.implicitly_wait(30)
        log.info("Test Case 001")
        log.info("Test Case Starting")
        lg.input_username("Admin")
        log.info("entered username")
        lg.input_password("admin123")
        log.info("entered password")
        lg.click_login()
        log.info("clicked login")
        try:
            if 'Dashboard' in db.welcomemsg():
                assert True
                log.info("Test Case Pass")
            else:
                log.critical("Test Case Failed")
                assert False
        except:
            print("Error element not found within timeout.")
            assert False
        self.driver.quit()

    def test_002(self, setup):
        log = self.getthelogs()
        self.driver = setup
        lg = Login(self.driver)
        self.driver.implicitly_wait(30)
        log.info("Test Case 002 - Starting")
        lg.input_username("Amin")
        log.info("Entered wrong username")
        lg.input_password("admin123")
        log.info("Entered password")
        lg.click_login()
        log.info("Clicked login")
        try:
            if 'Invalid credentials' in lg.invalid_msg():
                assert True
                log.info("Test Case 002 - Pass")
            else:
                log.critical("Test Case 002 - Failed")
                assert False
        except:
            log.error("Test Case 002 - Error: Element not found within timeout.")
            assert False
        self.driver.quit()

    def test_003(self, setup):
        log = self.getthelogs()
        self.driver = setup
        lg = Login(self.driver)
        self.driver.implicitly_wait(30)
        log.info("Test Case 003 - Starting")
        lg.input_username("Admin")
        log.info("Entered username")
        lg.input_password("admin")
        log.info("Entered wrong password")
        lg.click_login()
        log.info("Clicked login")
        try:
            if 'Invalid credentials' in lg.invalid_msg():
                assert True
                log.info("Test Case 003 - Pass")
            else:
                log.critical("Test Case 003 - Failed")
                assert False
        except:
            log.error("Test Case 003 - Error: Element not found within timeout.")
            assert False
        self.driver.quit()

