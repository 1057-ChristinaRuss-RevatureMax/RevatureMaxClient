from selenium import webdriver
import os

def before_all(context):
	context.driver = webdriver.Firefox() # the one true browser
	context.associate_dashboard_url = os.environ["front_end_url"]

def before_step(context, step):
	pass

def before_scenario(context, scenario):
	pass

def before_feature(context, feature):
	pass

def before_tag(context, tag):
	pass

def after_tag(context, tag):
	pass

def after_feature(context, feature):
	pass

def after_scenario(context, scenario):
	pass

def after_step(context, step):
	pass

def after_all(context):
	context.driver.quit()
