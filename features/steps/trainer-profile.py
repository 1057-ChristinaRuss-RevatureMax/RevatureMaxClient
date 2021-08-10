from behave import *

from features.poms.TrainerProfilePage import TrainerProfilePage

current_email = 'mock1026.employee0ced595f-c2c5-4fd9-9e69-4556edce0a6c@mock.com'


@given('the user is signed in as a trainer')
def log_in_as_trainer(context):
    context.driver.get('http://localhost:9001/')
    context.current_page = TrainerProfilePage(context.driver)
    context.current_page.login(current_email)


@given('the user is on the trainer profile page')
def on_trainer_profile_page(context):
    context.driver.get('http://localhost:9001/trainerprofile')
    context.current_page = TrainerProfilePage(context.driver)


@given('the trainers info is reset')
def reset_info(context):
    context.current_page.reset_info()
    global current_email
    current_email = 'mock1026.employee0ced595f-c2c5-4fd9-9e69-4556edce0a6c@mock.com'

@when('the trainer inputs new contact info')
def input_contact_info(context):
    context.current_page.input_contact_info('Joe', 'Tester', 'joe@test.com')
    global current_email
    current_email = 'joe@test.com'

@when('the user clicks the edit training info button')
def click_edit_training_info(context):
    context.current_page.click_edit_training_info()


@when('the user inputs a new specialization')
def input_specialization(context):
    context.current_page.input_specialization('something else')


@when('the user inputs a new location')
def input_location(context):
    context.current_page.input_location('somewhere else')


@when('the user clicks the submit training info button')
def click_submit_training_info(context):
    context.current_page.submit_training_info()


@then('the trainer can view their profile information')
def test_view_trainer_info(context):
    results = context.current_page.get_trainer_info()
    assert results[0] == 'Mock 1026'
    assert results[1] == 'Employee 1026'
    assert results[2] == 'mock1026.employee0ced595f-c2c5-4fd9-9e69-4556edce0a6c@mock.com'
    assert results[3] == 'some trainer stuff about me'
    assert results[4] == 'something'
    assert results[5] == 'somewhere'


@then('the specialization and location are updated')
def test_training_info_updated(context):
    results = context.current_page.get_training_info()
    assert results[0] == 'something else'
    assert results[1] == 'somewhere else'

    # reset the info for next time
    context.current_page.reset_info()

