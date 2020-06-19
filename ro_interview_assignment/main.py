import logging
from sys import stdout
import requests
from time import sleep

from data_structures.datacenter import Datacenter

# logger = logging.getLogger(__name__)
# console_handler = logging.StreamHandler(stream=stdout)
# console_handler.setLevel(logging.DEBUG)
#
# # Create formatter and add it to the handler
# console_handler_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s - %(message)s')
# console_handler.setFormatter(console_handler_formatter)
#
# # Add the file handler to the logger
# logger.addHandler(console_handler)

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


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

    print(f"Fetching data from URL {url} ...")
    for retry_attempt in range(1, max_retries+1):
        try:
            server_response = requests.get(url)
            server_response_json = server_response.json()
            print(f"Data successfully fetched from attempt no. {retry_attempt}")
            return server_response_json
        except Exception as e:
            print(f"Attempt no. {retry_attempt} to fetch the data failed.  Error message: {e}")
            sleep(delay_between_retries)
    print(f"Could not fetch data")


def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')

    print("Organizing the fetched data into structures ...")
    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]

    print("Removing invalid clusters ...")
    for datacenter in datacenters:
        datacenter.remove_invalid_clusters()

    print("Removing invalid network records ...")
    for datacenter in datacenters:
        for cluster in datacenter.clusters:
            for network in cluster.networks:
                network.remove_invalid_records()

    print("Sorting network records ...")
    for datacenter in datacenters:
        for cluster in datacenter.clusters:
            for network in cluster.networks:
                network.sort_records()


if __name__ == '__main__':
    main()
