"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import unittest

import auth_generated
from auth_generated.api.auth_service_api import AuthServiceApi  # noqa: E501


class TestAuthServiceApi(unittest.TestCase):
    """AuthServiceApi unit test stubs"""

    def setUp(self):
        self.api = AuthServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_auth_service_auth(self):
        """Test case for auth_service_auth

        """
        pass

    def test_auth_service_logout(self):
        """Test case for auth_service_logout

        """
        pass

    def test_auth_service_refresh_token(self):
        """Test case for auth_service_refresh_token

        """
        pass

    def test_auth_service_switch_user(self):
        """Test case for auth_service_switch_user

        """
        pass


if __name__ == '__main__':
    unittest.main()