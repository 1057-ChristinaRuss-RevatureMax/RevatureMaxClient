
######################################################################
#these tests auto generated with svw.py (salt, vinegar, & water) -JJC#
######################################################################

from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

#Scenario #1: An associate wants to view their dashboard

@given("the associate is on the associate dashboard")
def step_the_associate_is_on_the_associate_dashboard(context):
	context.driver.get(context.associate_dashboard_url)
	assert "associate-dashboard" in context.driver.current_url


@then("the page shows at least the table header")
def step_the_page_shows_at_least_the_table_header(context):
	element = WebDriverWait(context.driver, 5, 1).until(lambda x: '<th>' in context.driver.page_source)
	assert len(context.driver.find_element_by_id("stat_table_head").find_elements(By.TAG_NAME, 'th')) > 0

