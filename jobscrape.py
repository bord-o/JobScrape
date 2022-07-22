#!/home/bordo/.local/share/virtualenvs/JobScrape-478cIvc0/bin/python3
import scrape
import asyncReq

JOBS_URL = 'https://account.ycombinator.com/?continue=https%3A%2F%2Fwww.workatastartup.com%2F'
JOBS_USER = 'brodylittle011@gmail.com'
JOBS_PASS = '0nly?Consept'

HEADLESS = False

test_jobs = ['https://www.workatastartup.com/companies/focal-systems', 'https://www.workatastartup.com/companies/daily', 'https://www.workatastartup.com/companies/mason', 'https://www.workatastartup.com/companies/magicbus', 'https://www.workatastartup.com/companies/tovala']


def main():
    urls = scrape.YCombLogin(JOBS_USER, JOBS_PASS, True, depth=16, writeFile=False)
    jobs = list(map(scrape.addwww, urls))
    print(f"total jobs: {len(jobs)}")

    reqs = asyncReq.getPg(jobs)

    print(f"reqests recieved: {len(reqs)}")
    print(list(filter(lambda req: req.status_code != 200, reqs)))

    tech = list(map(scrape.getTech, reqs))
    # print(tech)

    # 'rawCompany -> 'tech_description

    with open("./tech.txt", 'w+') as wf:
        for entry in tech:
            wf.write(f'{entry}\n---------------------------------------------------------------------------\n')

    empty_tech = 0
    for entry in tech:
        if entry == "":
            empty_tech += 1

    print(f"{empty_tech} companies had no technology section. (out of {len(tech)})")

if __name__ == "__main__":
    main()
