from selenium import webdriver
#from path_to_poms import pom_name_here

def before_all(context):
	context.driver = webdriver.Firefox() # the one true browser
	#context.my_pom_abbreviation = pom_name_here(context.driver)

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
