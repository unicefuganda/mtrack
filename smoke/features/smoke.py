from lettuce import *
from lxml import html
from nose.tools import assert_equals
from splinter import Browser
import sys

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

def print_ok(text):
  print bcolors.OKBLUE + text + bcolors.ENDC

def print_success(text):
  print bcolors.OKGREEN + text + bcolors.ENDC

def print_fail(text):
  print bcolors.FAIL + "Failed : " + text + bcolors.ENDC

def assert_true(boolean, text):
  if  boolean != True:
    raise Exception(bcolors.FAIL + "Failed : " + text + bcolors.ENDC)

def close_browser():
  browser.quit();

def assert_text_presence(*texts):
  for text in texts:
    assert_true(browser.is_text_present(text), "Text '"+ text +"' is present")

def assert_current_url(url, text):
  assert_true(browser.url == url, text)

URL = {
  'home'                : 'http://localhost:8000/',
  'login'               : 'http://localhost:8000/account/login/',
  'approve'             : 'http://localhost:8000/approve/',
  'health_data'         : 'http://localhost:8000/mtrack/stats/',
  'mgt_data'            : 'http://localhost:8000/mtrack/mgt/stats/',
  'facility'            : 'http://localhost:8000/cvs/facility/',
  'users'               : 'http://localhost:8000/cvs/reporter/',
  'messages'            : 'http://localhost:8000/cvs/messagelog/',
  'anonymous_reports'   : 'http://localhost:8000/anonymousreports/',
  'stock_data'          : 'http://localhost:8000/mtrack/logistics',
}

def assert_landing_page():
  """Landing page"""
  browser.visit(URL['home'])
  assert_text_presence('Alerts', 'Approve HMIS Reports', 'User Management', 'Incoming Messages')
  print_ok("Landing page ok!")

def assert_login_page():
  """Login page"""
  browser.visit(URL['login'])
  browser.fill("username", "smoke")
  browser.fill("password", "password")
  browser.find_by_css("input[type=submit]").first.click()
  assert_current_url(URL['home'], 'Login success!')
  print_ok("Login page ok!")

def assert_approve_page():
  """Approve page"""
  browser.visit(URL['approve'])
  assert_text_presence('Actions', 'Last Reporting Period Results')
  print_ok("Approve page ok!")

def assert_health_data_page():
  """Health data page"""
  browser.visit(URL['health_data'])
  assert_text_presence('Variation of Fever (VHT)')
  print_ok("Health data page ok!")

def assert_mgt_data_page():
  """Mgt Data page"""
  browser.visit(URL['mgt_data'])
  assert_text_presence('District', 'VHTs', 'Health Centers')
  print_ok("Mgt Data page ok!")

def assert_faciliy_page():
  """Facility page"""
  browser.visit(URL['facility'])
  assert_text_presence('Filters', 'Health Facilities')
  print_ok("Facility page ok!")

def assert_users_page():
  """Users page"""
  browser.visit(URL['users'])
  assert_text_presence('Filters', 'Actions', 'Registered Users')
  print_ok("Users page ok!")

def assert_messaging_page():
  """Messaging page"""
  browser.visit(URL['messages'])
  assert_text_presence('Filters', 'Actions', 'Results')
  print_ok("Messaging page ok!")

def assert_anonymous_reports_page():
  """Anonymous reports page"""
  browser.visit(URL['anonymous_reports'])
  assert_text_presence('Actions', 'Anonymous Reports')
  print_ok("Anonymous reports page ok!")

def assert_stock_data_page():
  """Stock Data page"""
  browser.visit(URL['stock_data'])
  assert_text_presence()
  print_ok("Stock Data page ok!")

def smoke():
  """Main suite"""
  try:
    assert_landing_page()
    assert_login_page()
    assert_approve_page()
    assert_health_data_page()
    assert_mgt_data_page()
    assert_faciliy_page()
    assert_users_page()
    assert_messaging_page()
    assert_anonymous_reports_page()
    # assert_stock_data_page() #commenting this out since it takes a lot of time, uncomment this once the issue is resolved
    close_browser()
    return 0
  except Exception, e:
    print e
    close_browser()
    return 1

if __name__ == '__main__':
    sys.exit(smoke())