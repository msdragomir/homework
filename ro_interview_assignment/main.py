import json
import os
import time
from time import sleep

import requests

import loggin_module
from data_structures.datacenter import Datacenter

logger = loggin_module.get_logger(__name__, level="INFO")

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"
JSON_FILE_NAME = "generated_response.json"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
​
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """

    logger.info(f"Fetching data from URL {url} ...")
    for retry_attempt in range(1, max_retries+1):
        try:
            server_response = requests.get(url)
            server_response_json = server_response.json()
            logger.debug(
                f"Data successfully fetched from attempt no. "
                f"{retry_attempt}")
            return server_response_json
        except Exception as e:
            logger.warning(
                f"Attempt no. {retry_attempt} to fetch the data failed."
                f"  Error message: {e}")
            sleep(delay_between_retries)
    logger.error(f"Could not fetch data")


def dump_datacenter_to_file(datacenter_list):
    """
    Write the datacenter data to JSON file
    """
    # Buiding dict with datacenter data
    datacenters_dict = {}
    for datacenter in datacenter_list:
        datacenters_dict.update(
            {
                datacenter.name: {}
            }
        )
        for cluster in datacenter.clusters:
            datacenters_dict[datacenter.name].update(
                {
                    cluster.name: {
                        "security_level": cluster.security_level,
                        "networks": {}
                    }
                }
            )
            for network in cluster.networks:
                datacenters_dict[datacenter.name][cluster.name][
                    "networks"].update(
                    {
                        str(network.ipv4_network): []
                    }
                )
                for entry in network.entries:
                    datacenters_dict[datacenter.name][cluster.name][
                        "networks"][str(network.ipv4_network)].append(
                        {
                            "address": entry.address,
                            "available": entry.available,
                            "last_used": entry.last_used
                        }
                    )

    # Dumping datacenter data to file
    json_path = os.path.join(os.getcwd(), JSON_FILE_NAME)
    with open(json_path, "w") as json_file:
        json.dump(datacenters_dict, json_file, indent=2)
    logger.info(f"Datacenter data written to {json_path}")


def generate_bigger_data_set():
    """
    Generate bigger datacenter data
    """
    big_data_set = {
        "Berlin": {},
        "Paris": {},
        "Amsterdam": {},
        "Bucharest": {},
        "Madrid": {},
        "London": {},
        "Prague": {},
        "Roma": {},
        "Stockholm": {},
        "Vienna": {}
    }
    for datacenter_name in big_data_set:
        for cluster_number in range(1, 1001):
            cluster_name = \
                f"{datacenter_name[:3].upper()}-{cluster_number}"
            big_data_set[datacenter_name].update(
                {
                    cluster_name: {
                        "security_level": 1,
                        "networks": {
                            "192.168.0.0/24": [
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
                                    "address": "192.168.0.288",
                                    "available": False,
                                    "last_used": "30/01/20 17:00:00"
                                },
                                {
                                    "address": "invalid",
                                    "available": True,
                                    "last_used": "30/01/20 17:00:00"
                                },
                                {
                                    "address": "192.168.0.1",
                                    "available": False,
                                    "last_used": "30/01/20 16:00:00"
                                },
                                {
                                    "address": "192.168.0.4",
                                    "available": True,
                                    "last_used": "30/01/20 17:00:00"
                                },
                                {
                                    "address": "192.168.0.2",
                                    "available": False,
                                    "last_used": "30/01/20 17:00:00"
                                },
                                {
                                    "address": "192.168.0.3",
                                    "available": True,
                                    "last_used": "30/01/20 17:00:00"
                                },
                                {
                                    "address": "192.168.1.1",
                                    "available": True,
                                    "last_used": "30/01/20 17:00:00"
                                }
                            ],
                            "10.0.8.0/22": [
                                {
                                    "address": "10.0.11.254",
                                    "available": True,
                                    "last_used": "30/01/20 17:00:00"
                                },
                                {
                                    "address": "10.0.8.1",
                                    "available": False,
                                    "last_used": "30/01/20 16:00:00"
                                },
                                {
                                    "address": "10.0.8.0",
                                    "available": False,
                                    "last_used": "30/01/20 16:00:00"
                                },
                                {
                                    "address": "10.0.12.1",
                                    "available": True,
                                    "last_used": "30/01/20 17:00:00"
                                },
                                {
                                    "address": "10.0.10.a",
                                    "available": False,
                                    "last_used": "30/01/20 17:00:00"
                                }
                            ],
                            "192.168.10.0/24": [
                                {
                                    "address": "192.168.10.8",
                                    "available": True,
                                    "last_used": "30/01/20 17:00:00"
                                },
                                {
                                    "address": "192.168.10.5",
                                    "available": False,
                                    "last_used": "30/01/20 17:00:00"
                                },
                                {
                                    "address": "192.168.10.6",
                                    "available": False,
                                    "last_used": "30/01/20 17:00:00"
                                },
                                {
                                    "address": "192.168.0.7",
                                    "available": True,
                                    "last_used": "30/01/20 17:00:00"
                                }
                            ],
                            "192.168.11.0/24": [
                                {
                                    "address": "192.168.11.1",
                                    "available": True,
                                    "last_used": "30/01/20 17:00:00"
                                },
                                {
                                    "address": "192.168.2.1",
                                    "available": False,
                                    "last_used": "30/01/20 17:00:00"
                                },
                                {
                                    "address": "192.168.11.522",
                                    "available": False,
                                    "last_used": "30/01/20 17:00:00"
                                }
                            ],
                            "192.168.100.0/24": [
                                {
                                    "address": "192.168.100.1",
                                    "available": True,
                                    "last_used": "30/01/20 17:00:00"
                                }
                            ],
                            "192.168.200.0/24": [
                                {
                                    "address": "192.168.200.8",
                                    "available": True,
                                    "last_used": "30/01/20 17:00:00"
                                }
                            ],
                            "192.168.203.0/24": [
                                {
                                    "address": "192.168.203.20",
                                    "available": True,
                                    "last_used": "30/01/20 17:00:00"
                                },
                                {
                                    "address": "192.168.203.21",
                                    "available": False,
                                    "last_used": "30/01/20 17:00:00"
                                },
                                {
                                    "address": "192.168.203.19",
                                    "available": False,
                                    "last_used": "30/01/20 17:00:00"
                                },
                                {
                                    "address": "192.168.0.0",
                                    "available": True,
                                    "last_used": "30/01/20 17:00:00"
                                }
                            ]
                        }
                    },
                    "TEST-1": {
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
                    "TEST-2": {
                        "security_level": "3",
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
                    "TEST-3": {
                        "security_level": 3,
                        "networks": [
                            {
                                "address": "192.168.200.8",
                                "available": True,
                                "last_used": "30/01/20 17:00:00"
                            }
                        ]
                    },
                    "TEST-4": {
                        "security_level": 3,
                        "networks": {
                            "192.168.200.0/245": [
                                {
                                    "address": "192.168.200.8",
                                    "available": True,
                                    "last_used": "30/01/20 17:00:00"
                                }
                            ]
                        }
                    },
                    "TEST-5": {
                        "security_level": 3,
                        "networks": {
                            "192.168.200.0/24": {
                                "address": "192.168.200.8",
                                "available": True,
                                "last_used": "30/01/20 17:00:00"
                            }
                        }
                    },
                    "TEST-6": {
                        "security_level": 3,
                        "networks": {
                            "192.168.200.0/24": [
                                {
                                    "address": 1,
                                    "available": True,
                                    "last_used": "30/01/20 17:00:00"
                                }
                            ]
                        }
                    },
                    "TEST-7": {
                        "security_level": 3,
                        "networks": {
                            "192.168.200.0/24": [
                                {
                                    "address": "192.168.200.8",
                                    "available": "True",
                                    "last_used": "30/01/20 17:00:00"
                                }
                            ]
                        }
                    },
                    "TEST-8": {
                        "security_level": 3,
                        "networks": {
                            "192.168.200.0/24": [
                                {
                                    "address": "192.168.200.8",
                                    "available": True,
                                    "last_used": "some_str"
                                }
                            ]
                        }
                    },
                }
            )
    return big_data_set


def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)
    # data = generate_bigger_data_set()

    if not data:
        raise ValueError('No data to process')

    start_time = time.time()

    logger.info("Organizing the fetched data into structures ...")
    datacenters = []
    for datacenter_name, datacenter_dict in data.items():
        try:
            datacenters.append(Datacenter(datacenter_name,
                                          datacenter_dict))
        except Exception as e:
            logger.error(str(e))

    data_processing_time = time.time() - start_time

    logger.info("Dumping datacenter data to file ...")
    dump_datacenter_to_file(datacenters)

    logger.info(
        f"Datacenter processing time: {data_processing_time} seconds")


if __name__ == '__main__':
    main()
