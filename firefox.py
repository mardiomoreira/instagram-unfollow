from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from time import sleep

binary = FirefoxBinary('/opt/firefox-developer/firefox')
ff = webdriver.Firefox(firefox_binary=binary)
ff.get('http://127.0.0.1:8080/')
print(ff.page_source)