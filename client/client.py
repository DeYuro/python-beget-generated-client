import auth_generated.api.auth_service_api
from auth_generated.model.auth_auth_request import AuthAuthRequest
from client.auth_provider.auth_provider import AuthProvider
from client.vps_provider.vps_provider import VpsProvider
from vps_generated.exceptions import NotFoundException


class Test:
    login = ''
    password = ''

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def run(self):
        self.__wrong_data_auth()
        self.__empty_login_auth()
        jwt = self.__auth()
        VpsProvider(jwt)
        vps_list = self.__get_vps_list()
        self.__get_vps_info_wrong_id()
        self.__get_vps_info(vps_list["vps"][0]["id"])
        self.__logout(jwt)

    def __wrong_data_auth(self):
        print("Auth wrong credential request: Expect {0} error".format(AuthProvider.INCORRECT_CREDENTIALS) + str("\n"))
        p = AuthProvider()
        r = p.auth(login="wrong", password="credential")
        print(r)
        if r.error != AuthProvider.INCORRECT_CREDENTIALS:
            raise Exception("Expect {0} error: Got {1}".format(AuthProvider.INCORRECT_CREDENTIALS, r.error))

    def __empty_login_auth(self):
        print("Empty login auth request: Expect {0} error".format(AuthProvider.EMPTY_LOGIN) + str("\n"))
        p = AuthProvider()
        r = p.auth(login="", password="credential")
        print(r)
        if r.error != AuthProvider.EMPTY_LOGIN:
            raise Exception("Expect {0} error: Got {1}".format(AuthProvider.EMPTY_LOGIN, r.error))

    def __auth(self):
        print("Auth correct credential request: Expect Token is not None" + str("\n"))
        p = AuthProvider()
        r = p.auth(login=self.login, password=self.password)
        print(r)
        if r.token is None:
            raise Exception("Expect Token is not None: Got is None".format(AuthProvider.EMPTY_LOGIN, r.error))
        return r.token

    def __logout(self, jwt):
        print("Logout request: Expect no errors" + str("\n"))
        p = AuthProvider(jwt)
        r = p.logout()
        print(r)

    def __get_vps_list(self):
        print("GetVpsList request: Expect customer vps list" + str("\n"))

        p = VpsProvider()
        r = p.get_vps_list()
        print(r)

        return r

    def __get_vps_info_wrong_id(self):
        print("GetVpsInfo request with wrong id: Expect 404" + str("\n"))
        p = VpsProvider()
        try:
            r = p.get_vps_info("qwerty")
        except NotFoundException as err:
            print(err)
            if err.status != 404:
                raise Exception("Expect 404: Got {0}".format(err.status) + str("\n"))

    def __get_vps_info(self, uuid):
        print("GetVpsInfo request correct id: Expect VpsInfo is not None" + str("\n"))
        p = VpsProvider()
        r = p.get_vps_info(uuid)
        print(r)

        if r.get("vps") is None:
            raise Exception("Expect VpsInfo is not None: Got is None")
