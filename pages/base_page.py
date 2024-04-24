from selenium.webdriver.common.by import By

class BasePage:
   #Se inicializa la clase y se pasa el driver para manejar el navegador
  def __init__(self, driver):
    self.driver = driver

  def find(self, *locator): #* solo argumentos clave como ID
    return self.driver.find_element(*locator)
   
  def click(self, locator):
    self.find(*locator).click()
    #self.driver.find_element(*locator).click()

  def set(self, locator, value):
    self.find(*locator).clear()
    self.find(*locator).send_keys(value)

  def get_text(self, locator):
    return self.find(*locator).text
   
  def get_title(self):
    return self.driver.title

   #Este metodo nos permite buscar la opcion de cursos en el menu superior y darle click
  def click_my_courses(self):
    course_menu = By.XPATH, "//ul[@role='menubar']//li[@data-key='mycourses']//a[@role='menuitem']"  
    self.click(course_menu)

   #Este metodo nos permite buscar cualquier item en el menu superior y darle click
  def click_menu_item(self, menu_item):
    item = By.XPATH, "//ul[@role='menubar']//li[@data-key='"+menu_item+"']//a[@role='menuitem']" 
    self.click(item)

  def menu_item(self, menu_item):
    return By.XPATH, "//ul[@role='menubar']//li[@data-key='"+menu_item+"']//a[@role='menuitem']"