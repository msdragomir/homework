import datetime
from ipaddress import IPv4Address

DATETIME_FORMAT = '%d/%m/%y %H:%M:%S'


class Entry:
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """

        if isinstance(address, str):
            self.address = address
        else:
            raise TypeError(
                f"Invalid Entry 'address' field - {address}.  "
                f"Expected 'str', got {type(address)}")

        if isinstance(available, bool):
            self.available = available
        else:
            raise TypeError(
                f"Invalid Entry 'available' field - {available}.  "
                f"Expected 'bool', got {type(available)}")

        try:
            datetime.datetime.strptime(last_used, DATETIME_FORMAT)
            self.last_used = last_used
        except Exception:
            raise TypeError(
                f"Invalid Entry 'last_used' field {last_used}.  "
                f"Expected datetime format {DATETIME_FORMAT}")

    def __lt__(self, other):
        """
        Decide whether one IPv4 address is "less than" the other by
        comparing the decimal value of the IPv4 address
        """
        assert isinstance(other, Entry)
        return IPv4Address(self.address) < IPv4Address(other.address)
