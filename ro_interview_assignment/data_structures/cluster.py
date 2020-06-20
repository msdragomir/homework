from data_structures.network_collection import NetworkCollection


class Cluster:
    def __init__(self, name, network_dict, security_level):
        """
        Constructor for Cluster data structure.

        self.name -> str
        self.security_level -> int
        self.networks -> list(NetworkCollection)
        """

        try:
            self.name = str(name)
        except Exception:
            raise TypeError(
                f"Cannot convert 'name' argument {name} for Cluster to "
                f"str")

        self.networks = []
        if isinstance(network_dict, dict):
            for ipv4_prefix, network_list in network_dict.items():
                try:
                    self.networks.append(
                        NetworkCollection(ipv4_network=ipv4_prefix,
                                          raw_entry_list=network_list))
                except Exception as e:
                    print(str(e))
        else:
            raise TypeError(
                f"Invalid 'network_dict' argument for Cluster.  "
                f"Expected 'dict', got {type(network_dict)}")

        # ToDo: bool is subclass of int; isinstance(bool) -> int
        if isinstance(security_level, int):
            self.security_level = security_level
        else:
            raise TypeError(
                f"Invalid 'security_level' argument for Cluster.  "
                f"Expected 'int', got {type(security_level)}")
