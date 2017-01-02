import trollius as asyncio
import datetime
from time import sleep

@asyncio.coroutine
def display_date(loop):
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        yield asyncio.sleep(1)

@asyncio.coroutine
def display_date_again(loop):
    end_time = loop.time() + 5.0
    while True:
        print("New" + str(datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        yield asyncio.sleep(1)


loop = asyncio.get_event_loop()
# Blocking call which returns when the display_date() coroutine is done
loop.run_until_complete(display_date(loop))
loop.run_until_complete(display_date_again(loop))
loop.close()
