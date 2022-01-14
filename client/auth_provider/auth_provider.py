from auth_generated.api.auth_service_api import AuthServiceApi
from auth_generated.model.auth_auth_request import AuthAuthRequest
from auth_generated.configuration import Configuration
from auth_generated.api_client import ApiClient


class AuthProvider(object):
    INCORRECT_CREDENTIALS = "INCORRECT_CREDENTIALS"
    EMPTY_LOGIN = "EMPTY_LOGIN"

    def __init__(self, jwt=None):
        client = ApiClient()
        if jwt is not None:
            config = Configuration(access_token=jwt)
            client = ApiClient(configuration=config)
        self.api = AuthServiceApi(api_client=client)

    def auth(self, login, password):
        req = AuthAuthRequest(login=login, password=password)
        return self.api.auth_service_auth(auth_auth_request=req)

    def logout(self):
        return self.api.auth_service_logout()
