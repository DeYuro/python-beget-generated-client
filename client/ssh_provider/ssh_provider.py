from vps_generated.api.ssh_key_service_api import SshKeyServiceApi
from vps_generated.configuration import Configuration
from vps_generated.api_client import ApiClient
from vps_generated.model.ssh_key_add_request import SshKeyAddRequest


class SshProvider(object):
    DUMMY_PUBLIC_KEY = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCxmMK5s2UEVVRXITbIlYDvQjWfaWStBOi5JdnpWtFnOofWg6o2tD5qQNl4NycmcS8XMZ3gWlNpsOtoV9IHPrypKlWjL8f0YHxdL3YDMa33OW6TM/Nj2mZe0AvIbCF/wBvn99GOh2D0R+yhoBDRT+8+Bn1zRRmddF+YlD60Z6GXS5tLOtmLr2tkVaLgtNug0KNg6NoL7iSB5BU0fN/9Dkr3Gg1jaVCrjcY4cR9f3axBGI+XXs7D/7DXGqJKyZS384cBbyHTaK8cMQDL5WcJa/eyBCt/pkXYANb483NLRQr0TPML8tCgAG9ZuErbJpubX4gHEW9VxfpEp9hdHSaFUXux \n"

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(SshProvider, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self, jwt=None):
        if self.__initialized:
            return
        config = Configuration(access_token=jwt)
        client = ApiClient(configuration=config)
        self.api = SshKeyServiceApi(api_client=client)
        self.__initialized = True

    def add_ssh(self):
        req = SshKeyAddRequest(name="python generated client dummy key", public_key=self.DUMMY_PUBLIC_KEY)
        return self.api.ssh_key_service_add(ssh_key_add_request=req)

    def delete_ssh(self, ssh_key_id):
        return self.api.ssh_key_service_remove(id=ssh_key_id)
