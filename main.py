import time

from utils.web_utils import is_address_available

print('Starting up service...')

while True:
    is_available = is_address_available('http://www.google.com')

    if is_available:
        print('Google is available!')

    else:
        print('Google is available!')

    time.sleep(5)
