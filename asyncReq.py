import httpx
import asyncio


async def getpls(urls):
    async with httpx.AsyncClient() as client:
        req = await client.get(urls)
    return req


test_jobs = ['https://www.workatastartup.com/companies/focal-systems', 'https://www.workatastartup.com/companies/daily', 'https://workatastartup.com/companies/mason', 'https://workatastartup.com/companies/magicbus', 'https://workatastartup.com/companies/tovala']


async def run(urls):
    tasks = []
    for url in urls:
        tasks.append(getpls(url))
    html = await asyncio.gather(*tasks)
    return html


def getReqs(urls):
    a = asyncio.run(run(urls))
    return a
