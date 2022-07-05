#!/home/bordo/.local/share/virtualenvs/JobScrape-478cIvc0/bin/python3
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

JOBS_URL = 'https://www.ycombinator.com/jobs'
JOBS_LOGIN_URL = 'https://account.ycombinator.com/?continue=https%3A%2F%2Fwww.workatastartup.com%2F'
JOBS_USER = 'brodylittle011@gmail.com'
JOBS_PASS = '0nly?Consept'

foxopts = webdriver.FirefoxOptions()
# foxopts.add_argument("--headless")

driver = webdriver.Firefox(options=foxopts)
driver.get(JOBS_LOGIN_URL)

username_input = driver.find_element(By.ID, "ycid-input")
password_input = driver.find_element(By.ID, "password-input")
#print(username_input)

username_input.send_keys(JOBS_USER)
password_input.send_keys(JOBS_PASS)

login_button = driver.find_element(By.CSS_SELECTOR, "button.sign-in-button" )
login_button.click()

sleep(10)

for i in range(20):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(4)

company_names = driver.find_elements(By.CSS_SELECTOR, "span.company-name")

company_links_list = []
company_names_list = []

for n in company_names:
    # use parent element of name to get link
    company_links_list.append(n.find_element(By.XPATH, '..').get_attribute('href'))

    # lowercase the company name text
    company_names_list.append(n.text.lower())

print("company names: ", len(company_names_list))
print("company links: ", len(company_links_list))

with open('./companies.txt', "w") as file:
    file.write('\n'.join(company_names_list))

with open('./complinks.txt', "w") as file:
    file.write('\n'.join(company_links_list))

