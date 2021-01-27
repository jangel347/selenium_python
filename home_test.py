import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HomePageTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_field_text_by_id(self):
        search_field = self.driver.find_element_by_id('search')

    def test_search_field_text_by_name(self):
        search_field = self.driver.find_element_by_name('q')

    # def test_search_field_text_by_class(self):
    #     search_field = self.driver.find_element_by_class_name('input-text')

    # def test_search_button_enabled(self):
    #     button = self.driver.find_element_by_class_name('search')
    
    # def test_count_images_promo(self):
    #     banner_list = self.driver.find_element_by_class_name('promos')
    #     banners = banner_list.find_elements_by_tag_name('img')
    #     self.assertEqual(3,len(banners))

    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[5]/ul/li[2]/a/em')

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")

    # cerrar ventana del navegador
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes',report_name='home_report'))