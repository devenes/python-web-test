from unittest import mock, TestCase
from requests import Response

from utils import web_utils


class TestWebUtils(TestCase):

    def _is_address_available_helper(self, patch_status_code, target_address, expected_result):
        with mock.patch('utils.web_utils.requests.get') as patched_get:
            response = Response()
            response.status_code = patch_status_code
            patched_get.return_value = response

            result = web_utils.is_address_available(target_address)
            self.assertEqual(
                result, expected_result, f'Expected result: {expected_result} Actual result: {result}')

    def test_is_address_available_returns_true_on_200_status(self):
        self._is_address_available_helper(200, 'http://www.google.com', True)

    def test_is_address_available_returns_false_on_non_200_status(self):
        self._is_address_available_helper(
            500, 'http://www.notavailable.com', False)
