import httpx
import multiprocessing

test_jobs = ['https://www.workatastartup.com/companies/focal-systems', 'https://www.workatastartup.com/companies/daily', 'https://workatastartup.com/companies/mason', 'https://workatastartup.com/companies/magicbus', 'https://workatastartup.com/companies/tovala']


def getWithStatus(url):
    print(f'getting: {url}')
    return httpx.get(url)


def getPg(urls):
    with multiprocessing.Pool() as p:
        res = p.map(getWithStatus, urls)
    return res


# just a sequential version of the function for testing
def getPgSeq(urls):
    res = []
    for u in urls:
        res.append(httpx.get(u))
    return res
