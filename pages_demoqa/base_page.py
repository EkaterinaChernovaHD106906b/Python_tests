from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_all_elements_located(locator))

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('fixedban').style.display='none'")



