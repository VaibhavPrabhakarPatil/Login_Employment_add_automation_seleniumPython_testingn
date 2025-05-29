import time
from PageObjects.Dashboard import dashboard
from PageObjects.LoginPage import Login
from PageObjects.EmploymentStatusPage import EmploymentStatus
class TestLogin:
    def test_001(self,setup):
        self.driver = setup
        lg = Login(self.driver)
        db = dashboard(self.driver)
        emp = EmploymentStatus(self.driver)
        self.driver.implicitly_wait(30)
        lg.input_username("Admin")
        lg.input_password("admin123")
        lg.click_login()
        db.click_admin()
        time.sleep(5)
        db.click_job()
        db.click_employment_status()
        Old_record = 0
        for i in emp.total_record():
            Old_record = Old_record + 1
        print(Old_record)
        emp.click_add_status()
        emp.input_name("Testing start")
        emp.click_save()
        time.sleep(5)
        New_record = 0
        for j in emp.total_record():
            New_record = New_record + 1
        print(New_record)
        if Old_record + 1 == New_record:
            assert True
        else:
            assert False