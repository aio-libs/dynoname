from ipaddress import IPv4Address, IPv6Address
from typing import List, Union, NewType
import socket

import attr

IpAddress = Union[IPv4Address, IPv6Address]

LocalAddress = NewType('LocalAddress', str)
SingleAddress = Union[SocketAddr, LocalAddress]


@attr.s
class SocketAddr:
    ip = attr.ib(type=IpAddress)
    port = attr.ib(type=Port)


class Address:
    __slots__ = ('_first_priority',)

    def diff(self, other: Address) -> (List[SingleAddress], List[SingleAddress]):
        #
        return (new, old)

    @classmethod
    def from_getaddrinfo(list_of_addresses) -> Address:
        first_priority = []
        for (family, type, proto, canonname, sockaddr) in list_of_addresses:
            if family == socket.AF_INET:
                addr, port = sockaddr
                first_priority.append(SocketAddr(
                    ip=IPv4Address(addr),
                    port=port,
                ))
            elif family == socket.AF_INET6:
                addr, port, * = sockaddr
                first_priority.append(SocketAddr(
                    ip=IPv6Address(addr),
                    port=port,
                ))
            else:
                raise TypeError("Invalid address family")
        me = Address()
        me._first_priority = lst
        return me
