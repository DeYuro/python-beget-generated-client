# vps_generated.BackupServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backup_service_get_available_copies**](BackupServiceApi.md#backup_service_get_available_copies) | **GET** /v1/vps/backup | 
[**backup_service_get_backup_file_list**](BackupServiceApi.md#backup_service_get_backup_file_list) | **GET** /v1/vps/{id}/backup/{copy_id} | 
[**backup_service_get_orders**](BackupServiceApi.md#backup_service_get_orders) | **GET** /v1/vps/backup/orders | 
[**backup_service_restore_file**](BackupServiceApi.md#backup_service_restore_file) | **POST** /v1/vps/{id}/backup/{copy_id}/file | 
[**backup_service_restore_server**](BackupServiceApi.md#backup_service_restore_server) | **POST** /v1/vps/{id}/backup/{copy_id}/server | 


# **backup_service_get_available_copies**
> BackupGetAvailableCopiesResponse backup_service_get_available_copies()



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import backup_service_api
from vps_generated.model.backup_get_available_copies_response import BackupGetAvailableCopiesResponse
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
    api_instance = backup_service_api.BackupServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.backup_service_get_available_copies()
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling BackupServiceApi->backup_service_get_available_copies: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**BackupGetAvailableCopiesResponse**](BackupGetAvailableCopiesResponse.md)

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

# **backup_service_get_backup_file_list**
> BackupGetBackupFileListResponse backup_service_get_backup_file_list(id, copy_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import backup_service_api
from vps_generated.model.backup_get_backup_file_list_response import BackupGetBackupFileListResponse
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
    api_instance = backup_service_api.BackupServiceApi(api_client)
    id = "id_example" # str | 
    copy_id = "copy_id_example" # str | 
    path = "path_example" # str | Путь для отображения (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.backup_service_get_backup_file_list(id, copy_id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling BackupServiceApi->backup_service_get_backup_file_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.backup_service_get_backup_file_list(id, copy_id, path=path)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling BackupServiceApi->backup_service_get_backup_file_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **copy_id** | **str**|  |
 **path** | **str**| Путь для отображения | [optional]

### Return type

[**BackupGetBackupFileListResponse**](BackupGetBackupFileListResponse.md)

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

# **backup_service_get_orders**
> BackupGetOrdersResponse backup_service_get_orders()



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import backup_service_api
from vps_generated.model.backup_get_orders_response import BackupGetOrdersResponse
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
    api_instance = backup_service_api.BackupServiceApi(api_client)
    limit = "limit_example" # str | Количество записей на страницу (от 1 до 100) (optional)
    offset = "offset_example" # str | Смещение относительно нулевой (последней) записи (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.backup_service_get_orders(limit=limit, offset=offset)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling BackupServiceApi->backup_service_get_orders: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Количество записей на страницу (от 1 до 100) | [optional]
 **offset** | **str**| Смещение относительно нулевой (последней) записи | [optional]

### Return type

[**BackupGetOrdersResponse**](BackupGetOrdersResponse.md)

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

# **backup_service_restore_file**
> BackupRestoreFileResponse backup_service_restore_file(id, copy_id, backup_restore_file_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import backup_service_api
from vps_generated.model.backup_restore_file_response import BackupRestoreFileResponse
from vps_generated.model.backup_restore_file_request import BackupRestoreFileRequest
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
    api_instance = backup_service_api.BackupServiceApi(api_client)
    id = "id_example" # str | 
    copy_id = "copy_id_example" # str | 
    backup_restore_file_request = BackupRestoreFileRequest(None) # BackupRestoreFileRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.backup_service_restore_file(id, copy_id, backup_restore_file_request)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling BackupServiceApi->backup_service_restore_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **copy_id** | **str**|  |
 **backup_restore_file_request** | [**BackupRestoreFileRequest**](BackupRestoreFileRequest.md)|  |

### Return type

[**BackupRestoreFileResponse**](BackupRestoreFileResponse.md)

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

# **backup_service_restore_server**
> BackupRestoreServerResponse backup_service_restore_server(id, copy_id, backup_restore_server_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import backup_service_api
from vps_generated.model.backup_restore_server_response import BackupRestoreServerResponse
from vps_generated.model.backup_restore_server_request import BackupRestoreServerRequest
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
    api_instance = backup_service_api.BackupServiceApi(api_client)
    id = "id_example" # str | 
    copy_id = "copy_id_example" # str | 
    backup_restore_server_request = BackupRestoreServerRequest(None) # BackupRestoreServerRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.backup_service_restore_server(id, copy_id, backup_restore_server_request)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling BackupServiceApi->backup_service_restore_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **copy_id** | **str**|  |
 **backup_restore_server_request** | [**BackupRestoreServerRequest**](BackupRestoreServerRequest.md)|  |

### Return type

[**BackupRestoreServerResponse**](BackupRestoreServerResponse.md)

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

