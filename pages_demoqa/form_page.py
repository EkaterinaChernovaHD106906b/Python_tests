import os
import time

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from locators_demoqa import form_page_locators
from locators_demoqa.form_page_locators import FormPageLocators
from pages_demoqa.base_page import BasePage


class FormPage(BasePage):
    def fill_fields_and_submit(self):
        person = generated_person()
        path = generated_file()
        first_name = 'Joe'
        last_name = 'Week'
        email = 'joe_week@mail.com'
        self.remove_footer()
        self.element_is_visible(FormPageLocators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(FormPageLocators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(FormPageLocators.EMAIL).send_keys(person.email)
        self.element_is_visible(FormPageLocators.GENDER).click()
        self.element_is_visible(FormPageLocators.MOBILE).send_keys(person.mobile)
        subject = self.element_is_visible(FormPageLocators.SUBJECTS)
        subject.send_keys(person.subject)
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(FormPageLocators.HOBBIES).click()
        self.element_is_visible(FormPageLocators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(FormPageLocators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(FormPageLocators.SUBMIT).click()
        return person


    def form_result(self):
        result_list = self.elements_are_visible(FormPageLocators.RESULT_TABLE)
        result_list = [i.text for i in result_list]
        return result_list

