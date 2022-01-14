# vps_generated.ManageServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**manage_service_attach_ip_address**](ManageServiceApi.md#manage_service_attach_ip_address) | **POST** /v1/vps/{id}/network/{ip_address} | 
[**manage_service_attach_ssh_key**](ManageServiceApi.md#manage_service_attach_ssh_key) | **POST** /v1/vps/{id}/sshKey/{ssh_key_id} | 
[**manage_service_attach_to_private_network**](ManageServiceApi.md#manage_service_attach_to_private_network) | **POST** /v1/vps/{id}/private-network/{network_id} | 
[**manage_service_change_configuration**](ManageServiceApi.md#manage_service_change_configuration) | **PUT** /v1/vps/server/{id}/configuration | 
[**manage_service_change_ssh_access**](ManageServiceApi.md#manage_service_change_ssh_access) | **PUT** /v1/vps/{id}/ssh/access | 
[**manage_service_check_software_requirements**](ManageServiceApi.md#manage_service_check_software_requirements) | **POST** /v1/vps/software/requirements | 
[**manage_service_create_vps**](ManageServiceApi.md#manage_service_create_vps) | **POST** /v1/vps/server | 
[**manage_service_detach_from_private_network**](ManageServiceApi.md#manage_service_detach_from_private_network) | **DELETE** /v1/vps/{id}/private-network/{network_id} | 
[**manage_service_detach_ip_address**](ManageServiceApi.md#manage_service_detach_ip_address) | **DELETE** /v1/vps/network/detach/{ip_address} | 
[**manage_service_detach_ssh_key**](ManageServiceApi.md#manage_service_detach_ssh_key) | **DELETE** /v1/vps/{id}/sshKey/{ssh_key_id} | 
[**manage_service_get_available_configuration**](ManageServiceApi.md#manage_service_get_available_configuration) | **GET** /v1/vps/configuration | 
[**manage_service_get_available_software**](ManageServiceApi.md#manage_service_get_available_software) | **GET** /v1/vps/software | 
[**manage_service_get_file_manager_settings**](ManageServiceApi.md#manage_service_get_file_manager_settings) | **POST** /v1/vps/{id}/fm | 
[**manage_service_get_history**](ManageServiceApi.md#manage_service_get_history) | **GET** /v1/vps/{id}/history | 
[**manage_service_get_info**](ManageServiceApi.md#manage_service_get_info) | **GET** /v1/vps/server/{id} | 
[**manage_service_get_installed_software**](ManageServiceApi.md#manage_service_get_installed_software) | **GET** /v1/vps/{id}/software | 
[**manage_service_get_list**](ManageServiceApi.md#manage_service_get_list) | **GET** /v1/vps/server/list | 
[**manage_service_get_statuses**](ManageServiceApi.md#manage_service_get_statuses) | **GET** /v1/vps/server/statuses | 
[**manage_service_reboot_vps**](ManageServiceApi.md#manage_service_reboot_vps) | **POST** /v1/vps/server/{id}/reboot | 
[**manage_service_reinstall**](ManageServiceApi.md#manage_service_reinstall) | **POST** /v1/vps/server/{id}/reinstall | 
[**manage_service_remove_vps**](ManageServiceApi.md#manage_service_remove_vps) | **POST** /v1/vps/server/{id}/remove | 
[**manage_service_reset_password**](ManageServiceApi.md#manage_service_reset_password) | **PUT** /v1/vps/{id}/password | 
[**manage_service_reset_vps**](ManageServiceApi.md#manage_service_reset_vps) | **POST** /v1/vps/server/{id}/reset | 
[**manage_service_start_rescue**](ManageServiceApi.md#manage_service_start_rescue) | **POST** /v1/vps/server/{id}/rescue | 
[**manage_service_start_vps**](ManageServiceApi.md#manage_service_start_vps) | **POST** /v1/vps/server/{id}/start | 
[**manage_service_stop_rescue**](ManageServiceApi.md#manage_service_stop_rescue) | **DELETE** /v1/vps/server/{id}/rescue | 
[**manage_service_stop_vps**](ManageServiceApi.md#manage_service_stop_vps) | **POST** /v1/vps/server/{id}/stop | 
[**manage_service_unarchive**](ManageServiceApi.md#manage_service_unarchive) | **DELETE** /v1/vps/archive/{id} | 
[**manage_service_update_info**](ManageServiceApi.md#manage_service_update_info) | **PUT** /v1/vps/server/{id}/info | 


# **manage_service_attach_ip_address**
> ManageAttachIpAddressResponse manage_service_attach_ip_address(id, ip_address, manage_attach_ip_address_request)



Прикрепление дополнительного IP адреса пользователя к VPS

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_attach_ip_address_response import ManageAttachIpAddressResponse
from vps_generated.model.manage_attach_ip_address_request import ManageAttachIpAddressRequest
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 
    ip_address = "ip_address_example" # str | 
    manage_attach_ip_address_request = ManageAttachIpAddressRequest(None) # ManageAttachIpAddressRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_attach_ip_address(id, ip_address, manage_attach_ip_address_request)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_attach_ip_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **ip_address** | **str**|  |
 **manage_attach_ip_address_request** | [**ManageAttachIpAddressRequest**](ManageAttachIpAddressRequest.md)|  |

### Return type

[**ManageAttachIpAddressResponse**](ManageAttachIpAddressResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_attach_ssh_key**
> ManageAttachSshKeyResponse manage_service_attach_ssh_key(id, ssh_key_id)



Добавляет ssh-ключ к VPS

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_attach_ssh_key_response import ManageAttachSshKeyResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 
    ssh_key_id = "ssh_key_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_attach_ssh_key(id, ssh_key_id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_attach_ssh_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **ssh_key_id** | **str**|  |

### Return type

[**ManageAttachSshKeyResponse**](ManageAttachSshKeyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_attach_to_private_network**
> ManageAttachToPrivateNetworkResponse manage_service_attach_to_private_network(id, network_id, manage_attach_to_private_network_request)



Добавляет VPS к приватной сети

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_attach_to_private_network_response import ManageAttachToPrivateNetworkResponse
from vps_generated.model.manage_attach_to_private_network_request import ManageAttachToPrivateNetworkRequest
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 
    network_id = "network_id_example" # str | 
    manage_attach_to_private_network_request = ManageAttachToPrivateNetworkRequest(None) # ManageAttachToPrivateNetworkRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_attach_to_private_network(id, network_id, manage_attach_to_private_network_request)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_attach_to_private_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **network_id** | **str**|  |
 **manage_attach_to_private_network_request** | [**ManageAttachToPrivateNetworkRequest**](ManageAttachToPrivateNetworkRequest.md)|  |

### Return type

[**ManageAttachToPrivateNetworkResponse**](ManageAttachToPrivateNetworkResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_change_configuration**
> ManageChangeConfigurationResponse manage_service_change_configuration(id, manage_change_configuration_request)



Отправляет запрос на смену конфигурации Vps (с перезагрузкой)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_change_configuration_request import ManageChangeConfigurationRequest
from vps_generated.model.manage_change_configuration_response import ManageChangeConfigurationResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 
    manage_change_configuration_request = ManageChangeConfigurationRequest(None) # ManageChangeConfigurationRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_change_configuration(id, manage_change_configuration_request)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_change_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **manage_change_configuration_request** | [**ManageChangeConfigurationRequest**](ManageChangeConfigurationRequest.md)|  |

### Return type

[**ManageChangeConfigurationResponse**](ManageChangeConfigurationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_change_ssh_access**
> ManageChangeSshAccessResponse manage_service_change_ssh_access(id, manage_change_ssh_access_request)



Изменение возможности доступа к пользовательской машине через SSH-ключи BeGet

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_change_ssh_access_response import ManageChangeSshAccessResponse
from vps_generated.model.manage_change_ssh_access_request import ManageChangeSshAccessRequest
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 
    manage_change_ssh_access_request = ManageChangeSshAccessRequest(None) # ManageChangeSshAccessRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_change_ssh_access(id, manage_change_ssh_access_request)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_change_ssh_access: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **manage_change_ssh_access_request** | [**ManageChangeSshAccessRequest**](ManageChangeSshAccessRequest.md)|  |

### Return type

[**ManageChangeSshAccessResponse**](ManageChangeSshAccessResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_check_software_requirements**
> ManageCheckSoftwareRequirementsResponse manage_service_check_software_requirements(manage_check_software_requirements_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_check_software_requirements_request import ManageCheckSoftwareRequirementsRequest
from vps_generated.model.manage_check_software_requirements_response import ManageCheckSoftwareRequirementsResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    manage_check_software_requirements_request = ManageCheckSoftwareRequirementsRequest(None) # ManageCheckSoftwareRequirementsRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_check_software_requirements(manage_check_software_requirements_request)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_check_software_requirements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manage_check_software_requirements_request** | [**ManageCheckSoftwareRequirementsRequest**](ManageCheckSoftwareRequirementsRequest.md)|  |

### Return type

[**ManageCheckSoftwareRequirementsResponse**](ManageCheckSoftwareRequirementsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_create_vps**
> ManageCreateVpsResponse manage_service_create_vps(manage_create_vps_request)



Отправляет команду на создание новой Vps и ее запуск (https://jira.beget.ru/browse/BH-327)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_create_vps_request import ManageCreateVpsRequest
from vps_generated.model.manage_create_vps_response import ManageCreateVpsResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    manage_create_vps_request = ManageCreateVpsRequest(None) # ManageCreateVpsRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_create_vps(manage_create_vps_request)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_create_vps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manage_create_vps_request** | [**ManageCreateVpsRequest**](ManageCreateVpsRequest.md)|  |

### Return type

[**ManageCreateVpsResponse**](ManageCreateVpsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_detach_from_private_network**
> ManageDetachFromPrivateNetworkResponse manage_service_detach_from_private_network(id, network_id)



Удаляет VPS из приватной сети

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_detach_from_private_network_response import ManageDetachFromPrivateNetworkResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 
    network_id = "network_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_detach_from_private_network(id, network_id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_detach_from_private_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **network_id** | **str**|  |

### Return type

[**ManageDetachFromPrivateNetworkResponse**](ManageDetachFromPrivateNetworkResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_detach_ip_address**
> ManageDetachIpAddressResponse manage_service_detach_ip_address(ip_address)



Открепление дополнительного IP адреса пользователя от VPS

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_detach_ip_address_response import ManageDetachIpAddressResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    ip_address = "ip_address_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_detach_ip_address(ip_address)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_detach_ip_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**|  |

### Return type

[**ManageDetachIpAddressResponse**](ManageDetachIpAddressResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_detach_ssh_key**
> ManageDetachSshKeyResponse manage_service_detach_ssh_key(id, ssh_key_id)



Удаляет ssh-ключ из VPS

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_detach_ssh_key_response import ManageDetachSshKeyResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 
    ssh_key_id = "ssh_key_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_detach_ssh_key(id, ssh_key_id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_detach_ssh_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **ssh_key_id** | **str**|  |

### Return type

[**ManageDetachSshKeyResponse**](ManageDetachSshKeyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_get_available_configuration**
> ManageGetAvailableConfigurationResponse manage_service_get_available_configuration()



Возвращает досупные варианты конфигурации Vps (список ОС и тарифных планов)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_get_available_configuration_response import ManageGetAvailableConfigurationResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.manage_service_get_available_configuration()
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_get_available_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ManageGetAvailableConfigurationResponse**](ManageGetAvailableConfigurationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_get_available_software**
> ManageGetAvailableSoftwareResponse manage_service_get_available_software()



Возвращает список доступного для установки ПО

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_get_available_software_response import ManageGetAvailableSoftwareResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.manage_service_get_available_software()
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_get_available_software: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ManageGetAvailableSoftwareResponse**](ManageGetAvailableSoftwareResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_get_file_manager_settings**
> ManageGetFileManagerSettingsResponse manage_service_get_file_manager_settings(id)



Возвращает необходимые параметры сессии для перехода в файловый менеджер

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_get_file_manager_settings_response import ManageGetFileManagerSettingsResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_get_file_manager_settings(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_get_file_manager_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ManageGetFileManagerSettingsResponse**](ManageGetFileManagerSettingsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_get_history**
> ManageGetHistoryResponse manage_service_get_history(id)



Возвращат историю состояний VPS

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_get_history_response import ManageGetHistoryResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_get_history(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_get_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ManageGetHistoryResponse**](ManageGetHistoryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_get_info**
> ManageGetInfoResponse manage_service_get_info(id)



Возвращает информацию по одной конкретной Vps

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_get_info_response import ManageGetInfoResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_get_info(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_get_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ManageGetInfoResponse**](ManageGetInfoResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_get_installed_software**
> ManageGetInstalledSoftwareResponse manage_service_get_installed_software(id)



Возвращает список установленного ПО на сервере

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_get_installed_software_response import ManageGetInstalledSoftwareResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_get_installed_software(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_get_installed_software: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ManageGetInstalledSoftwareResponse**](ManageGetInstalledSoftwareResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_get_list**
> ManageGetListResponse manage_service_get_list()



Возвращает список Vps с некоторыми параметрами

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_get_list_response import ManageGetListResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.manage_service_get_list()
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_get_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ManageGetListResponse**](ManageGetListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_get_statuses**
> ManageGetStatusesResponse manage_service_get_statuses()



Возвращает статусы всех Vps

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_get_statuses_response import ManageGetStatusesResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.manage_service_get_statuses()
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_get_statuses: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ManageGetStatusesResponse**](ManageGetStatusesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_reboot_vps**
> ManageRebootVpsResponse manage_service_reboot_vps(id)



Отправляет команду на рестарт Vps

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_reboot_vps_response import ManageRebootVpsResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_reboot_vps(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_reboot_vps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ManageRebootVpsResponse**](ManageRebootVpsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_reinstall**
> ManageReinstallResponse manage_service_reinstall(id, manage_reinstall_request)



Отправляет запрос на переустановку ОС (с перезагрузкой и уничтожением всех данных)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_reinstall_request import ManageReinstallRequest
from vps_generated.model.manage_reinstall_response import ManageReinstallResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 
    manage_reinstall_request = ManageReinstallRequest(None) # ManageReinstallRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_reinstall(id, manage_reinstall_request)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_reinstall: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **manage_reinstall_request** | [**ManageReinstallRequest**](ManageReinstallRequest.md)|  |

### Return type

[**ManageReinstallResponse**](ManageReinstallResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_remove_vps**
> ManageRemoveVpsResponse manage_service_remove_vps(id)



Отправляет команду на удаление Vps

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_remove_vps_response import ManageRemoveVpsResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_remove_vps(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_remove_vps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ManageRemoveVpsResponse**](ManageRemoveVpsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_reset_password**
> ManageResetPasswordResponse manage_service_reset_password(id)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_reset_password_response import ManageResetPasswordResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_reset_password(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_reset_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ManageResetPasswordResponse**](ManageResetPasswordResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_reset_vps**
> ManageResetVpsResponse manage_service_reset_vps(id)



Отправляет команду на рестарт Vps

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_reset_vps_response import ManageResetVpsResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_reset_vps(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_reset_vps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ManageResetVpsResponse**](ManageResetVpsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_start_rescue**
> ManageStartRescueResponse manage_service_start_rescue(id)



Отправляет команду на перевод Vps в rescue-режим

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_start_rescue_response import ManageStartRescueResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_start_rescue(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_start_rescue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ManageStartRescueResponse**](ManageStartRescueResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_start_vps**
> ManageStartVpsResponse manage_service_start_vps(id)



Отправляет команду на запуск Vps

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_start_vps_response import ManageStartVpsResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_start_vps(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_start_vps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ManageStartVpsResponse**](ManageStartVpsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_stop_rescue**
> ManageStopRescueResponse manage_service_stop_rescue(id)



Отправляет запрос на отключение rescue-режима и перезагрузку Vps

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_stop_rescue_response import ManageStopRescueResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_stop_rescue(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_stop_rescue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ManageStopRescueResponse**](ManageStopRescueResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_stop_vps**
> ManageStopVpsResponse manage_service_stop_vps(id)



Отправляет команду на остановку Vps

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_stop_vps_response import ManageStopVpsResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_stop_vps(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_stop_vps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ManageStopVpsResponse**](ManageStopVpsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_unarchive**
> ManageUnarchiveResponse manage_service_unarchive(id)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_unarchive_response import ManageUnarchiveResponse
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_unarchive(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_unarchive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ManageUnarchiveResponse**](ManageUnarchiveResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_service_update_info**
> ManageUpdateInfoResponse manage_service_update_info(id, manage_update_info_request)



Обновляет информацию о Vps (которая отображается в панели)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import manage_service_api
from vps_generated.model.manage_update_info_response import ManageUpdateInfoResponse
from vps_generated.model.manage_update_info_request import ManageUpdateInfoRequest
from pprint import pprint
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
    api_instance = manage_service_api.ManageServiceApi(api_client)
    id = "id_example" # str | 
    manage_update_info_request = ManageUpdateInfoRequest(None) # ManageUpdateInfoRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_service_update_info(id, manage_update_info_request)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling ManageServiceApi->manage_service_update_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **manage_update_info_request** | [**ManageUpdateInfoRequest**](ManageUpdateInfoRequest.md)|  |

### Return type

[**ManageUpdateInfoResponse**](ManageUpdateInfoResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

