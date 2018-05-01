from ipaddress import IPv4Address, IPv6Address
from typing import List, Union

import attr

IpAddress = Union[IPv4Address, IPv6Address]


@attr.s
class SocketAddr:
    ip = attr.ib(type=IpAddress)
    port = attr.ib(type=Port)


class Address:
    def __init__(self):
        pass

    def diff(self, other: Address) -> (List[SocketAddr], List[SocketAddr]):
        return (new, old)

