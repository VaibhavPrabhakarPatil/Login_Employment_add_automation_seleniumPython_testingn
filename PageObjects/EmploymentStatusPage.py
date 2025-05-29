from selenium.webdriver.common.by import By
class EmploymentStatus:
    def __init__(self,driver):
        self.driver = driver
        self.button_add_status_xpath = "//button[normalize-space()='Add']"
        self.textbox_input_name_xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
        self.total_record_xpath = "//div[@class='orangehrm-paper-container']//div[@class='oxd-table-card']"
        self.button_save_xpath = "//button[normalize-space()='Save']"

    def click_add_status(self):
        add_btn = self.driver.find_element(By.XPATH, self.button_add_status_xpath)
        add_btn.click()
    def input_name(self,Name):
        self.driver.find_element(By.XPATH,self.textbox_input_name_xpath).send_keys(Name)
    def click_save(self):
        save_btn = self.driver.find_element(By.XPATH,  self.button_save_xpath)
        save_btn.click()
    def total_record(self):
        return self.driver.find_elements(By.XPATH,self.total_record_xpath)