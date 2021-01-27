import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    #preparar el entorno para la prueba, carga los recursos o acciones necesarias
    # def setUp(self):
    #     self.driver = webdriver.Chrome(executable_path = r'./chromedriver')
    #     driver = self.driver
    #     driver.implicitly_wait(10)

    #para que se abran en una nueva ventana
    #se cambia todos los self y se le pone el decorador

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        driver = cls.driver
        driver.implicitly_wait(20)

    #siempre deben ir con test al inicio
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://platzi.com/')

    def test_jeisons_page(self):
        driver = self.driver
        driver.get('https://github.com/')
        
    # cerrar ventana del navegador
    # def tearDown(self):
    #     self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes',report_name='hello_world_report'))