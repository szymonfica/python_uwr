# Szymon Fica 337307
# list 8 task 1

import private
import asyncio
import aiohttp

async def fetch_page(session, url, params):
    async with session.get(url, params=params) as result:
        ans = await result.json()
    if result.status == 200:
        return ans
    else:
        return f"Error: {ans.get('message', 'Unknown error')}"


async def main():

    urls = ["https://api.openweathermap.org/data/2.5/weather",
            "https://api.nasa.gov/neo/rest/v1/feed"]
    params = [
        {
            'lat': '44.34',
            'lon': '10.99',
            'appid': private.API_key_weather(),
        },
        {
            'start_date': '2015-09-07',
            'end_date': '2015-09-08',
            'api_key': private.API_key_nasa(),
        }
    ]
    async with aiohttp.ClientSession() as session:
        requests = [fetch_page(session, urls[i], params[i]) for i in range(0, len(urls))]
        pages = await asyncio.gather(*requests)
        #with open("results.out", 'w') as f:
        #    print(pages, file=f)

asyncio.run(main())
