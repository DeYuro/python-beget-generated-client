import auth_generated.api.auth_service_api
from auth_generated.model.auth_auth_request import AuthAuthRequest
from client.auth_provider.auth_provider import AuthProvider
from client.vps_provider.vps_provider import VpsProvider
from client.ssh_provider.ssh_provider import SshProvider
from vps_generated.exceptions import NotFoundException
from vps_generated.exceptions import ForbiddenException
import time


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
        SshProvider(jwt)
        vps_list = self.__get_vps_list()
        self.__get_vps_info_wrong_id()
        self.__get_vps_info(vps_list[0]["id"])
        config_list, os_list = self.__get_available_configuration()
        self.__create_vps_invalid_hostname(config_id=config_list[10]["id"], os_id=os_list[0]["id"])
        vps = self.__create_vps(config_id=config_list[10]["id"], os_id=os_list[0]["id"])
        time.sleep(10)
        self.__check_running(vps["id"], "creating")
        self.__reset_password(vps["id"])
        self.__update_info(vps["id"])
        self.__reboot_vps(vps["id"])
        time.sleep(10)
        self.__check_running(vps["id"], "rebooting")
        self.__reinstall_vps(vps["id"], os_id=os_list[1]["id"])
        time.sleep(10)
        self.__check_running(vps["id"], "reinstalling")
        key = self.__add_ssh()
        self.__attach_ssh(vps["id"], key["id"])
        self.__detach_ssh(vps["id"], key["id"])
        self.__remove_ssh(key["id"])
        self.__remove_vps(vps["id"])
        self.__logout(jwt)
        self.__forbidden_request()
        print("!!!!!!!!ALL TESTS PASSED!!!!!!!" + str("\n"))

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

        return r.get("vps")

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

        return r.get("vps")

    def __get_available_configuration(self):
        print("GetAvailableConfiguration request: Expect VpsConfiguration list and OperatingSystem list" + str("\n"))
        p = VpsProvider()
        r = p.get_available_configuration()
        print(r)
        if r.get("configurations") is None:
            raise Exception("Expect VpsConfiguration list: Got None")
        if r.get("operating_systems") is None:
            raise Exception("Expect OperatingSystem list: Got None")

        return r.get("configurations"), r.get("operating_systems")

    def __create_vps_invalid_hostname(self, config_id, os_id):
        print("CreateVps request with invalid hostname: Expect {0} error".format(VpsProvider.INVALID_HOSTNAME) + str(
            "\n"))
        p = VpsProvider()
        r = p.create_vps(hostname="Invalid:Host?Name", config_id=config_id, os_id=os_id)
        print(r)
        if r.error.code != VpsProvider.INVALID_HOSTNAME:
            raise Exception("Expect {0} error: Got {1}".format(VpsProvider.INVALID_HOSTNAME, r.error.code))

    def __create_vps(self, config_id, os_id):
        print("CreateVps request with valid data: Expect: VPS status == {0}".format(VpsProvider.CREATING) + str("\n"))
        p = VpsProvider()
        r = p.create_vps(hostname="validhostname", config_id=config_id, os_id=os_id)
        print(r)

        if r["vps"]["status"] != VpsProvider.CREATING:
            raise Exception(
                "Expect: VPS status == {0}: Got {1}".format(VpsProvider.CREATING, r["vps"]["status"]) + str("\n"))

        return r.get("vps")

    def __remove_vps(self, uuid):
        print("RemoveVps request: Expect: VPS status == {0}".format(VpsProvider.REMOVING) + str("\n"))
        p = VpsProvider()
        r = p.remove_vps(uuid=uuid)
        print(r)

        if r["vps"]["status"] != VpsProvider.REMOVING:
            raise Exception(
                "Expect: VPS status == {0}: Got {1}".format(VpsProvider.REMOVING, r["vps"]["status"]) + str("\n"))

    def __check_running(self, uuid, after):
        print("Check VpsInfo after {0} vps by uuid: Expect Vps with {0} exist and status is {0}"
              .format(after, uuid, VpsProvider.RUNNING) + str("\n"))

        vps = self.__get_vps_info(uuid)

        if vps["status"] != VpsProvider.RUNNING:
            raise Exception("Expect: VPS status == {0}: Got {1}".format(VpsProvider.RUNNING, vps["status"]) + str("\n"))

    def __reset_password(self, uuid):
        print("ResetPassword request:Expect VpsInfo not None" + str("\n"))
        p = VpsProvider()
        r = p.reset_password(uuid=uuid)
        if r.get("vps") is None:
            raise Exception("Expect VpsInfo is not None: Got is None")

    def __update_info(self, uuid):
        hostname = "newhostname"
        print("UpdateInfo request with new hostname: Expect: VPS hostname == {0}".format(VpsProvider.CREATING) + str(
            "\n"))
        p = VpsProvider()
        r = p.update_info(hostname=hostname, uuid=uuid)
        print(r)

        if r["vps"]["hostname"] != hostname:
            raise Exception("Expect: VPS hostname == {0} Got {1}".format(hostname, r["vps"]["hostname"]) + str("\n"))

    def __reboot_vps(self, uuid):
        print("RebootVps request:Expect VpsInfo not None" + str("\n"))
        p = VpsProvider()
        r = p.reboot_vps(uuid=uuid)
        if r.get("vps") is None:
            raise Exception("Expect VpsInfo is not None: Got is None")

    def __reinstall_vps(self, uuid, os_id):
        print("Reinstalling request with valid data: Expect: VPS status == {0}".format(VpsProvider.REINSTALLING) + str(
            "\n"))
        p = VpsProvider()
        r = p.reinstall_vps(uuid=uuid, os_id=os_id)
        print(r)

        if r["vps"]["status"] != VpsProvider.REINSTALLING:
            raise Exception(
                "Expect: VPS status == {0}: Got {1}".format(VpsProvider.REINSTALLING, r["vps"]["status"]) + str("\n"))

    def __add_ssh(self):
        print("AddSsh request:Expect SshKey is not None" + str("\n"))
        p = SshProvider()
        r = p.add_ssh()
        print(r)

        if r.get("key") is None:
            raise Exception("Expect SshKey is not None: Got is None")

        return r.get("key")

    def __remove_ssh(self, ssh_key_id):
        print("AddSsh request:Expect removed SshKey is not None" + str("\n"))
        p = SshProvider()
        r = p.delete_ssh(str(ssh_key_id))
        print(r)

        if r.get("key") is None:
            raise Exception("Expect removed SshKey is not None: Got is None")

    def __attach_ssh(self, uuid, ssh_key_id):
        print("AttachSshKey request:Expect VPS has key with id == {0}".format(ssh_key_id) + str("\n"))
        p = VpsProvider()
        r = p.attach_ssh(uuid, str(ssh_key_id))
        print(r)

        if r["vps"]["ssh_keys"][0]["id"] != ssh_key_id:
            raise Exception(
                "Expect VPS has key with id == {0}: Got {1}".format(ssh_key_id, r["vps"]["ssh_keys"][0]["id"]))

    def __detach_ssh(self, uuid, ssh_key_id):
        print("DetachSshKey request:Expect VPS has no ssh keys".format(ssh_key_id) + str("\n"))
        p = VpsProvider()
        r = p.detach_ssh(uuid, str(ssh_key_id))
        print(r)

        if not r["vps"].get("ssh_keys"):
            return

        raise Exception("Expect VPS has no ssh keys:Got Has Keys")

    def __forbidden_request(self):
        print("Unauthorized request with wrong id: Expect 403" + str("\n"))
        p = VpsProvider()
        try:
            p.get_vps_list()
        except ForbiddenException as err:
            print(err)
            if err.status != 403:
                raise Exception("Expect 403: Got {0}".format(err.status) + str("\n"))
