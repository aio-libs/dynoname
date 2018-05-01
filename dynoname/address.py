from typing import Union

IpAddress = Union[Ipv4Address, Ipv6Address]
SocketAddr = (IpAddress, Port)


class Address:
    def __init__(self):
        pass

    def diff(self, other: Address) -> (List[SocketAddr], List[SocketAddr]):
        return (new, old)

