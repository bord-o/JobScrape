#!/home/bordo/.local/share/virtualenvs/JobScrape-478cIvc0/bin/python3
import scrape
import asyncReq

JOBS_URL = 'https://account.ycombinator.com/?continue=https%3A%2F%2Fwww.workatastartup.com%2F'
JOBS_USER = 'brodylittle011@gmail.com'
JOBS_PASS = '0nly?Consept'
THREADS = 4

HEADLESS = False

test_jobs = ['https://www.workatastartup.com/companies/focal-systems', 'https://www.workatastartup.com/companies/daily', 'https://workatastartup.com/companies/mason', 'https://workatastartup.com/companies/magicbus', 'https://workatastartup.com/companies/tovala']


def main():
    urls = scrape.YCombLogin(JOBS_USER, JOBS_PASS, True, depth=2, writeFile=False)
    jobs = list(map(scrape.addwww, urls))
    print(f"total jobs: {len(jobs)}")

    reqs = asyncReq.getReqs(jobs)

    print(f"reqests recieved: {len(reqs)}")
    print(list(filter(lambda req: req.status_code != 200, reqs)))

    tech = list(map(scrape.getTech, reqs))
    # print(tech)

    # 'rawCompany -> 'tech_description

    with open("./tech.txt", 'w+') as wf:
        for entry in tech:
            wf.write(f'{entry}\n---------------------------------------------------------------------------\n')

if __name__ == "__main__":
    main()
