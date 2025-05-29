from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class dashboard:
    def __init__(self,driver):
        self.driver = driver
        self.text_welcome_xpath = "//h6[normalize-space()='Dashboard']"
        self.button_admin_xpath = "//span[normalize-space()='Admin']"
        self.button_job_xpath = "//span[normalize-space()='Job']"
        self.button_Employment_status_xpath = "//a[normalize-space()='Employment Status']"
    def welcomemsg(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located((By.XPATH, self.text_welcome_xpath))).text

    def click_admin(self):
        self.driver.find_element(By.XPATH, self.button_admin_xpath).click()

    def click_job(self):
        self.driver.find_element(By.XPATH, self.button_job_xpath).click()

    def click_employment_status(self):
        self.driver.find_element(By.XPATH, self.button_Employment_status_xpath).click()
