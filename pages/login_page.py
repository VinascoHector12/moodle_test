from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.my_account_page import MyAccountPage

class LoginPage(BasePage):
  user_name_field = (By.ID, "username")
  password_field = (By.ID, "password")
  login_button = (By.ID, "loginbtn")
  warning_message = (By.ID, "loginerrormessage")

  def __init__(self, driver):
    super().__init__(driver)

  def set_username(self, username):
    self.set(self.user_name_field, username)
    # self.driver.find_element(self.username_field).send_keys(username)

  def set_password(self, password):
    self.set(self.password_field, password)

  def click_login_button(self):
    self.click(self.login_button)
    return MyAccountPage(self.driver)

  def log_into_application(self, username, password):
    self.set_username(username)
    self.set_password(password)
    self.click_login_button()

  def get_warning_message(self):
    return self.get_text(self.warning_message)
