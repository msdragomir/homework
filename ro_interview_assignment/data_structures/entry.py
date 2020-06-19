import datetime

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
            print(f"Invalid Entry 'address' field - {address}.  Expected 'str', got {type(address)}")
            # ToDo: what do i do ?

        if isinstance(available, bool):
            self.available = available
        else:
            print(f"Invalid Entry 'available' field - {available}.  Expected 'bool', got {type(available)}")
            # ToDo: what do i do ?

        try:
            # ToDo: does it really have to be of datetime type ?
            last_used_datetime = datetime.datetime.strptime(last_used, DATETIME_FORMAT)
            self.last_used = last_used_datetime
        except:
            print(f"Invalid Entry 'last_used' field.  Expected datetime format {DATETIME_FORMAT}")
            # ToDo: what do i do ?
