from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
import csv

chrome_driver_path = "./chromedriver"
chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

s = Service(chrome_driver_path)

driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get("https://www.indexmundi.com/facts/indicators/IQ.WEF.PORT.XQ/rankings")

sleep(2)
scores = driver.find_elements(by=By.CSS_SELECTOR, value=("table tr td.r"))
countries = driver.find_elements(by=By.CSS_SELECTOR, value=("table tr td a"))

# get countries
i = 0
for item in countries:
    try:
        countries[i] = item.text
        i += 1
    except Exception:
        print(Exception.mro())
        pass

# get scores
i = 0
for item in scores:
    try:
        scores[i] = round((float(item.text) / 7), 4)
        i += 1
    except Exception:
        pass

with open('infra.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')

    spamwriter.writerow(["country", "score"])

    i = 0
    for c in countries:
        spamwriter.writerow([countries[i], scores[i]])
        i += 1


driver.close()
