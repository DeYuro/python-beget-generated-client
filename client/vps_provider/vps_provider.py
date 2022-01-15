from vps_generated.api.manage_service_api import ManageServiceApi
from vps_generated.configuration import Configuration
from vps_generated.api_client import ApiClient
from vps_generated.model.manage_create_vps_request import ManageCreateVpsRequest
from vps_generated.model.manage_update_info_request import ManageUpdateInfoRequest
from vps_generated.model.manage_reinstall_request import ManageReinstallRequest


class VpsProvider(object):
    INVALID_HOSTNAME = "INVALID_HOSTNAME"
    REMOVING = "REMOVING"
    CREATING = "CREATING"
    RUNNING = "RUNNING"
    RESTARTING = "RESTARTING"
    REINSTALLING = "REINSTALLING"

    VPS_PASSWORD = "L%v2sZ2j"
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

    def get_available_configuration(self):
        return self.api.manage_service_get_available_configuration()

    def create_vps(self, hostname, config_id, os_id):
        req = ManageCreateVpsRequest(hostname=hostname,
                                     description="Test client from generated code",
                                     password=self.VPS_PASSWORD,
                                     beget_ssh_access_allowed=True,
                                     display_name="Python Generated Client",
                                     configuration_id=config_id,
                                     operating_system_id=os_id)
        return self.api.manage_service_create_vps(manage_create_vps_request=req)

    def remove_vps(self, uuid):
        return self.api.manage_service_remove_vps(id=uuid)

    def reset_password(self, uuid):
        return self.api.manage_service_reset_password(id=uuid)

    def reboot_vps(self, uuid):
        return self.api.manage_service_reboot_vps(id=uuid)

    def update_info(self, hostname, uuid):
        req = ManageUpdateInfoRequest(hostname=hostname,
                                      description="Test client from generated code",
                                      display_name="Python Generated Client", )
        return self.api.manage_service_update_info(id=uuid, manage_update_info_request=req)

    def reinstall_vps(self, uuid, os_id):
        req = ManageReinstallRequest(password=self.VPS_PASSWORD, operating_system_id=os_id)
        return self.api.manage_service_reinstall(id=uuid, manage_reinstall_request=req)

    def attach_ssh(self, uuid, ssh_key_id):
        return self.api.manage_service_attach_ssh_key(id=uuid, ssh_key_id=ssh_key_id)

    def detach_ssh(self, uuid, ssh_key_id):
        return self.api.manage_service_detach_ssh_key(id=uuid, ssh_key_id=ssh_key_id)
