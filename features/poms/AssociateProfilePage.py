from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AssociateProfilePage:
    first_name_id = 'userFirstName'
    last_name_id = 'userLastName'
    email_id = 'userEmail'
    edit_contact_info_id = 'editContactInfo'
    edit_first_name_id = 'editFirstName'
    edit_last_name_id = 'editLastName'
    edit_email_id = 'editEmail'
    submit_contact_info_id = 'submitContactInfo'
    bio_id = 'userBio'
    edit_bio_id = 'editBio'
    new_bio_id = 'newBio'
    submit_bio_id = 'submitBio'
    tech1_id = 'tech1'
    tech2_id = 'tech2'
    tech3_id = 'tech3'
    preference_id = 'userPreference'
    edit_fav_technologies_id = 'editFavTechnologies'
    edit_tech1_id = 'editTech1'
    edit_tech2_id = 'editTech2'
    edit_tech3_id = 'editTech3'
    edit_preference_id = 'editPreference'
    new_preference_id = 'indifferent'
    submit_fav_technologies_id = 'submitFavTechnologies'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_associate_info(self):
        self.wait.until(EC.text_to_be_present_in_element((By.ID, self.first_name_id), 'example'))
        results = [self.driver.find_element_by_id(self.first_name_id).text,
                   self.driver.find_element_by_id(self.last_name_id).text,
                   self.driver.find_element_by_id(self.email_id).text,
                   self.driver.find_element_by_id(self.bio_id).text,
                   self.driver.find_element_by_id(self.tech1_id).text,
                   self.driver.find_element_by_id(self.tech2_id).text,
                   self.driver.find_element_by_id(self.tech3_id).text,
                   self.driver.find_element_by_id(self.preference_id).text]
        return results

    def click_edit_contact_info(self):
        self.driver.find_element_by_id(self.edit_contact_info_id).click()

    def input_contact_info(self, inputValue):
        self.wait.until(EC.text_to_be_present_in_element_value((By.ID, self.edit_first_name_id), 'name'))
        self.driver.find_element_by_id(self.edit_first_name_id).clear()
        self.driver.find_element_by_id(self.edit_first_name_id).send_keys(inputValue)
        self.driver.find_element_by_id(self.edit_last_name_id).clear()
        self.driver.find_element_by_id(self.edit_last_name_id).send_keys(inputValue)
        self.driver.find_element_by_id(self.edit_email_id).clear()
        self.driver.find_element_by_id(self.edit_email_id).send_keys(inputValue + '@email')

    def submit_contact_info(self):
        self.driver.find_element_by_id(self.submit_contact_info_id).click()

    def get_contact_info(self):
        self.wait.until(EC.text_to_be_present_in_element((By.ID, self.email_id), 'test'))
        results = [self.driver.find_element_by_id(self.first_name_id).text,
                   self.driver.find_element_by_id(self.last_name_id).text,
                   self.driver.find_element_by_id(self.email_id).text]
        return results

    def click_edit_bio(self):
        self.driver.find_element_by_id(self.edit_bio_id).click()

    def input_bio(self, inputValue):
        self.wait.until(EC.text_to_be_present_in_element_value((By.ID, self.new_bio_id), 'stuff'))
        self.driver.find_element_by_id(self.new_bio_id).clear()
        self.driver.find_element_by_id(self.new_bio_id).send_keys(inputValue)

    def submit_bio(self):
        self.driver.find_element_by_id(self.submit_bio_id).click()

    def get_bio(self):
        self.wait.until(EC.text_to_be_present_in_element((By.ID, self.bio_id), 'test'))
        result = self.driver.find_element_by_id(self.bio_id).text
        return result

    def click_edit_fav_technologies(self):
        self.driver.find_element_by_id(self.edit_fav_technologies_id).click()

    def input_fav_technologies(self, inputValue):
        self.wait.until(EC.text_to_be_present_in_element_value((By.ID, self.edit_tech1_id), 'example'))
        self.driver.find_element_by_id(self.edit_tech1_id).clear()
        self.driver.find_element_by_id(self.edit_tech1_id).send_keys(inputValue + '1')
        self.driver.find_element_by_id(self.edit_tech2_id).clear()
        self.driver.find_element_by_id(self.edit_tech2_id).send_keys(inputValue + '2')
        self.driver.find_element_by_id(self.edit_tech3_id).clear()
        self.driver.find_element_by_id(self.edit_tech3_id).send_keys(inputValue + '3')

    def select_preference(self):
        self.driver.find_element_by_id(self.edit_preference_id).click()
        self.driver.find_element_by_id(self.new_preference_id).click()

    def submit_fav_technologies(self):
        self.driver.find_element_by_id(self.submit_fav_technologies_id).click()

    def get_fav_technologies(self):
        self.wait.until(EC.text_to_be_present_in_element((By.ID, self.tech1_id), 'test'))
        results = [self.driver.find_element_by_id(self.tech1_id).text,
                   self.driver.find_element_by_id(self.tech2_id).text,
                   self.driver.find_element_by_id(self.tech3_id).text,
                   self.driver.find_element_by_id(self.preference_id).text]
        return results
