import abc

from aioredis.pool import ConnectionsPool
from dynoname import Stream


class DynonamePool(ConnectionsPool):

    def __init__(self, address: Stream, *args, loop=None, **kwargs):
        self._address_stream = address
        self._current_address = None
        self._name_task = None
        super().__init__(None, *args, loop=None, **kwargs)

    # TODO(tailhook) fix this in the original pool
    @property
    def _address(self):
        return self._current_address.pick_one().as_tuple()

    # TODO(tailhook) fix this in the original pool
    @_address.setter
    def _address(self, value):
        pass

    async def update_names(self, address):
        # TODO(tailhook) cancellation, timeout
        current_name = await address.__anext__()
        while True:
            new_name = await address.__anext__()
            old, new = new_name.diff(old_name)
            if old:
                for conn in self._used:
                    if conn._address == old:
                        # TODO(tailhook) extra attribute
                        conn._retired = true

    def release(self, conn):  # TODO: arguments
        if getattr(conn, '_retired', False):
            conn.close()
        super().release(conn)

    async def acquire(self, command=None, args=()):
        # TODO(tailhook) wait for the first address
        return await super().acquire(command, args)

    @property
    def address(self):
        return "<dynamic-address>"

    async def _fill_free(self, *args, **kwargs):
        if self._current_address is None:
            # this is a first connection, perhaps in create_pool
            self._current_address = await self._address_stream.__anext__()
            print("ADDR", self._current_address)
            # TODO(tailhook) add cancellation
            self._name_task = self._loop.create_task(
                self.update_names(self._address_stream))
        return await super()._fill_free(*args, **kwargs)

    async def close(self):
        self._name_task.cancel()
        await super().close()




