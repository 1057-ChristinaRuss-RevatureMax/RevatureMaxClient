from behave import *

from features.poms.AssociateProfilePage import AssociateProfilePage


@given('the user is signed in as an associate')
def log_in_as_associate(context):
    pass


@given('the user is on the associate profile page')
def on_associate_profile_page(context):
    context.driver.get('file:///E:/Projects/RevatureMaxClient/associate-profile/associate-profile.html')
    context.current_page = AssociateProfilePage(context.driver)


@when('the user clicks the edit contact info button')
def click_edit_contact_info(context):
    context.current_page.click_edit_contact_info()


@when('the user inputs new contact info')
def input_contact_info(context):
    context.current_page.input_contact_info('test')


@when('the user clicks the submit contact info button')
def click_submit_contact_info(context):
    context.current_page.submit_contact_info()


@when('the user clicks the edit bio button')
def click_edit_bio(context):
    context.current_page.click_edit_bio()


@when('the user inputs a new bio')
def input_bio(context):
    context.current_page.input_bio('some test stuff')


@when('the user clicks the submit bio button')
def click_submit_bio(context):
    context.current_page.submit_bio()


@when('the user clicks the edit fav technologies button')
def click_edit_fav_technologies(context):
    context.current_page.click_edit_fav_technologies()


@when('the user inputs new favorite technologies')
def input_fav_technologies(context):
    context.current_page.input_fav_technologies('test')


@when('the user selects a new preference')
def select_preference(context):
    context.current_page.select_preference()


@when('the user clicks the submit fav technologies button')
def click_submit_fav_technologies(context):
    context.current_page.submit_fav_technologies()


@then('the associate can view their profile information')
def test_view_associate_info(context):
    results = context.current_page.get_associate_info()
    assert results[0] == 'examplefirstname'
    assert results[1] == 'examplelastname'
    assert results[2] == 'example@email.com'
    assert results[3] == 'some stuff about me'
    assert results[4] == 'example1'
    assert results[5] == 'example2'
    assert results[6] == 'example3'
    assert results[7] == 'Backend'


@then('the contact info is updated')
def test_contact_info_updated(context):
    results = context.current_page.get_contact_info()
    assert results[0] == 'test'
    assert results[1] == 'test'
    assert results[2] == 'test@email'


@then('the bio is updated')
def test_bio_updated(context):
    assert context.current_page.get_bio() == 'some test stuff'


@then('the favorite technologies are updated')
def test_fav_technologies_updated(context):
    results = context.current_page.get_fav_technologies()
    assert results[0] == 'test1'
    assert results[1] == 'test2'
    assert results[2] == 'test3'
    assert results[3] == 'Indifferent'
