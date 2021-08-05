from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TrainerProfilePage:
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
    specialization_id = 'userSpecialization'
    location_id = 'userLocation'
    edit_training_info_id = 'editTrainingInfo'
    edit_specialization_id = 'editUserSpecialization'
    edit_location_id = 'editUserLocation'
    submit_training_info_id = 'submitTrainingInfo'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_trainer_info(self):
        self.wait.until(EC.text_to_be_present_in_element((By.ID, self.first_name_id), 'trainer'))
        results = [self.driver.find_element_by_id(self.first_name_id).text,
                   self.driver.find_element_by_id(self.last_name_id).text,
                   self.driver.find_element_by_id(self.email_id).text,
                   self.driver.find_element_by_id(self.bio_id).text,
                   self.driver.find_element_by_id(self.specialization_id).text,
                   self.driver.find_element_by_id(self.location_id).text]
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

    def click_edit_training_info(self):
        self.driver.find_element_by_id(self.edit_training_info_id).click()

    def input_specialization(self, inputValue):
        self.wait.until(EC.text_to_be_present_in_element_value((By.ID, self.edit_specialization_id), 'w/'))
        self.driver.find_element_by_id(self.edit_specialization_id).clear()
        self.driver.find_element_by_id(self.edit_specialization_id).send_keys(inputValue)

    def input_location(self, inputValue):
        self.wait.until(EC.text_to_be_present_in_element_value((By.ID, self.edit_location_id), 'Ohio'))
        self.driver.find_element_by_id(self.edit_location_id).clear()
        self.driver.find_element_by_id(self.edit_location_id).send_keys(inputValue)

    def submit_training_info(self):
        self.driver.find_element_by_id(self.submit_training_info_id).click()

    def get_training_info(self):
        self.wait.until(EC.text_to_be_present_in_element((By.ID, self.specialization_id), 'test'))
        results = [self.driver.find_element_by_id(self.specialization_id).text,
                   self.driver.find_element_by_id(self.location_id).text]
        return results
