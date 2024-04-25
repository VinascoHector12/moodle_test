from pages.base_page import BasePage
from pages.create_course_page import CreateCoursesPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.test_data import TestData
import time

class TestCreateCourse(BaseTest):
  def test_create_course(self):
    #Inicialmente inicia sesión el usuario
    login_page = LoginPage(self.driver)
    login_page.log_into_application(TestData.username, TestData.password)
    time.sleep(1)

    #Una vez ingresa se dirige al modulo de cursos  
    course_page = CreateCoursesPage(self.driver)
    course_page.go_to_course_module()
    course_page.create_course(TestData.courseFullName, TestData.courseShortName)
    actual_title = course_page.get_title()
    assert actual_title == "Curso: Tecnologia de la información | Test"

  def test_invalid_course(self):
    login_page = LoginPage(self.driver)
    login_page.log_into_application(TestData.username, TestData.password)
    course_page = CreateCoursesPage(self.driver)
    course_page.go_to_course_module()
    course_page.create_course(TestData.courseFullName, TestData.courseShortName)
    actual_title = course_page.get_title()
    assert actual_title == "Añade un curso nuevo | Test"