from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options


#///////////////// Init binary & driver
new_driver_path = '/home/mardio/PYTHON/intagram/geckodriver'
new_binary_path = '/opt/firefox-developer/firefox'

ops = options()
ops.binary_location = new_binary_path
serv = Service(new_driver_path)
browser1 = webdriver.Firefox(service=serv, options=ops)