from lettuce import *
@step('I have the string "(.*)"')
def have_the_string(step, string):
	world.string = string

@step('I put it in upper case')
def put_it_in_upper(step):
	world.string = world.string.upper()

@step('I see the string is "(.*)"')
def see_the_string_is(step, expected):
	assert world.string == expected, \
			"Got %s" % world.string
