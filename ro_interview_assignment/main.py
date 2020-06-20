from time import sleep

import requests

import loggin_module
from data_structures.datacenter import Datacenter

logger = loggin_module.get_logger(__name__, level="INFO")

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


def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')

    logger.info("Organizing the fetched data into structures ...")
    datacenters = []
    for datacenter_name, datacenter_dict in data.items():
        try:
            datacenters.append(Datacenter(datacenter_name,
                                          datacenter_dict))
        except Exception as e:
            logger.error(str(e))


if __name__ == '__main__':
    main()
