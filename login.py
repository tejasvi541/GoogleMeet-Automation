#! /usr/bin/python3

from lnks import getLnk
from selenium import webdriver
import time
import sys


if len(sys.argv) > 1:
    # Get subject from command line.
    csub = ' '.join(sys.argv[1:])

# Getting Link of class from dictionary
clink = getLnk(csub)

# Path of WebDriver
PATH = "/home/tejasvi/Workspace/NW/Selenium/chromedriver"
driver = webdriver.Chrome(PATH)
# Requesting Website
driver.get('https://meet.google.com/landing?authuser=1')

# Logging into Gmail
driver.find_element_by_id("identifierId").send_keys(
    open("pwd.txt").read())
driver.find_element_by_id("identifierNext").click()
time.sleep(5)

driver.find_element_by_name("password").send_keys(open("pwd.txt").read())
driver.find_element_by_id("passwordNext").click()
time.sleep(5)

# Sending Link to Website to Start the meet
driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]').click()
time.sleep(1)
driver.find_element_by_css_selector(
    '#yDmH0d > div.llhEMd.iWO5td > div > div.g3VIld.Xpwrdc.JLm1tf-Jyewjb.Up8vH.hFEqNb.J9Nfi.iWO5td > span > div > div.W9wDc.D3oBEe.CNZLwc.xSLMxc.yaevDc > div.n9IS1.oJeWuf > div.FtBNWb > input').send_keys(clink)
driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[4]/div[2]/div').click()
