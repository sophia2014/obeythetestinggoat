from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title

if ! 'Django' in browser.title
    throw new AssertionError
