# vps-generated
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The `vps_generated` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage

This python library package is generated without supporting files like setup.py or requirements files

To be able to use it, you will need these dependencies in your own package that uses this library:

* urllib3 >= 1.25.3
* python-dateutil

## Getting Started

In your own code, to use this library to connect and interact with vps-generated,
you can run the following:

```python

import time
import vps_generated
from pprint import pprint
from vps_generated.api import backup_service_api
from vps_generated.model.backup_get_available_copies_response import BackupGetAvailableCopiesResponse
from vps_generated.model.backup_get_backup_file_list_response import BackupGetBackupFileListResponse
from vps_generated.model.backup_get_orders_response import BackupGetOrdersResponse
from vps_generated.model.backup_restore_file_request import BackupRestoreFileRequest
from vps_generated.model.backup_restore_file_response import BackupRestoreFileResponse
from vps_generated.model.backup_restore_server_request import BackupRestoreServerRequest
from vps_generated.model.backup_restore_server_response import BackupRestoreServerResponse
# Defining the host is optional and defaults to https://api.beget.com
# See configuration.py for a list of all supported configuration parameters.
configuration = vps_generated.Configuration(
    host = "https://api.beget.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = vps_generated.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)


# Enter a context with an instance of the API client
with vps_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backup_service_api.BackupServiceApi(api_client)
    
    try:
        api_response = api_instance.backup_service_get_available_copies()
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling BackupServiceApi->backup_service_get_available_copies: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.beget.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BackupServiceApi* | [**backup_service_get_available_copies**](vps_generated/docs/BackupServiceApi.md#backup_service_get_available_copies) | **GET** /v1/vps/backup | 
*BackupServiceApi* | [**backup_service_get_backup_file_list**](vps_generated/docs/BackupServiceApi.md#backup_service_get_backup_file_list) | **GET** /v1/vps/{id}/backup/{copy_id} | 
*BackupServiceApi* | [**backup_service_get_orders**](vps_generated/docs/BackupServiceApi.md#backup_service_get_orders) | **GET** /v1/vps/backup/orders | 
*BackupServiceApi* | [**backup_service_restore_file**](vps_generated/docs/BackupServiceApi.md#backup_service_restore_file) | **POST** /v1/vps/{id}/backup/{copy_id}/file | 
*BackupServiceApi* | [**backup_service_restore_server**](vps_generated/docs/BackupServiceApi.md#backup_service_restore_server) | **POST** /v1/vps/{id}/backup/{copy_id}/server | 
*ManageServiceApi* | [**manage_service_attach_ip_address**](vps_generated/docs/ManageServiceApi.md#manage_service_attach_ip_address) | **POST** /v1/vps/{id}/network/{ip_address} | 
*ManageServiceApi* | [**manage_service_attach_ssh_key**](vps_generated/docs/ManageServiceApi.md#manage_service_attach_ssh_key) | **POST** /v1/vps/{id}/sshKey/{ssh_key_id} | 
*ManageServiceApi* | [**manage_service_attach_to_private_network**](vps_generated/docs/ManageServiceApi.md#manage_service_attach_to_private_network) | **POST** /v1/vps/{id}/private-network/{network_id} | 
*ManageServiceApi* | [**manage_service_change_configuration**](vps_generated/docs/ManageServiceApi.md#manage_service_change_configuration) | **PUT** /v1/vps/server/{id}/configuration | 
*ManageServiceApi* | [**manage_service_change_ssh_access**](vps_generated/docs/ManageServiceApi.md#manage_service_change_ssh_access) | **PUT** /v1/vps/{id}/ssh/access | 
*ManageServiceApi* | [**manage_service_check_software_requirements**](vps_generated/docs/ManageServiceApi.md#manage_service_check_software_requirements) | **POST** /v1/vps/software/requirements | 
*ManageServiceApi* | [**manage_service_create_vps**](vps_generated/docs/ManageServiceApi.md#manage_service_create_vps) | **POST** /v1/vps/server | 
*ManageServiceApi* | [**manage_service_detach_from_private_network**](vps_generated/docs/ManageServiceApi.md#manage_service_detach_from_private_network) | **DELETE** /v1/vps/{id}/private-network/{network_id} | 
*ManageServiceApi* | [**manage_service_detach_ip_address**](vps_generated/docs/ManageServiceApi.md#manage_service_detach_ip_address) | **DELETE** /v1/vps/network/detach/{ip_address} | 
*ManageServiceApi* | [**manage_service_detach_ssh_key**](vps_generated/docs/ManageServiceApi.md#manage_service_detach_ssh_key) | **DELETE** /v1/vps/{id}/sshKey/{ssh_key_id} | 
*ManageServiceApi* | [**manage_service_get_available_configuration**](vps_generated/docs/ManageServiceApi.md#manage_service_get_available_configuration) | **GET** /v1/vps/configuration | 
*ManageServiceApi* | [**manage_service_get_available_software**](vps_generated/docs/ManageServiceApi.md#manage_service_get_available_software) | **GET** /v1/vps/software | 
*ManageServiceApi* | [**manage_service_get_file_manager_settings**](vps_generated/docs/ManageServiceApi.md#manage_service_get_file_manager_settings) | **POST** /v1/vps/{id}/fm | 
*ManageServiceApi* | [**manage_service_get_history**](vps_generated/docs/ManageServiceApi.md#manage_service_get_history) | **GET** /v1/vps/{id}/history | 
*ManageServiceApi* | [**manage_service_get_info**](vps_generated/docs/ManageServiceApi.md#manage_service_get_info) | **GET** /v1/vps/server/{id} | 
*ManageServiceApi* | [**manage_service_get_installed_software**](vps_generated/docs/ManageServiceApi.md#manage_service_get_installed_software) | **GET** /v1/vps/{id}/software | 
*ManageServiceApi* | [**manage_service_get_list**](vps_generated/docs/ManageServiceApi.md#manage_service_get_list) | **GET** /v1/vps/server/list | 
*ManageServiceApi* | [**manage_service_get_statuses**](vps_generated/docs/ManageServiceApi.md#manage_service_get_statuses) | **GET** /v1/vps/server/statuses | 
*ManageServiceApi* | [**manage_service_reboot_vps**](vps_generated/docs/ManageServiceApi.md#manage_service_reboot_vps) | **POST** /v1/vps/server/{id}/reboot | 
*ManageServiceApi* | [**manage_service_reinstall**](vps_generated/docs/ManageServiceApi.md#manage_service_reinstall) | **POST** /v1/vps/server/{id}/reinstall | 
*ManageServiceApi* | [**manage_service_remove_vps**](vps_generated/docs/ManageServiceApi.md#manage_service_remove_vps) | **POST** /v1/vps/server/{id}/remove | 
*ManageServiceApi* | [**manage_service_reset_password**](vps_generated/docs/ManageServiceApi.md#manage_service_reset_password) | **PUT** /v1/vps/{id}/password | 
*ManageServiceApi* | [**manage_service_reset_vps**](vps_generated/docs/ManageServiceApi.md#manage_service_reset_vps) | **POST** /v1/vps/server/{id}/reset | 
*ManageServiceApi* | [**manage_service_start_rescue**](vps_generated/docs/ManageServiceApi.md#manage_service_start_rescue) | **POST** /v1/vps/server/{id}/rescue | 
*ManageServiceApi* | [**manage_service_start_vps**](vps_generated/docs/ManageServiceApi.md#manage_service_start_vps) | **POST** /v1/vps/server/{id}/start | 
*ManageServiceApi* | [**manage_service_stop_rescue**](vps_generated/docs/ManageServiceApi.md#manage_service_stop_rescue) | **DELETE** /v1/vps/server/{id}/rescue | 
*ManageServiceApi* | [**manage_service_stop_vps**](vps_generated/docs/ManageServiceApi.md#manage_service_stop_vps) | **POST** /v1/vps/server/{id}/stop | 
*ManageServiceApi* | [**manage_service_unarchive**](vps_generated/docs/ManageServiceApi.md#manage_service_unarchive) | **DELETE** /v1/vps/archive/{id} | 
*ManageServiceApi* | [**manage_service_update_info**](vps_generated/docs/ManageServiceApi.md#manage_service_update_info) | **PUT** /v1/vps/server/{id}/info | 
*NetworkServiceApi* | [**network_service_create_private_network**](vps_generated/docs/NetworkServiceApi.md#network_service_create_private_network) | **POST** /v1/vps/private-network | 
*NetworkServiceApi* | [**network_service_get_network_info**](vps_generated/docs/NetworkServiceApi.md#network_service_get_network_info) | **GET** /v1/vps/network | 
*NetworkServiceApi* | [**network_service_order_ip_address**](vps_generated/docs/NetworkServiceApi.md#network_service_order_ip_address) | **POST** /v1/vps/network | 
*NetworkServiceApi* | [**network_service_remove_ip_address**](vps_generated/docs/NetworkServiceApi.md#network_service_remove_ip_address) | **DELETE** /v1/vps/network/{ip_address} | 
*NetworkServiceApi* | [**network_service_suggest_private_address**](vps_generated/docs/NetworkServiceApi.md#network_service_suggest_private_address) | **POST** /v1/vps/private-network/{network_id}/suggested-address | 
*SnapshotServiceApi* | [**snapshot_service_create**](vps_generated/docs/SnapshotServiceApi.md#snapshot_service_create) | **POST** /v1/vps/snapshot | 
*SnapshotServiceApi* | [**snapshot_service_create_calculator**](vps_generated/docs/SnapshotServiceApi.md#snapshot_service_create_calculator) | **POST** /v1/vps/snapshot/calculator | 
*SnapshotServiceApi* | [**snapshot_service_edit**](vps_generated/docs/SnapshotServiceApi.md#snapshot_service_edit) | **PUT** /v1/vps/snapshot/{id} | 
*SnapshotServiceApi* | [**snapshot_service_get_all**](vps_generated/docs/SnapshotServiceApi.md#snapshot_service_get_all) | **GET** /v1/vps/snapshot | 
*SnapshotServiceApi* | [**snapshot_service_get_all_restores**](vps_generated/docs/SnapshotServiceApi.md#snapshot_service_get_all_restores) | **GET** /v1/vps/snapshot/restore | 
*SnapshotServiceApi* | [**snapshot_service_remove**](vps_generated/docs/SnapshotServiceApi.md#snapshot_service_remove) | **DELETE** /v1/vps/snapshot/{id} | 
*SnapshotServiceApi* | [**snapshot_service_restore**](vps_generated/docs/SnapshotServiceApi.md#snapshot_service_restore) | **POST** /v1/vps/snapshot/{id}/restore | 
*SshKeyServiceApi* | [**ssh_key_service_add**](vps_generated/docs/SshKeyServiceApi.md#ssh_key_service_add) | **POST** /v1/vps/sshKey | 
*SshKeyServiceApi* | [**ssh_key_service_get_all**](vps_generated/docs/SshKeyServiceApi.md#ssh_key_service_get_all) | **GET** /v1/vps/sshKey | 
*SshKeyServiceApi* | [**ssh_key_service_remove**](vps_generated/docs/SshKeyServiceApi.md#ssh_key_service_remove) | **DELETE** /v1/vps/sshKey/{id} | 
*StatisticServiceApi* | [**statistic_service_get_cpu**](vps_generated/docs/StatisticServiceApi.md#statistic_service_get_cpu) | **GET** /v1/vps/statistic/cpu/{id} | 
*StatisticServiceApi* | [**statistic_service_get_cpu_details**](vps_generated/docs/StatisticServiceApi.md#statistic_service_get_cpu_details) | **GET** /v1/vps/statistic/cpu-details/{id} | 
*StatisticServiceApi* | [**statistic_service_get_disk**](vps_generated/docs/StatisticServiceApi.md#statistic_service_get_disk) | **GET** /v1/vps/statistic/disk/{id} | 
*StatisticServiceApi* | [**statistic_service_get_disk_usage**](vps_generated/docs/StatisticServiceApi.md#statistic_service_get_disk_usage) | **GET** /v1/vps/statistic/disk-usage/{id} | 
*StatisticServiceApi* | [**statistic_service_get_load_average**](vps_generated/docs/StatisticServiceApi.md#statistic_service_get_load_average) | **GET** /v1/vps/statistic/load-average/{id} | 
*StatisticServiceApi* | [**statistic_service_get_memory**](vps_generated/docs/StatisticServiceApi.md#statistic_service_get_memory) | **GET** /v1/vps/statistic/memory/{id} | 
*StatisticServiceApi* | [**statistic_service_get_network**](vps_generated/docs/StatisticServiceApi.md#statistic_service_get_network) | **GET** /v1/vps/statistic/network/{id} | 
*StatisticServiceApi* | [**statistic_service_get_process_list**](vps_generated/docs/StatisticServiceApi.md#statistic_service_get_process_list) | **GET** /v1/vps/statistic/processes/{id} | 


## Documentation For Models

 - [BackupGetAvailableCopiesResponse](vps_generated/docs/BackupGetAvailableCopiesResponse.md)
 - [BackupGetBackupFileListResponse](vps_generated/docs/BackupGetBackupFileListResponse.md)
 - [BackupGetOrdersResponse](vps_generated/docs/BackupGetOrdersResponse.md)
 - [BackupRestoreFileRequest](vps_generated/docs/BackupRestoreFileRequest.md)
 - [BackupRestoreFileResponse](vps_generated/docs/BackupRestoreFileResponse.md)
 - [BackupRestoreFileResponseError](vps_generated/docs/BackupRestoreFileResponseError.md)
 - [BackupRestoreServerRequest](vps_generated/docs/BackupRestoreServerRequest.md)
 - [BackupRestoreServerResponse](vps_generated/docs/BackupRestoreServerResponse.md)
 - [BackupRestoreServerResponseError](vps_generated/docs/BackupRestoreServerResponseError.md)
 - [ManageAttachIpAddressRequest](vps_generated/docs/ManageAttachIpAddressRequest.md)
 - [ManageAttachIpAddressResponse](vps_generated/docs/ManageAttachIpAddressResponse.md)
 - [ManageAttachIpAddressResponseError](vps_generated/docs/ManageAttachIpAddressResponseError.md)
 - [ManageAttachSshKeyResponse](vps_generated/docs/ManageAttachSshKeyResponse.md)
 - [ManageAttachSshKeyResponseError](vps_generated/docs/ManageAttachSshKeyResponseError.md)
 - [ManageAttachToPrivateNetworkRequest](vps_generated/docs/ManageAttachToPrivateNetworkRequest.md)
 - [ManageAttachToPrivateNetworkResponse](vps_generated/docs/ManageAttachToPrivateNetworkResponse.md)
 - [ManageAttachToPrivateNetworkResponseError](vps_generated/docs/ManageAttachToPrivateNetworkResponseError.md)
 - [ManageChangeConfigurationRequest](vps_generated/docs/ManageChangeConfigurationRequest.md)
 - [ManageChangeConfigurationResponse](vps_generated/docs/ManageChangeConfigurationResponse.md)
 - [ManageChangeConfigurationResponseError](vps_generated/docs/ManageChangeConfigurationResponseError.md)
 - [ManageChangeSshAccessRequest](vps_generated/docs/ManageChangeSshAccessRequest.md)
 - [ManageChangeSshAccessResponse](vps_generated/docs/ManageChangeSshAccessResponse.md)
 - [ManageChangeSshAccessResponseError](vps_generated/docs/ManageChangeSshAccessResponseError.md)
 - [ManageCheckSoftwareRequirementsRequest](vps_generated/docs/ManageCheckSoftwareRequirementsRequest.md)
 - [ManageCheckSoftwareRequirementsResponse](vps_generated/docs/ManageCheckSoftwareRequirementsResponse.md)
 - [ManageCheckSoftwareRequirementsResponseError](vps_generated/docs/ManageCheckSoftwareRequirementsResponseError.md)
 - [ManageCreateVpsRequest](vps_generated/docs/ManageCreateVpsRequest.md)
 - [ManageCreateVpsResponse](vps_generated/docs/ManageCreateVpsResponse.md)
 - [ManageCreateVpsResponseError](vps_generated/docs/ManageCreateVpsResponseError.md)
 - [ManageCreateVpsResponseErrorSoftwareVariableError](vps_generated/docs/ManageCreateVpsResponseErrorSoftwareVariableError.md)
 - [ManageDetachFromPrivateNetworkResponse](vps_generated/docs/ManageDetachFromPrivateNetworkResponse.md)
 - [ManageDetachFromPrivateNetworkResponseError](vps_generated/docs/ManageDetachFromPrivateNetworkResponseError.md)
 - [ManageDetachIpAddressResponse](vps_generated/docs/ManageDetachIpAddressResponse.md)
 - [ManageDetachIpAddressResponseError](vps_generated/docs/ManageDetachIpAddressResponseError.md)
 - [ManageDetachSshKeyResponse](vps_generated/docs/ManageDetachSshKeyResponse.md)
 - [ManageDetachSshKeyResponseError](vps_generated/docs/ManageDetachSshKeyResponseError.md)
 - [ManageGetAvailableConfigurationResponse](vps_generated/docs/ManageGetAvailableConfigurationResponse.md)
 - [ManageGetAvailableSoftwareResponse](vps_generated/docs/ManageGetAvailableSoftwareResponse.md)
 - [ManageGetAvailableSoftwareResponseSoftwareInfo](vps_generated/docs/ManageGetAvailableSoftwareResponseSoftwareInfo.md)
 - [ManageGetAvailableSoftwareResponseSoftwareInfoRequirements](vps_generated/docs/ManageGetAvailableSoftwareResponseSoftwareInfoRequirements.md)
 - [ManageGetFileManagerSettingsResponse](vps_generated/docs/ManageGetFileManagerSettingsResponse.md)
 - [ManageGetFileManagerSettingsResponseCredentials](vps_generated/docs/ManageGetFileManagerSettingsResponseCredentials.md)
 - [ManageGetFileManagerSettingsResponseError](vps_generated/docs/ManageGetFileManagerSettingsResponseError.md)
 - [ManageGetHistoryResponse](vps_generated/docs/ManageGetHistoryResponse.md)
 - [ManageGetInfoResponse](vps_generated/docs/ManageGetInfoResponse.md)
 - [ManageGetInstalledSoftwareResponse](vps_generated/docs/ManageGetInstalledSoftwareResponse.md)
 - [ManageGetInstalledSoftwareResponseInstalledSoftwareInfo](vps_generated/docs/ManageGetInstalledSoftwareResponseInstalledSoftwareInfo.md)
 - [ManageGetListResponse](vps_generated/docs/ManageGetListResponse.md)
 - [ManageGetStatusesResponse](vps_generated/docs/ManageGetStatusesResponse.md)
 - [ManageGetStatusesResponseStatusInfo](vps_generated/docs/ManageGetStatusesResponseStatusInfo.md)
 - [ManageHistoryItem](vps_generated/docs/ManageHistoryItem.md)
 - [ManagePrivateNetworkInfo](vps_generated/docs/ManagePrivateNetworkInfo.md)
 - [ManageRebootVpsResponse](vps_generated/docs/ManageRebootVpsResponse.md)
 - [ManageRebootVpsResponseError](vps_generated/docs/ManageRebootVpsResponseError.md)
 - [ManageReinstallRequest](vps_generated/docs/ManageReinstallRequest.md)
 - [ManageReinstallResponse](vps_generated/docs/ManageReinstallResponse.md)
 - [ManageReinstallResponseError](vps_generated/docs/ManageReinstallResponseError.md)
 - [ManageReinstallResponseErrorSoftwareVariableError](vps_generated/docs/ManageReinstallResponseErrorSoftwareVariableError.md)
 - [ManageRemoveVpsResponse](vps_generated/docs/ManageRemoveVpsResponse.md)
 - [ManageRemoveVpsResponseError](vps_generated/docs/ManageRemoveVpsResponseError.md)
 - [ManageResetPasswordResponse](vps_generated/docs/ManageResetPasswordResponse.md)
 - [ManageResetPasswordResponseError](vps_generated/docs/ManageResetPasswordResponseError.md)
 - [ManageResetVpsResponse](vps_generated/docs/ManageResetVpsResponse.md)
 - [ManageResetVpsResponseError](vps_generated/docs/ManageResetVpsResponseError.md)
 - [ManageSoftwareInstallInfo](vps_generated/docs/ManageSoftwareInstallInfo.md)
 - [ManageStartRescueResponse](vps_generated/docs/ManageStartRescueResponse.md)
 - [ManageStartRescueResponseError](vps_generated/docs/ManageStartRescueResponseError.md)
 - [ManageStartVpsResponse](vps_generated/docs/ManageStartVpsResponse.md)
 - [ManageStartVpsResponseError](vps_generated/docs/ManageStartVpsResponseError.md)
 - [ManageStopRescueResponse](vps_generated/docs/ManageStopRescueResponse.md)
 - [ManageStopRescueResponseError](vps_generated/docs/ManageStopRescueResponseError.md)
 - [ManageStopVpsResponse](vps_generated/docs/ManageStopVpsResponse.md)
 - [ManageStopVpsResponseError](vps_generated/docs/ManageStopVpsResponseError.md)
 - [ManageUnarchiveResponse](vps_generated/docs/ManageUnarchiveResponse.md)
 - [ManageUpdateInfoRequest](vps_generated/docs/ManageUpdateInfoRequest.md)
 - [ManageUpdateInfoResponse](vps_generated/docs/ManageUpdateInfoResponse.md)
 - [ManageUpdateInfoResponseError](vps_generated/docs/ManageUpdateInfoResponseError.md)
 - [ManageVpsConfiguration](vps_generated/docs/ManageVpsConfiguration.md)
 - [ManageVpsInfo](vps_generated/docs/ManageVpsInfo.md)
 - [NetworkCreatePrivateNetworkResponse](vps_generated/docs/NetworkCreatePrivateNetworkResponse.md)
 - [NetworkCreatePrivateNetworkResponseError](vps_generated/docs/NetworkCreatePrivateNetworkResponseError.md)
 - [NetworkGetNetworkInfoResponse](vps_generated/docs/NetworkGetNetworkInfoResponse.md)
 - [NetworkOrderIpAddressRequest](vps_generated/docs/NetworkOrderIpAddressRequest.md)
 - [NetworkOrderIpAddressResponse](vps_generated/docs/NetworkOrderIpAddressResponse.md)
 - [NetworkOrderIpAddressResponseError](vps_generated/docs/NetworkOrderIpAddressResponseError.md)
 - [NetworkRemoveIpAddressResponse](vps_generated/docs/NetworkRemoveIpAddressResponse.md)
 - [NetworkRemoveIpAddressResponseError](vps_generated/docs/NetworkRemoveIpAddressResponseError.md)
 - [NetworkSuggestPrivateAddressRequest](vps_generated/docs/NetworkSuggestPrivateAddressRequest.md)
 - [NetworkSuggestPrivateAddressResponse](vps_generated/docs/NetworkSuggestPrivateAddressResponse.md)
 - [SnapshotCreateCalculatorRequest](vps_generated/docs/SnapshotCreateCalculatorRequest.md)
 - [SnapshotCreateCalculatorResponse](vps_generated/docs/SnapshotCreateCalculatorResponse.md)
 - [SnapshotCreateRequest](vps_generated/docs/SnapshotCreateRequest.md)
 - [SnapshotCreateResponse](vps_generated/docs/SnapshotCreateResponse.md)
 - [SnapshotCreateResponseError](vps_generated/docs/SnapshotCreateResponseError.md)
 - [SnapshotEditRequest](vps_generated/docs/SnapshotEditRequest.md)
 - [SnapshotEditResponse](vps_generated/docs/SnapshotEditResponse.md)
 - [SnapshotGetAllResponse](vps_generated/docs/SnapshotGetAllResponse.md)
 - [SnapshotGetAllRestoresResponse](vps_generated/docs/SnapshotGetAllRestoresResponse.md)
 - [SnapshotRemoveResponse](vps_generated/docs/SnapshotRemoveResponse.md)
 - [SnapshotRemoveResponseError](vps_generated/docs/SnapshotRemoveResponseError.md)
 - [SnapshotRequiredConfiguration](vps_generated/docs/SnapshotRequiredConfiguration.md)
 - [SnapshotRestore](vps_generated/docs/SnapshotRestore.md)
 - [SnapshotRestoreRequest](vps_generated/docs/SnapshotRestoreRequest.md)
 - [SnapshotRestoreResponse](vps_generated/docs/SnapshotRestoreResponse.md)
 - [SnapshotRestoreResponseError](vps_generated/docs/SnapshotRestoreResponseError.md)
 - [SnapshotSnapshot](vps_generated/docs/SnapshotSnapshot.md)
 - [SshKeyAddRequest](vps_generated/docs/SshKeyAddRequest.md)
 - [SshKeyAddResponse](vps_generated/docs/SshKeyAddResponse.md)
 - [SshKeyAddResponseError](vps_generated/docs/SshKeyAddResponseError.md)
 - [SshKeyGetAllResponse](vps_generated/docs/SshKeyGetAllResponse.md)
 - [SshKeyRemoveResponse](vps_generated/docs/SshKeyRemoveResponse.md)
 - [SshKeyRemoveResponseError](vps_generated/docs/SshKeyRemoveResponseError.md)
 - [StatisticGetCpuDetailsResponse](vps_generated/docs/StatisticGetCpuDetailsResponse.md)
 - [StatisticGetCpuResponse](vps_generated/docs/StatisticGetCpuResponse.md)
 - [StatisticGetDiskResponse](vps_generated/docs/StatisticGetDiskResponse.md)
 - [StatisticGetDiskUsageResponse](vps_generated/docs/StatisticGetDiskUsageResponse.md)
 - [StatisticGetLoadAverageResponse](vps_generated/docs/StatisticGetLoadAverageResponse.md)
 - [StatisticGetMemoryResponse](vps_generated/docs/StatisticGetMemoryResponse.md)
 - [StatisticGetNetworkResponse](vps_generated/docs/StatisticGetNetworkResponse.md)
 - [StatisticGetProcessListResponse](vps_generated/docs/StatisticGetProcessListResponse.md)
 - [StatisticGetProcessListResponseError](vps_generated/docs/StatisticGetProcessListResponseError.md)
 - [StatisticGetProcessListResponseProcessList](vps_generated/docs/StatisticGetProcessListResponseProcessList.md)
 - [StatisticGetProcessListResponseProcessListProcessInfo](vps_generated/docs/StatisticGetProcessListResponseProcessListProcessInfo.md)
 - [StatisticSeriesData](vps_generated/docs/StatisticSeriesData.md)
 - [StructuresAdditionalIpInfo](vps_generated/docs/StructuresAdditionalIpInfo.md)
 - [StructuresAttachedPrivateNetwork](vps_generated/docs/StructuresAttachedPrivateNetwork.md)
 - [StructuresCopyInfo](vps_generated/docs/StructuresCopyInfo.md)
 - [StructuresCopyInfoConfiguration](vps_generated/docs/StructuresCopyInfoConfiguration.md)
 - [StructuresFileInfo](vps_generated/docs/StructuresFileInfo.md)
 - [StructuresIpInfo](vps_generated/docs/StructuresIpInfo.md)
 - [StructuresOperatingSystem](vps_generated/docs/StructuresOperatingSystem.md)
 - [StructuresOperatingSystemRequirements](vps_generated/docs/StructuresOperatingSystemRequirements.md)
 - [StructuresOrderInfo](vps_generated/docs/StructuresOrderInfo.md)
 - [StructuresOrderInfoErrorDetails](vps_generated/docs/StructuresOrderInfoErrorDetails.md)
 - [StructuresOrderInfoErrorDetailsFileError](vps_generated/docs/StructuresOrderInfoErrorDetailsFileError.md)
 - [StructuresPrivateNetwork](vps_generated/docs/StructuresPrivateNetwork.md)
 - [StructuresSshKeyInfo](vps_generated/docs/StructuresSshKeyInfo.md)


## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication (JWT)


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in vps_generated.apis and vps_generated.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from vps_generated.api.default_api import DefaultApi`
- `from vps_generated.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import vps_generated
from vps_generated.apis import *
from vps_generated.models import *
```
