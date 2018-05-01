import asyncio
from typing import AsyncIterator
import socket

from .address import Address

Stream = AsyncIterator[Address]


async def stdlib_resolve(name: str, port: int) -> Address:
    lst = await asyncio.get_event_loop().getaddrinfo(name, port)
    return Address.from_getaddrinfo(lst)
