import unittest
import requests


def is_address_available(address):
    '''
    Uses requests library to determine if a web address is available.
    :param address: Target web address. Address is assumed to be valid
    :return: True if a GET request sent to the target address returns a 200 status code. False otherwise.
    '''

    response = requests.get(address)
    return response.status_code == 200


if __name__ == '__main__':
    unittest.main()
