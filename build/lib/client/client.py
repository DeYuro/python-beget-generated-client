from internal.apiclient.auth.openapi_client.api.auth_service_api import AuthServiceApi
from internal.apiclient.auth.openapi_client.model.auth_auth_request import AuthAuthRequest
class Test:
    def __init__(self, login, password):
        self.login = login,
        self.password = password

    def run(self):
        self.__wrong_data_auth()

    def __wrong_data_auth(self):
        print("Auth wrong credential request: Expect {0} error" + str("\n").format("test"))
        req = AuthAuthRequest(login=self.login, password=self.password)
        api = AuthServiceApi()
        res = api.auth_service_auth(auth_auth_request=req)

        return res



