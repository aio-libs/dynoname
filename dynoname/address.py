from ipaddress import IPv4Address, IPv6Address
from typing import List, Union, NewType
import socket
import random

import attr

IpAddress = Union[IPv4Address, IPv6Address]
LocalAddress = NewType('LocalAddress', str)


@attr.s
class SocketAddr:
    ip = attr.ib(type=IpAddress)
    port = attr.ib(type=int)

    def as_tuple(self):
        return (str(self.ip), self.port)


SingleAddress = Union[SocketAddr, LocalAddress]


class Address:
    __slots__ = ('_first_priority',)

    def diff(self, other: "Address") -> (List[SingleAddress], List[SingleAddress]):
        raise NotImplemented()
        # return (new, old)

    def __eq__(self, other: "Address") -> bool:
        if isinstance(other, Address):
            return self._first_priority == other._first_priority
        else:
            return NotImplemented

    def pick_one(self):
        return random.choice(self._first_priority)

    @classmethod
    def from_getaddrinfo(Address, list_of_addresses) -> "Address":
        first_priority = []
        for (family, type, proto, canonname, sockaddr) in list_of_addresses:
            if family == socket.AF_INET:
                addr, port = sockaddr
                first_priority.append(SocketAddr(
                    ip=IPv4Address(addr),
                    port=port,
                ))
            elif family == socket.AF_INET6:
                addr, port, *_ = sockaddr
                first_priority.append(SocketAddr(
                    ip=IPv6Address(addr),
                    port=port,
                ))
            else:
                raise TypeError("Invalid address family")
        me = Address()
        me._first_priority = first_priority
        return me
