from copy import deepcopy
from ipaddress import IPv4Network

from data_structures.datacenter import Datacenter

DATA = {
    "Berlin": {
        "BER-1": {
            "security_level": 3,
            "networks": {
                "192.168.200.0/24": [
                    {
                        "address": "192.168.200.8",
                        "available": True,
                        "last_used": "30/01/20 17:00:00"
                    }
                ]
            }
        }
    }
}


def test_invalid_entry_address_field():
    """
    Validate that invalid values for the 'address' attribute of an Entry
    object are ignored
    """
    datacenter_dict = deepcopy(DATA)
    datacenter_dict["Berlin"]["BER-1"]["networks"][
        "192.168.200.0/24"].extend(
        [
            {
                "address": 1,
                "available": True,
                "last_used": "30/01/20 17:00:00"
            },
            {
                "address": "255.255.255.0",
                "available": True,
                "last_used": "30/01/20 17:00:00"
            },
            {
                "address": "192.168..0.3",
                "available": True,
                "last_used": "30/01/20 17:00:00"
            },
            {
                "address": "192.168.0",
                "available": False,
                "last_used": "30/01/20 17:00:00"
            },
            {
                "address": "invalid",
                "available": True,
                "last_used": "30/01/20 17:00:00"
            },
            {
                "address": "192.168.200.0",
                "available": True,
                "last_used": "30/01/20 17:00:00"
            },
            {
                "address": "192.168.200.255",
                "available": True,
                "last_used": "30/01/20 17:00:00"
            },
            {
                "address": "192.168.200.a",
                "available": True,
                "last_used": "30/01/20 17:00:00"
            }
        ]
    )
    common_check_invalid_entry(datacenter_dict)


def test_invalid_entry_available_field():
    """
    Validate that invalid values for the 'available' attribute of an
    Entry object are ignored
    """
    datacenter_dict = deepcopy(DATA)
    datacenter_dict["Berlin"]["BER-1"]["networks"][
        "192.168.200.0/24"].append(
        {
            "address": "192.168.200.9",
            "available": 1,
            "last_used": "30/01/20 17:00:00"
        }
    )
    common_check_invalid_entry(datacenter_dict)


def test_invalid_entry_last_used_field():
    """
    Validate that invalid values for the 'last_used' attribute of an
    Entry object are ignored
    """
    datacenter_dict = deepcopy(DATA)
    datacenter_dict["Berlin"]["BER-1"]["networks"][
        "192.168.200.0/24"].append(
        {
            "address": "192.168.200.9",
            "available": True,
            "last_used": 1
        }
    )
    common_check_invalid_entry(datacenter_dict)


def test_invalid_network_ipv4_network():
    """
    Validate that invalid values for the 'ipv4_network' attribute of a
    NetworkCollection object are ignored
    """
    datacenter_dict = deepcopy(DATA)
    datacenter_dict["Berlin"]["BER-1"]["networks"].update(
        {
            "192.168.200.0/33": [
                {
                    "address": "192.168.200.8",
                    "available": True,
                    "last_used": "30/01/20 17:00:00"
                }
            ],
            "some string": [
                {
                    "address": "192.168.200.8",
                    "available": True,
                    "last_used": "30/01/20 17:00:00"
                }
            ]
        }
    )
    common_check_invalid_entry(datacenter_dict)


def test_invalid_network_entries_type():
    """
    Validate that invalid values for the 'entries' attribute of a
    NetworkCollection object are ignored
    """
    datacenter_dict = {
        "Berlin": {
            "BER-1": {
                "security_level": 3,
                "networks": {
                    "192.168.200.0/24": [
                        {
                            "address": "192.168.200.8",
                            "available": True,
                            "last_used": "30/01/20 17:00:00"
                        }
                    ],
                    "192.168.201.0/24": {
                        "address": "192.168.201.8",
                        "available": False,
                        "last_used": "30/01/20 17:00:00"
                    }
                }
            }
        }
    }
    common_check_invalid_entry(datacenter_dict)


