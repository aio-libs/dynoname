
async def stream():
    yield await dns.resolve()
    while True:
        sleep()
        yield await dns.resolve()
