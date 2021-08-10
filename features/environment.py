from selenium import webdriver
from poms.AssociateProfilePage import AssociateProfilePage


def before_scenario(context, scenario):
    # we will start each test by opening a new browser window
    context.driver = webdriver.Chrome()


def after_scenario(context, scenario):
    # we will end each test by closing our browser window
    context.driver.quit()
