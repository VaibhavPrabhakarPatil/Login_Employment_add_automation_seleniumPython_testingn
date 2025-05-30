import time
from PageObjects.Dashboard import dashboard
from PageObjects.LoginPage import Login
from PageObjects.EmploymentStatusPage import EmploymentStatus
from Utilities.random_status import status_generator
from Utilities.logger import logclass
import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")
class TestLogin(logclass):
    def test_001(self,setup):
        self.driver = setup
        log = self.getthelogs()
        lg = Login(self.driver)
        db = dashboard(self.driver)
        emp = EmploymentStatus(self.driver)
        log.info("Test Case 001, TO test the add button in employment status page")
        log.info("Test case started")
        self.driver.implicitly_wait(30)
        lg.input_username(config.get("credential","correct_username"))
        lg.input_password(config.get("credential","correct_password"))
        lg.click_login()
        log.info("Login Successful")
        db.click_admin()
        log.info("Click On Admin")
        time.sleep(5)
        db.click_job()
        log.info("Click On job")
        db.click_employment_status()
        log.info("Click On Employment_Status")
        Old_record = 0
        for i in emp.total_record():
            Old_record = Old_record + 1
        log.info("old status count save")
        emp.click_add_status()
        log.info("clicked add status")
        emp.input_name(status_generator())
        log.info("Add New status")
        emp.click_save()
        log.info("Click on save status")
        time.sleep(5)
        New_record = 0
        for j in emp.total_record():
            New_record = New_record + 1
        log.info("New status count save")
        if Old_record + 1 == New_record:
            assert True
            log.info("Test case Passed, Add functionality in working fine")
        else:
            self.driver.save_screenshot("Screenshots\\Addbutton_001.png")
            log.error("Test case Failed")
            assert False
        self.driver.quit()
