from behave import *

from features.poms.TrainerProfilePage import TrainerProfilePage


@given('the user is signed in as a trainer')
def log_in_as_trainer(context):
    pass


@given('the user is on the trainer profile page')
def on_trainer_profile_page(context):
    context.driver.get('file:///E:/Projects/RevatureMaxClient/trainer-profile/trainer-profile.html')
    context.current_page = TrainerProfilePage(context.driver)


@when('the user clicks the edit training info button')
def click_edit_training_info(context):
    context.current_page.click_edit_training_info()


@when('the user inputs a new specialization')
def input_specialization(context):
    context.current_page.input_specialization('test')


@when('the user inputs a new location')
def input_location(context):
    context.current_page.input_location('test')


@when('the user clicks the submit training info button')
def click_submit_training_info(context):
    context.current_page.submit_training_info()


@then('the trainer can view their profile information')
def test_view_trainer_info(context):
    results = context.current_page.get_trainer_info()
    assert results[0] == 'trainerfirstname'
    assert results[1] == 'trainerlastname'
    assert results[2] == 'example@trainer.com'
    assert results[3] == 'some trainer stuff about me'
    assert results[4] == 'python w/ automation'
    assert results[5] == 'Ohio'


@then('the specialization and location are updated')
def test_training_info_updated(context):
    results = context.current_page.get_training_info()
    assert results[0] == 'test'
    assert results[1] == 'test'
