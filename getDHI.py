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
url = "https://www.wikiwand.com/en/List_of_countries_by_Human_Development_Index"
driver.get(url)

sleep(2)
scores = driver.find_elements(
    by=By.CSS_SELECTOR, value=("table tr td:nth-child(4)"))

countries = driver.find_elements(
    by=By.CSS_SELECTOR, value=("table th a.int-link"))

i = 0
listedCountries = []
scoresByCountry = []
for item in countries:
    try:
        name = item.text
        listedCountries.append(name)

    except Exception:
        print(Exception.mro())
        pass
i = 0
for item in scores:
    try:
        if i == len(listedCountries):
            break

        scoresByCountry.append(round(float(item.text),4))
        i += 1
    except Exception:
        pass

#print(listedCountries, scoresByCountry)

filteredCountries = []
filteredScores = []

with open('infra.csv', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            for country in listedCountries:
                if row[0] in country:
                    filteredCountries.append(row[0])
                    filteredScores.append(
                        scoresByCountry[listedCountries.index(country)])

            line_count += 1

with open('idh.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')

    spamwriter.writerow(["country", "score"])

    i = 0
    for c in filteredScores:
        spamwriter.writerow([filteredCountries[i], filteredScores[i]])
        i += 1

driver.close()
