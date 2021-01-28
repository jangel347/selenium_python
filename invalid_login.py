import unittest
from selenium import webdriver


class InvalidLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')

    def test_invalid_login(self):
        driver = self.driver
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()

        email_field = driver.find_element_by_id('email')
        password_field = driver.find_element_by_id('pass')
        button_submit = driver.find_element_by_xpath('//*[@id="send2"]')

        self.assertTrue(email_field.is_enabled()
                        and password_field.is_enabled()
                        and button_submit.is_enabled())
        
        email_field.send_keys('nn@pruebajeison.com.co')
        password_field.send_keys('j0fc3asz4sdf61')
        button_submit.click()

        self.assertTrue(driver.find_element_by_class_name('error-msg').is_displayed())
        
        
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main(verbosity=2)