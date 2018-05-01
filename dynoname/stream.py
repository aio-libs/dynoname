import asyncio
from typing import AsyncIterator
import socket

from .address import Address

Stream = AsyncIterator[Address]


async def stdlib_resolve(name: str, port: int) -> Address:
    lst = await asyncio.get_event_loop().getaddrinfo(name, port)
    addr =  Address.from_getaddrinfo(lst)
    yield addr
    while True:

        await asyncio.sleep(10)

        lst = await asyncio.get_event_loop().getaddrinfo(name, port)
        new_addr = Address.from_getaddrinfo(lst)
        if new_addr != addr:
            yield Address.from_getaddrinfo(lst)
