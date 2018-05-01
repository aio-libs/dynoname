import pytest

from .redis import DynonamePool
from aioredis import create_pool

# TODO(tailhook) move and rename?
from dynoname.stream import stdlib_resolve



@pytest.mark.run_loop
async def test_connect_tcp(request, server):
    stream = stdlib_resolve("localhost", server.tcp_address.port)
    pool = await create_pool(stream, db=13, pool_cls=DynonamePool)
    async with pool.get() as conn:
        await conn.execute("SET", "test_key", b"value1")
        value = await conn.execute("GET", "test_key")
        assert value == b"value1"
