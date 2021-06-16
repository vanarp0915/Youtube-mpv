#!/usr/bin/env python
import urllib.request
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver
import time
import sys
import subprocess
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote

__author__      = "Vanarp0915"

search=(sys.argv[1])

def youtube():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)

    query = urllib.parse.quote(search)
    link = "https://www.youtube.com/results?search_query=" + query
    driver.get(link)
    more_buttons = driver.find_elements_by_class_name("moreLink")
    for x in range(len(more_buttons)):
        if more_buttons[x].is_displayed():
            driver.execute_script("arguments[0].click();", more_buttons[x])
            time.sleep(1)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source,'html.parser')
    for vid in soup.findAll(attrs={'class': 'yt-simple-endpoint style-scope ytd-video-renderer'}):
        if "googleads" not in vid['href'] and not vid['href'].startswith(u"/user") and not vid['href'].startswith(
                u"/channel"):
            id = vid['href'].split("v=")[1].split("&")[0]
            url="https://www.youtube.com/watch?v=" + id
            return url
#print(youtube())
link= youtube()
subprocess.call(['bash',"thetest.sh",link,sys.argv[1] ])

