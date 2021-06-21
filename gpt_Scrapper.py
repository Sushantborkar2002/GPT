from selenium import webdriver
from colorama import Fore
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

Options = webdriver.ChromeOptions()
preferences = {"safebrowsing.enabled": "false", "download.default_directory": "C:\\Users\\sushant\\PycharmProjects\\untitled1\\codeforces"}

Options.add_experimental_option("prefs", preferences)
k = 100
url = f'https://www.codechef.com/problems/hard/?sort_by=SuccessfulSubmission&sorting_order=desc'
driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
driver.get(url)

for i in range(2, len(
        driver.find_elements_by_xpath('//*[@id="primary-content"]/div/div[2]/div/div[2]/table/tbody/tr')) - 1):
    code = driver.find_element_by_xpath(
        f'//*[@id="primary-content"]/div/div[2]/div/div[2]/table/tbody/tr[{i}]/td[2]').text
    url2 = f'https://www.codechef.com/status/{code}?sort_by=All&sorting_order=asc&language=116&status=15&handle=&Submit=GO'
    driver2 = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
    driver2.get(url2)
    for j in range(1, len(driver2.find_elements_by_xpath('//*[@id="primary-content"]/div/div[3]/table/tbody/tr')) - 1):
        sol = driver2.find_element_by_xpath(f'//*[@id="primary-content"]/div/div[3]/table/tbody/tr[{j}]/td[1]').text
        url3 = f'https://www.codechef.com/viewsolution/{sol}'
        Options = webdriver.ChromeOptions()
        Options.add_experimental_option("prefs", preferences)
        driver3 = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe", options=Options)
        driver3.get(url3)
        driver3.find_element_by_xpath('//*[@id="ember261"]/section[1]/aside/div/div/div[2]/ul/li[2]/a').click()
        time.sleep(3)
        driver3.quit()
    driver2.close()
