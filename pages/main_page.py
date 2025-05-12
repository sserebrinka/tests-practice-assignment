from locators.locators import FormsImplementation
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class MainPage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    
    def open(self):
        self.browser.get(self.url)

    def scroll_to_element(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def get_form_implementation(self, implementation):
        FORM_IMPLEMENTATION = (By.CSS_SELECTOR, f"div[data-testid='Implementation {implementation}'] input.form-control")
        return FORM_IMPLEMENTATION
    
    def fill_form_implementation(self, implementation, value):
        elem = self.browser.find_element(*self.get_form_implementation(implementation))
        self.scroll_to_element(elem)
        elem.send_keys(value)
        
    def get_validate_button(self, implementation):
        BUTTON_VALIDATE = (By.XPATH, f"(//button[text()='Validate'])[{implementation}]")
        return BUTTON_VALIDATE

    def click_validate_button(self, implementation):
        button = self.browser.find_element(*self.get_validate_button(implementation))
        self.scroll_to_element(button)
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.get_validate_button(implementation))
        )
        time.sleep(0.4)
        ActionChains(self.browser).move_to_element(button).click().perform()

    def get_validation_text(self):
        
        toast = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(FormsImplementation.TOAST_MESSAGE)
        )
        return toast.text
        
    def clear_form_implementation(self, implementation):
        self.browser.find_element(*self.get_form_implementation(implementation)).clear()
    