def test_invalid_cluster_name():
    """
    Validate that invalid values for the 'entries' attribute of a
    NetworkCollection object are ignored
    """
    datacenter_dict = deepcopy(DATA)
    datacenter_dict["Berlin"].update(
        {
            "BER_1": {
                "security_level": 3,
                "networks": {
                    "192.168.200.0/24": [
                        {
                            "address": "192.168.200.8",
                            "available": True,
                            "last_used": "30/01/20 17:00:00"
                        }
                    ]
                }
            },
            "Ber-1": {
                "security_level": 3,
                "networks": {
                    "192.168.200.0/24": [
                        {
                            "address": "192.168.200.8",
                            "available": True,
                            "last_used": "30/01/20 17:00:00"
                        }
                    ]
                }
            },
            "BER-1000": {
                "security_level": 3,
                "networks": {
                    "192.168.200.0/24": [
                        {
                            "address": "192.168.200.8",
                            "available": True,
                            "last_used": "30/01/20 17:00:00"
                        }
                    ]
                }
            },
            "~!@#$%^&*()_+": {
                "security_level": 3,
                "networks": {
                    "192.168.200.0/24": [
                        {
                            "address": "192.168.200.8",
                            "available": True,
                            "last_used": "30/01/20 17:00:00"
                        }
                    ]
                }
            },
            "XBER-1000": {
                "security_level": 3,
                "networks": {
                    "192.168.200.0/24": [
                        {
                            "address": "192.168.200.8",
                            "available": True,
                            "last_used": "30/01/20 17:00:00"
                        }
                    ]
                }
            },
            "BERL-10": {
                "security_level": 3,
                "networks": {
                    "192.168.200.0/24": [
                        {
                            "address": "192.168.200.8",
                            "available": True,
                            "last_used": "30/01/20 17:00:00"
                        }
                    ]
                }
            },
        }
    )
    common_check_invalid_entry(datacenter_dict)


def test_invalid_cluster_security_level():
    """
    Validate that invalid values for the 'security_level' attribute of a
    Cluster object are ignored
    """
    datacenter_dict = deepcopy(DATA)
    datacenter_dict["Berlin"].update(
        {
            "BER-2": {
                "security_level": "1",
                "networks": {
                    "192.168.200.0/24": [
                        {
                            "address": "192.168.200.8",
                            "available": True,
                            "last_used": "30/01/20 17:00:00"
                        }
                    ]
                }
            }
        }
    )
    common_check_invalid_entry(datacenter_dict)


def test_invalid_cluster_networks_type():
    """
    Validate that invalid values for the 'networks' attribute of a
    Cluster object are ignored
    """
    datacenter_dict = deepcopy(DATA)
    datacenter_dict["Berlin"].update(
        {
            "BER-1": {
                "security_level": 3,
                "networks": {
                    "192.168.200.0/24": [
                        {
                            "address": "192.168.200.8",
                            "available": True,
                            "last_used": "30/01/20 17:00:00"
                        }
                    ]
                }
            },
            "BER-2": {
                "security_level": 1,
                "networks": [
                    {
                        "address": "192.168.200.8",
                        "available": True,
                        "last_used": "30/01/20 17:00:00"
                    }
                ]
            }
        }
    )
    common_check_invalid_entry(datacenter_dict)


def test_invalid_datacenter_clusters_type():
    """
    Validate that invalid values for the 'clusters' attribute of a
    Cluster object are ignored
    """
    datacenter_dict = {
        "Berlin": {
            "BER-1": {
                "security_level": 3,
                "networks": {
                    "192.168.200.0/24": [
                        {
                            "address": "192.168.200.8",
                            "available": True,
                            "last_used": "30/01/20 17:00:00"
                        }
                    ]
                }
            }
        },
        "Paris": [
            {
                "security_level": 3,
                "networks": {
                    "192.168.200.0/24": [
                        {
                            "address": "192.168.200.8",
                            "available": True,
                            "last_used": "30/01/20 17:00:00"
                        }
                    ]
                }
            }
        ]
    }
    datacenters = []
    for datacenter_name, datacenter_dict in datacenter_dict.items():
        try:
            datacenters.append(
                Datacenter(datacenter_name, datacenter_dict))
        except Exception as e:
            print(str(e))
    assert len(datacenters) == 1, \
        f"Expcted only one datacenter, got {len(datacenters)}"
    datacenter_obj = datacenters[0]
    common_check_invalid_entry(datacenter_obj=datacenter_obj)


