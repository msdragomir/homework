from ipaddress import IPv4Network, IPv4Address

import loggin_module
from data_structures.entry import Entry

logger = loggin_module.get_logger(__name__, level="INFO")


class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """

        try:
            self.ipv4_network = IPv4Network(ipv4_network)
        except Exception:
            raise TypeError(f"Invalid 'ipv4_network' filed for "
                            f"NetworkCollection - {ipv4_network} ")

        self.entries = []
        if isinstance(raw_entry_list, list):
            for entry in raw_entry_list:
                if isinstance(entry, dict):
                    try:
                        self.entries.append(
                            Entry(entry.get("address"),
                                  entry.get("available"),
                                  entry.get("last_used")))
                    except Exception as e:
                        logger.error(str(e))
        else:
            raise TypeError(f"Invalid 'raw_entry_list' argument for "
                            f"NetworkCollection.  Expected 'list', "
                            f"got {type(raw_entry_list)}")

        logger.info(
            f"Removing invalid records for network "
            f"{self.ipv4_network} ...")
        self.remove_invalid_records()

        logger.info(
            f"Sorting records for network {self.ipv4_network} ...")
        self.sort_records()

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """

        valid_network_entries = []

        for network_entry in self.entries:
            ipv4_address = network_entry.address

            # Remove invalid IPv4 addresses
            try:
                ipv4_addr_obj = IPv4Address(ipv4_address)
            except Exception:
                logger.debug(
                    f"Removing invalid IPv4 address {ipv4_address}")
                continue

            # Remove IPv4 addresses that do not belong to the parent
            # IPv4 network and the network prefix
            if ipv4_addr_obj in self.ipv4_network.hosts():
                valid_network_entries.append(network_entry)
            else:
                logger.debug(
                    f"Removing IPv4 address {ipv4_address} as it does "
                    f"not belong to {self.ipv4_network}")

        self.entries = valid_network_entries

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)
