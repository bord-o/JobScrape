#!/home/bordo/.local/share/virtualenvs/JobScrape-478cIvc0/bin/python3
import scrape
import asyncReq
from bs4 import BeautifulSoup

JOBS_URL = 'https://account.ycombinator.com/?continue=https%3A%2F%2Fwww.workatastartup.com%2F'
JOBS_USER = 'brodylittle011@gmail.com'
JOBS_PASS = '0nly?Consept'
THREADS = 4

HEADLESS = False

test_jobs = ['https://www.workatastartup.com/companies/focal-systems', 'https://www.workatastartup.com/companies/daily', 'https://workatastartup.com/companies/mason', 'https://workatastartup.com/companies/magicbus', 'https://workatastartup.com/companies/tovala']


def main():
    '''
    urls = scrape.YCombLogin(JOBS_USER, JOBS_PASS, True, depth=2, writeFile=False)
    jobs = list(map(scrape.addwww, urls))
    print(jobs)
    '''

    reqs = asyncReq.getReqs(test_jobs)

    r = reqs[1]
    soup = BeautifulSoup(r, 'html.parser')
    print(soup.prettify())


    tech = []
    with open("./tech.txt", 'w+') as wf:
        wf.write(soup.prettify())

if __name__ == "__main__":
    main()
