import selenium
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from features.poms.AssociateProfilePage import AssociateProfilePage

current_email = 'mock17.associate5471ee3e-7e48-4d27-b277-e5579017f87f@mock.com'


@given('the user is signed in as an associate')
def log_in_as_associate(context):
    context.driver.get('http://localhost:9001/')
    context.current_page = AssociateProfilePage(context.driver)
    context.current_page.login(current_email)


@given('the user is on the associate profile page')
def on_associate_profile_page(context):
    context.driver.get('http://localhost:9001/associateprofile')
    context.current_page = AssociateProfilePage(context.driver)


@given('the associates info is reset')
def reset_info(context):
    context.current_page.reset_info()
    global current_email
    current_email = 'mock17.associate5471ee3e-7e48-4d27-b277-e5579017f87f@mock.com'


@when('the user clicks the edit contact info button')
def click_edit_contact_info(context):
    context.current_page.click_edit_contact_info()


@when('the user inputs new contact info')
def input_contact_info(context):
    context.current_page.input_contact_info('Joe', 'Tester', 'joe@test.com')
    global current_email
    current_email = 'joe@test.com'


@when('the user clicks the submit contact info button')
def click_submit_contact_info(context):
    context.current_page.submit_contact_info()


@when('the user clicks the edit bio button')
def click_edit_bio(context):
    context.current_page.click_edit_bio()


@when('the user inputs a new bio')
def input_bio(context):
    context.current_page.input_bio('some new stuff about me')


@when('the user clicks the submit bio button')
def click_submit_bio(context):
    context.current_page.submit_bio()


@when('the user clicks the edit fav technologies button')
def click_edit_fav_technologies(context):
    context.current_page.click_edit_fav_technologies()


@when('the user inputs new favorite technologies')
def input_fav_technologies(context):
    context.current_page.input_fav_technologies('test 1', 'test 2', 'test 3')


@when('the user selects a new preference')
def select_preference(context):
    context.current_page.select_preference('Backend')


@when('the user clicks the submit fav technologies button')
def click_submit_fav_technologies(context):
    context.current_page.submit_fav_technologies()


@then('the associate can view their profile information')
def test_view_associate_info(context):
    results = context.current_page.get_associate_info()
    assert results[0] == 'Mock 17'
    assert results[1] == 'Associate 17'
    assert results[2] == 'mock17.associate5471ee3e-7e48-4d27-b277-e5579017f87f@mock.com'
    assert results[3] == 'some stuff about me'
    assert results[4] == 'example 1'
    assert results[5] == 'example 2'
    assert results[6] == 'example 3'
    assert results[7] == 'Indifferent'


@then('the contact info is updated')
def test_contact_info_updated(context):
    results = context.current_page.get_contact_info()
    assert results[0] == 'Joe'
    assert results[1] == 'Tester'
    assert results[2] == 'joe@test.com'


@then('the bio is updated')
def test_bio_updated(context):
    assert context.current_page.get_bio() == 'some new stuff about me'


@then('the favorite technologies are updated')
def test_fav_technologies_updated(context):
    results = context.current_page.get_fav_technologies()
    assert results[0] == 'test 1'
    assert results[1] == 'test 2'
    assert results[2] == 'test 3'
    assert results[3] == 'Backend'

    # reset the info for next time
    context.current_page.reset_info()
