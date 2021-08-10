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

    def login(self, email):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'submit')))
        self.driver.find_element_by_id('username').send_keys(email)
        self.driver.find_element_by_id('password').send_keys('password')
        self.driver.find_element_by_id('submit').click()

    def get_trainer_info(self):
        self.wait.until(EC.text_to_be_present_in_element((By.ID, self.location_id), 'somewhere'))
        results = [self.driver.find_element_by_id(self.first_name_id).text,
                   self.driver.find_element_by_id(self.last_name_id).text,
                   self.driver.find_element_by_id(self.email_id).text,
                   self.driver.find_element_by_id(self.bio_id).text,
                   self.driver.find_element_by_id(self.specialization_id).text,
                   self.driver.find_element_by_id(self.location_id).text]
        return results

    def click_edit_contact_info(self):
        self.driver.find_element_by_id(self.edit_contact_info_id).click()

    def input_contact_info(self, firstName, lastName, email):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.submit_contact_info_id)))
        while self.driver.find_element_by_id(self.edit_first_name_id).get_attribute("value") != firstName:
            self.driver.find_element_by_id(self.edit_first_name_id).clear()
            self.driver.find_element_by_id(self.edit_first_name_id).send_keys(firstName)
        while self.driver.find_element_by_id(self.edit_last_name_id).get_attribute("value") != lastName:
            self.driver.find_element_by_id(self.edit_last_name_id).clear()
            self.driver.find_element_by_id(self.edit_last_name_id).send_keys(lastName)
        while self.driver.find_element_by_id(self.edit_email_id).get_attribute("value") != email:
            self.driver.find_element_by_id(self.edit_email_id).clear()
            self.driver.find_element_by_id(self.edit_email_id).send_keys(email)

    def submit_contact_info(self):
        self.driver.find_element_by_id(self.submit_contact_info_id).click()

    def get_contact_info(self):
        self.wait.until(EC.text_to_be_present_in_element((By.ID, self.email_id), '@'))
        results = [self.driver.find_element_by_id(self.first_name_id).text,
                   self.driver.find_element_by_id(self.last_name_id).text,
                   self.driver.find_element_by_id(self.email_id).text]
        return results

    def click_edit_bio(self):
        self.driver.find_element_by_id(self.edit_bio_id).click()

    def input_bio(self, bio):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.submit_bio_id)))
        while self.driver.find_element_by_id(self.new_bio_id).get_attribute("value") != bio:
            self.driver.find_element_by_id(self.new_bio_id).clear()
            self.driver.find_element_by_id(self.new_bio_id).send_keys(bio)

    def submit_bio(self):
        self.driver.find_element_by_id(self.submit_bio_id).click()

    def get_bio(self):
        self.wait.until(EC.text_to_be_present_in_element((By.ID, self.bio_id), 'stuff'))
        result = self.driver.find_element_by_id(self.bio_id).text
        return result

    def click_edit_training_info(self):
        self.driver.find_element_by_id(self.edit_training_info_id).click()

    def input_specialization(self, specialization):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.submit_training_info_id)))
        while self.driver.find_element_by_id(self.edit_specialization_id).get_attribute("value") != specialization:
            self.driver.find_element_by_id(self.edit_specialization_id).clear()
            self.driver.find_element_by_id(self.edit_specialization_id).send_keys(specialization)

    def input_location(self, location):
        while self.driver.find_element_by_id(self.edit_location_id).get_attribute("value") != location:
            self.driver.find_element_by_id(self.edit_location_id).clear()
            self.driver.find_element_by_id(self.edit_location_id).send_keys(location)

    def submit_training_info(self):
        self.driver.find_element_by_id(self.submit_training_info_id).click()

    def get_training_info(self):
        self.wait.until(EC.text_to_be_present_in_element((By.ID, self.location_id), 'somewhere'))
        results = [self.driver.find_element_by_id(self.specialization_id).text,
                   self.driver.find_element_by_id(self.location_id).text]
        return results

    def reset_info(self):
        result = self.get_contact_info()
        while not (result[0] == 'Mock 1026' and result[1] == 'Employee 1026' and result[2] == 'mock1026.employee0ced595f-c2c5-4fd9-9e69-4556edce0a6c@mock.com'):
            self.click_edit_contact_info()
            self.input_contact_info('Mock 1026', 'Employee 1026', 'mock1026.employee0ced595f-c2c5-4fd9-9e69-4556edce0a6c@mock.com')
            self.submit_contact_info()
            result = self.get_contact_info()
        result = self.get_bio()
        while result != 'some trainer stuff about me':
            self.click_edit_bio()
            self.input_bio('some trainer stuff about me')
            self.submit_bio()
            result = self.get_bio()
        result = self.get_training_info()
        while not (result[0] == 'something' and result[1] == 'somewhere'):
            self.click_edit_training_info()
            self.input_specialization('something')
            self.input_location('somewhere')
            self.submit_training_info()
            result = self.get_training_info()
