#!/home/bordo/.local/share/virtualenvs/JobScrape-478cIvc0/bin/python3
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from urllib3.exceptions import MaxRetryError


def extractTech(jobLink, headless=True):
    foxopts = webdriver.FirefoxOptions()
    if headless:
        foxopts.add_argument("--headless")

    driver = webdriver.Firefox(options=foxopts)
    print("Launching Selenium browser...")
    driver.get(jobLink)
    try:
        tech = driver.find_element(By.CSS_SELECTOR, 'div.sm\:block:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > p:nth-child(1)')
        print(tech.text)
        driver.quit()
        return tech.text

    except NoSuchElementException:
        print("No tech field found for this company...")
        driver.quit()
        return "***"

    '''
    except MaxRetryError:
        print("urllib3 max retries exceeded")
        driver.quit()
    '''



def YCombLogin(username, password, headless=True, depth=2, writeFile=False):

    if depth < 2:
        print("depth must be greater than 2...")
        return []

    JOBS_URL = 'https://account.ycombinator.com/?continue=https%3A%2F%2Fwww.workatastartup.com%2F'
    foxopts = webdriver.FirefoxOptions()
    if headless:
        foxopts.add_argument("--headless")

    driver = webdriver.Firefox(options=foxopts)
    print("Launching Selenium browser...")
    driver.get(JOBS_URL)

    username_input = driver.find_element(By.ID, "ycid-input")
    password_input = driver.find_element(By.ID, "password-input")

    username_input.send_keys(username)
    password_input.send_keys(password)

    login_button = driver.find_element(By.CSS_SELECTOR,
                                       "button.sign-in-button")
    login_button.click()
    print("Trying to log in...")

    sleep(10)

    print(f"Trying to scrape {depth*10} jobs...")

    for i in range(depth-1):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        print("sleeping for ajax load")
        sleep(4)

    company_names = driver.find_elements(By.CSS_SELECTOR, "span.company-name")

    company_links_list = []
    company_names_list = []

    for n in company_names:
        # use parent element of name to get link
        company_links_list.append(n.find_element(By.XPATH, '..')
                                   .get_attribute('href'))

        # lowercase the company name text
        company_names_list.append(n.text.lower())

    print("found company names: ", len(company_names_list))
    print("found company links: ", len(company_links_list))

    if writeFile:
        with open('./comp.txt', "w") as file:
            file.write('\n'.join(company_names_list))

        with open('./links.txt', "w") as file:
            file.write('\n'.join(company_links_list))

    driver.quit()

    return company_links_list
