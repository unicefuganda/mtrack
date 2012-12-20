from lettuce import *
from lxml import html
from nose.tools import assert_equals
from splinter import Browser

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

browser = Browser()

def assert_true(boolean, text):
  if  boolean == True:
    print bcolors.OKGREEN + text + bcolors.ENDC
  else:
    close_browser()
    raise Exception(bcolors.FAIL + "Failed : " + text + bcolors.ENDC)

def close_browser():
  browser.quit();

browser.visit('http://localhost:8000')
assert_true(browser.is_text_present('Alerts'), "Text 'Alerts' is present")
assert_true(browser.is_text_present('Approve HMIS Reports'), "Text 'Approve HMIS Reports' is present")
assert_true(browser.is_text_present('User Management'), "Text 'User Management' is present")
assert_true(browser.is_text_present('Incoming Messages'), "Text 'Incoming Messages' is present")
close_browser()
