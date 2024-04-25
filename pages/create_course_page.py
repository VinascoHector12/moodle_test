from pages.base_page import BasePage
from pages.my_account_page import MyAccountPage
from selenium.webdriver.common.by import By
import time

class CreateCoursesPage(BasePage):

  course_options = (By.ID, "opciones_cursos")
  new_course_field = (By.XPATH, "//div[@class='dropdown-menu dropdown-menu-right show']//a[text()='Nuevo curso']")
  full_name_field = (By.ID, "id_fullname")
  short_name_field = (By.ID, "id_shortname")
  save_button = (By.ID, "id_saveanddisplay")
  error_fullname_message = (By.ID, "id_error_fullname")
  error_shortname_message = (By.ID, "id_error_shortname")

  def __init__(self, driver):
    super().__init__(driver)

  def go_to_course_module(self):
    base_page = BasePage(self.driver)
    base_page.click_my_courses()
    time.sleep(1)
    self.click(self.course_options)
    self.click(self.new_course_field)
    return MyAccountPage(self.driver)

  def create_course(self, full_name, short_name):
    self.set(self.full_name_field, full_name)
    time.sleep(1)
    self.set(self.short_name_field, short_name)
    time.sleep(1)
    self.click(self.save_button)
    return MyAccountPage(self.driver)

  def get_confirmation_error_fullname_message(self):
    return self.get_text(self.error_fullname_message)
  
  def get_confirmation_error_shortname_message(self):
    return self.get_text(self.error_shortname_message)