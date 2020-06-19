from ipaddress import IPv4Network

from data_structures.entry import Entry


class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """

        try:
            self.ipv4_network = IPv4Network(ipv4_network)
        except:
            print(f"Invalid 'ipv4_network' filed for NetworkCollection - {ipv4_network} ")
            # ToDo: what do i do ?

        if isinstance(raw_entry_list, list):
            self.entries = [
                Entry(entry.get("address"), entry.get("available"), entry.get("last_used"))
                for entry in raw_entry_list if isinstance(entry, dict)
            ]
        else:
            print(f"Invalid 'raw_entry_list' argument for NetworkCollection.  "
                  f"Expected 'list', got {type(raw_entry_list)}")
            # ToDo: what do i do ?

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """

        pass

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)
