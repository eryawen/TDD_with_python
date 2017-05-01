from selenium import webdriver
# System.setProperty("webdriver.gecko.driver","D:\env\Python\Python36-32\Scripts\geckodriver.exe")
browser = webdriver.Firefox()
# browser.get('http://localhost:8080')
browser.get('http://127.0.0.1:8000/')
assert 'Django' in browser.title