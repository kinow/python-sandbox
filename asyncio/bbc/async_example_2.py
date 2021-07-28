import requests
import asyncio
import time

async def counter():
    now = time.time()
    print("Started counter")
    for i in range(0, 10):
        last = now
        await asyncio.sleep(0.001)
        now = time.time()
        print(f"{i}: Was asleep for {now - last}s")

async def main():
    t = asyncio.get_event_loop().create_task(counter())

    await asyncio.sleep(0)

    def send_request():
        print("Sending HTTP request")
        r = requests.get('https://www.mackenzie.br/')
        print(f"Got HTTP response with status {r.status_code}")

    # bug here in the tutorial, but couldn't find the source to fix it
    await asyncio.get_event_loop().run_in_executor(None, send_request)

    await t

asyncio.get_event_loop().run_until_complete(main())
