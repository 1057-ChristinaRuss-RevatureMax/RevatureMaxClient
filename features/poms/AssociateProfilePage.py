from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


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

    def login(self, email):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'submit')))
        self.driver.find_element_by_id('username').send_keys(email)
        self.driver.find_element_by_id('password').send_keys('password')
        self.driver.find_element_by_id('submit').click()

    def get_associate_info(self):
        self.wait.until(EC.text_to_be_present_in_element((By.ID, self.preference_id), 'Indifferent'))
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

    def click_edit_fav_technologies(self):
        self.driver.find_element_by_id(self.edit_fav_technologies_id).click()

    def input_fav_technologies(self, tech1, tech2, tech3):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.submit_fav_technologies_id)))
        while self.driver.find_element_by_id(self.edit_tech1_id).get_attribute("value") != tech1:
            self.driver.find_element_by_id(self.edit_tech1_id).clear()
            self.driver.find_element_by_id(self.edit_tech1_id).send_keys(tech1)
        while self.driver.find_element_by_id(self.edit_tech2_id).get_attribute("value") != tech2:
            self.driver.find_element_by_id(self.edit_tech2_id).clear()
            self.driver.find_element_by_id(self.edit_tech2_id).send_keys(tech2)
        while self.driver.find_element_by_id(self.edit_tech3_id).get_attribute("value") != tech3:
            self.driver.find_element_by_id(self.edit_tech3_id).clear()
            self.driver.find_element_by_id(self.edit_tech3_id).send_keys(tech3)

    def select_preference(self, preference):
        while self.driver.find_element_by_id(self.edit_preference_id).get_attribute("value") != preference:
            selectPreference = self.driver.find_element_by_id(self.edit_preference_id)
            for option in selectPreference.find_elements_by_tag_name('option'):
                if option.text == preference:
                    option.click()

    def submit_fav_technologies(self):
        self.driver.find_element_by_id(self.submit_fav_technologies_id).click()

    def get_fav_technologies(self):
        self.wait.until(EC.text_to_be_present_in_element((By.ID, self.tech3_id), '3'))
        results = [self.driver.find_element_by_id(self.tech1_id).text,
                   self.driver.find_element_by_id(self.tech2_id).text,
                   self.driver.find_element_by_id(self.tech3_id).text,
                   self.driver.find_element_by_id(self.preference_id).text]
        return results

    def reset_info(self):
        result = self.get_contact_info()
        while not (result[0] == 'Mock 17' and result[1] == 'Associate 17' and result[2] == 'mock17.associate5471ee3e-7e48-4d27-b277-e5579017f87f@mock.com'):
            self.click_edit_contact_info()
            self.input_contact_info('Mock 17', 'Associate 17', 'mock17.associate5471ee3e-7e48-4d27-b277-e5579017f87f@mock.com')
            self.submit_contact_info()
            result = self.get_contact_info()
        result = self.get_bio()
        while result != 'some stuff about me':
            self.click_edit_bio()
            self.input_bio('some stuff about me')
            self.submit_bio()
            result = self.get_bio()
        result = self.get_fav_technologies()
        while not (result[0] == 'example 1' and result[1] == 'example 2' and result[2] == 'example 3' and result[3] == 'Indifferent'):
            self.click_edit_fav_technologies()
            self.input_fav_technologies('example 1', 'example 2', 'example 3')
            self.select_preference('Indifferent')
            self.submit_fav_technologies()
            result = self.get_fav_technologies()