def test_records_order():
    """
    Validate that network entries are correctly ordered
    """
    datacenter_dict = deepcopy(DATA)
    datacenter_dict["Berlin"]["BER-1"]["networks"][
        "192.168.200.0/24"].append(
        {
            "address": "192.168.200.1",
            "available": False,
            "last_used": "30/01/20 16:00:00"
        }
    )
    datacenter = Datacenter("Berlin", datacenter_dict["Berlin"])
    assert datacenter.name == "Berlin",\
        f"Expected datacenter name to be Berlin, got {datacenter.name}"
    assert len(datacenter.clusters) == 1, \
        f"Expected only one cluster, got {len(datacenter.clusters)} " \
        f"clusters"
    assert datacenter.clusters[0].name == "BER-1", \
        f"Expected cluster name BER-1, got " \
        f"{datacenter.clusters[0].name}"
    assert datacenter.clusters[0].security_level == 3, \
        f"Expcetd cluster security level 3, got " \
        f"{datacenter.clusters[0].security_level}"
    assert len(datacenter.clusters[0].networks) == 1, \
        f"Expected only one cluster network, got " \
        f"{len(datacenter.clusters[0].networks)}"
    assert datacenter.clusters[0].networks[
               0].ipv4_network == IPv4Network("192.168.200.0/24"), \
        f"Expected cluster IPV4 network to be " \
        f"IPv4Network('192.168.200.0/24'), got " \
        f"{datacenter.clusters[0].networks[0].ipv4_network}"
    assert len(datacenter.clusters[0].networks[0].entries) == 2, \
        f"Expected two network entries, got " \
        f"{len(datacenter.clusters[0].networks[0].entries)}"
    assert datacenter.clusters[0].networks[0].entries[
               0].address == "192.168.200.1", \
        f"Expected network entry address '192.168.200.1', got " \
        f"{datacenter.clusters[0].networks[0].entries[0].address}"
    assert datacenter.clusters[0].networks[0].entries[
               0].available is False, \
        f"Expected network entry available field False, got " \
        f"{datacenter.clusters[0].networks[0].entries[0].available}"
    assert datacenter.clusters[0].networks[0].entries[
               0].last_used == "30/01/20 16:00:00", \
        f"Expected network entry last_used field 30/01/20 17:00:00, " \
        f"got {datacenter.clusters[0].networks[0].entries[0].last_used}"
    assert datacenter.clusters[0].networks[0].entries[
               1].address == "192.168.200.8", \
        f"Expected network entry address '192.168.200.8', got " \
        f"{datacenter.clusters[0].networks[0].entries[1].address}"
    assert datacenter.clusters[0].networks[0].entries[
               1].available is True, \
        f"Expected network entry available field True, got " \
        f"{datacenter.clusters[0].networks[0].entries[1].available}"
    assert datacenter.clusters[0].networks[0].entries[
               1].last_used == "30/01/20 17:00:00", \
        f"Expected network entry last_used field 30/01/20 17:00:00, " \
        f"got {datacenter.clusters[0].networks[0].entries[1].last_used}"


def common_check_invalid_entry(datacenter_dict=None,
                               datacenter_obj=None):
    """
    Common function used for checking the datacenter object attributes.
    """
    datacenter = Datacenter("Berlin", datacenter_dict[
        "Berlin"]) if datacenter_dict is not None else datacenter_obj
    assert datacenter.name == "Berlin", \
        f"Expected datacenter name to be Berlin, got {datacenter.name}"
    assert len(datacenter.clusters) == 1, \
        f"Expected only one cluster, got {len(datacenter.clusters)} " \
        f"clusters"
    assert datacenter.clusters[0].name == "BER-1", \
        f"Expected cluster name BER-1, got " \
        f"{datacenter.clusters[0].name}"
    assert datacenter.clusters[0].security_level == 3, \
        f"Expcetd cluster security level 3, got " \
        f"{datacenter.clusters[0].security_level}"
    assert len(datacenter.clusters[0].networks) == 1, \
        f"Expected only one cluster network, got " \
        f"{len(datacenter.clusters[0].networks)}"
    assert datacenter.clusters[0].networks[
               0].ipv4_network == IPv4Network("192.168.200.0/24"), \
        f"Expected cluster IPV4 network to be " \
        f"IPv4Network('192.168.200.0/24'), got " \
        f"{datacenter.clusters[0].networks[0].ipv4_network}"
    assert len(datacenter.clusters[0].networks[0].entries) == 1, \
        f"Expected only one network entry, got " \
        f"{len(datacenter.clusters[0].networks[0].entries)}"
    assert datacenter.clusters[0].networks[0].entries[
               0].address == "192.168.200.8", \
        f"Expected network entry address '192.168.200.8', got " \
        f"{datacenter.clusters[0].networks[0].entries[0].address}"
    assert datacenter.clusters[0].networks[0].entries[
               0].available is True, \
        f"Expected network entry available field True, got " \
        f"{datacenter.clusters[0].networks[0].entries[0].available}"
    assert datacenter.clusters[0].networks[0].entries[
               0].last_used == "30/01/20 17:00:00", \
        f"Expected network entry last_used field 30/01/20 17:00:00, " \
        f"got {datacenter.clusters[0].networks[0].entries[0].last_used}"


if __name__ == '__main__':
    test_invalid_entry_address_field()
    test_invalid_entry_available_field()
    test_invalid_entry_last_used_field()
    test_invalid_network_ipv4_network()
    test_invalid_network_entries_type()
    test_invalid_cluster_name()
    test_invalid_cluster_security_level()
    test_invalid_cluster_networks_type()
    test_invalid_datacenter_clusters_type()
    test_records_order()
