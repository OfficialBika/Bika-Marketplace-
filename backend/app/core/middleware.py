import time

async def request_timer(request, call_next):
    start = time.time()
    response = await call_next(request)
    response.headers['X-Process-Time'] = str(time.time() - start)
    return response
