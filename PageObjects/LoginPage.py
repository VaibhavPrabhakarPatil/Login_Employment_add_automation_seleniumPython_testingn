from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Login:
    def __init__(self,driver):
        self.driver = driver
        self.textbox_username_name = "username"
        self.textbox_password_name = "password"
        self.button_login_xpath = "//button[@type='submit']"
        self.text_invalidmsg_xpath = "//p[contains(@class,'oxd-alert-content-text')]"

    def input_username(self,Username):
        username = self.driver.find_element(By.NAME, self.textbox_username_name )
        username.send_keys(Username)

    def input_password(self,Password):
        password = self.driver.find_element(By.NAME, self.textbox_password_name)
        password.send_keys(Password)

    def click_login(self):
        login_btn = self.driver.find_element(By.XPATH, self.button_login_xpath)
        login_btn.click()

    def invalid_msg(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located((By.XPATH,self.text_invalidmsg_xpath))).text

