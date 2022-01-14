from vps_generated.api.manage_service_api import ManageServiceApi
from vps_generated.configuration import Configuration
from vps_generated.api_client import ApiClient


class VpsProvider(object):
    INVALID_HOSTNAME = "INVALID_HOSTNAME"
    REMOVING = "REMOVING"
    CREATING = "CREATING"
    RUNNING = "RUNNING"
    RESTARTING = "RESTARTING"
    REINSTALLING = "REINSTALLING"

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(VpsProvider, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self, jwt=None):
        if self.__initialized:
            return
        config = Configuration(access_token=jwt)
        client = ApiClient(configuration=config)
        self.api = ManageServiceApi(api_client=client)
        self.__initialized = True

    def get_vps_list(self):
        return self.api.manage_service_get_list()

    def get_vps_info(self, uuid):
        return self.api.manage_service_get_info(uuid)
