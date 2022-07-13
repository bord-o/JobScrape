#!/home/bordo/.local/share/virtualenvs/JobScrape-478cIvc0/bin/python3
import scrape
import multiprocessing

JOBS_URL = 'https://account.ycombinator.com/?continue=https%3A%2F%2Fwww.workatastartup.com%2F'
JOBS_USER = 'brodylittle011@gmail.com'
JOBS_PASS = '0nly?Consept'
THREADS = 4

HEADLESS = False

test_jobs = ['https://workatastartup.com/companies/focal-systems', 'https://workatastartup.com/companies/daily', 'https://workatastartup.com/companies/mason', 'https://workatastartup.com/companies/magicbus', 'https://workatastartup.com/companies/tovala']


def main():
    jobs = scrape.YCombLogin(JOBS_USER, JOBS_PASS, True, depth=2, writeFile=False)
    print(jobs)

    pool = multiprocessing.Pool(THREADS)
    tech = pool.map(scrape.extractTech, jobs)

    with open("./tech.txt", 'w+') as wf:
        for entry in tech:
            wf.write(entry+"\n\n")


if __name__ == "__main__":
    main()
