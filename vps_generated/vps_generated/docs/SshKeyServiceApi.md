# vps_generated.SshKeyServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ssh_key_service_add**](SshKeyServiceApi.md#ssh_key_service_add) | **POST** /v1/vps/sshKey | 
[**ssh_key_service_get_all**](SshKeyServiceApi.md#ssh_key_service_get_all) | **GET** /v1/vps/sshKey | 
[**ssh_key_service_remove**](SshKeyServiceApi.md#ssh_key_service_remove) | **DELETE** /v1/vps/sshKey/{id} | 


# **ssh_key_service_add**
> SshKeyAddResponse ssh_key_service_add(ssh_key_add_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import ssh_key_service_api
from vps_generated.model.ssh_key_add_response import SshKeyAddResponse
from vps_generated.model.ssh_key_add_request import SshKeyAddRequest
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
    api_instance = ssh_key_service_api.SshKeyServiceApi(api_client)
    ssh_key_add_request = SshKeyAddRequest(None) # SshKeyAddRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.ssh_key_service_add(ssh_key_add_request)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling SshKeyServiceApi->ssh_key_service_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_key_add_request** | [**SshKeyAddRequest**](SshKeyAddRequest.md)|  |

### Return type

[**SshKeyAddResponse**](SshKeyAddResponse.md)

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

# **ssh_key_service_get_all**
> SshKeyGetAllResponse ssh_key_service_get_all()



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import ssh_key_service_api
from vps_generated.model.ssh_key_get_all_response import SshKeyGetAllResponse
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
    api_instance = ssh_key_service_api.SshKeyServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.ssh_key_service_get_all()
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling SshKeyServiceApi->ssh_key_service_get_all: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SshKeyGetAllResponse**](SshKeyGetAllResponse.md)

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

# **ssh_key_service_remove**
> SshKeyRemoveResponse ssh_key_service_remove(id)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import ssh_key_service_api
from vps_generated.model.ssh_key_remove_response import SshKeyRemoveResponse
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
    api_instance = ssh_key_service_api.SshKeyServiceApi(api_client)
    id = "id_example" # str | 
    force = "force_example" # str | Принудительно удалить, даже если используется в VPS (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.ssh_key_service_remove(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling SshKeyServiceApi->ssh_key_service_remove: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.ssh_key_service_remove(id, force=force)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling SshKeyServiceApi->ssh_key_service_remove: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **force** | **str**| Принудительно удалить, даже если используется в VPS | [optional]

### Return type

[**SshKeyRemoveResponse**](SshKeyRemoveResponse.md)

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

