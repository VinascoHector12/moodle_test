from selenium.webdriver.common.by import By

class CourseLocatorFields:
  course_options = (By.ID, "opciones_cursos")
  new_course_field = (By.XPATH, "//div[@class='dropdown-menu dropdown-menu-right show']//a[text()='Nuevo curso']")
  full_name_field = (By.ID, "id_fullname")
  short_name_field = (By.ID, "id_shortname")
  save_button = (By.ID, "id_saveanddisplay")

  
  