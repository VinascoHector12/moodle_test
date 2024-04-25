from pages.base_page import BasePage
from pages.create_course_page import CreateCoursesPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.test_data import TestData

class TestCreateCourse(BaseTest):
  def test_create_course(self):
    #Inicialmente inicia sesión el usuario
    login_page = LoginPage(self.driver)
    login_page.set_username(TestData.username)
    login_page.set_password(TestData.password)
    login_page.click_login_button()

    #Una vez ingresa se dirige al modulo de cursos 
    base_page = BasePage(self.driver)   
    course_page = CreateCoursesPage(self.driver)
    course_page.go_to_course_module()
    course_page.create_course(TestData.courseFullName, TestData.courseShortName)
    base_page.click_menu_item("home")
    actual_title = course_page.get_title()
    assert actual_title == "Página Principal | Test"

  # def test_invalid_credentials(self):
  #   login_page = LoginPage(self.driver)
  #   login_page.log_into_application("Invalid Email", "Invalid Password")
  #   actual_message = login_page.get_warning_message()
  #   assert actual_message.__contains__("Acceso inválido. Por favor, inténtelo otra vez.")