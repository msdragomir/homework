from data_structures.network_collection import NetworkCollection


class Cluster:
    def __init__(self, name, network_dict, security_level):
        """
        Constructor for Cluster data structure.

        self.name -> str
        self.security_level -> int
        self.networks -> list(NetworkCollection)
        """

        # assert name is str, f"Invalid 'name' argument for Cluster.  Expected 'str', got {type(name)}"
        # assert network_dict is dict, f"Invalid 'network_dict' argument for Cluster.  Expected 'dict', got {type(network_dict)}"
        # assert security_level is int, f"Invalid 'security_level' argument for Cluster.  Expected 'int', got {type(security_level)}"
        if isinstance(name, str):
            self.name = name
        else:
            print(f"Invalid 'name' argument for Cluster.  Expected 'str', got {type(name)}")
            # ToDo: what do i do ?

        if isinstance(network_dict, dict):
            self.networks = [
                NetworkCollection(ipv4_network=ipv4_prefix, raw_entry_list=network_list)
                for ipv4_prefix, network_list in network_dict.items()
            ]
        else:
            print(f"Invalid 'network_dict' argument for Cluster.  Expected 'dict', got {type(network_dict)}")
            # ToDo: what do i do ?

        if isinstance(security_level, int):
            self.security_level = security_level
        else:
            print(f"Invalid 'security_level' argument for Cluster.  Expected 'int', got {type(security_level)}")
            # ToDo: what do i do ?
