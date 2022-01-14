# vps_generated.SnapshotServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**snapshot_service_create**](SnapshotServiceApi.md#snapshot_service_create) | **POST** /v1/vps/snapshot | 
[**snapshot_service_create_calculator**](SnapshotServiceApi.md#snapshot_service_create_calculator) | **POST** /v1/vps/snapshot/calculator | 
[**snapshot_service_edit**](SnapshotServiceApi.md#snapshot_service_edit) | **PUT** /v1/vps/snapshot/{id} | 
[**snapshot_service_get_all**](SnapshotServiceApi.md#snapshot_service_get_all) | **GET** /v1/vps/snapshot | 
[**snapshot_service_get_all_restores**](SnapshotServiceApi.md#snapshot_service_get_all_restores) | **GET** /v1/vps/snapshot/restore | 
[**snapshot_service_remove**](SnapshotServiceApi.md#snapshot_service_remove) | **DELETE** /v1/vps/snapshot/{id} | 
[**snapshot_service_restore**](SnapshotServiceApi.md#snapshot_service_restore) | **POST** /v1/vps/snapshot/{id}/restore | 


# **snapshot_service_create**
> SnapshotCreateResponse snapshot_service_create(snapshot_create_request)



create a snapshot

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import snapshot_service_api
from vps_generated.model.snapshot_create_request import SnapshotCreateRequest
from vps_generated.model.snapshot_create_response import SnapshotCreateResponse
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
    api_instance = snapshot_service_api.SnapshotServiceApi(api_client)
    snapshot_create_request = SnapshotCreateRequest(None) # SnapshotCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.snapshot_service_create(snapshot_create_request)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling SnapshotServiceApi->snapshot_service_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_create_request** | [**SnapshotCreateRequest**](SnapshotCreateRequest.md)|  |

### Return type

[**SnapshotCreateResponse**](SnapshotCreateResponse.md)

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

# **snapshot_service_create_calculator**
> SnapshotCreateCalculatorResponse snapshot_service_create_calculator(snapshot_create_calculator_request)



create cost calculator for snapshot creating

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import snapshot_service_api
from vps_generated.model.snapshot_create_calculator_request import SnapshotCreateCalculatorRequest
from vps_generated.model.snapshot_create_calculator_response import SnapshotCreateCalculatorResponse
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
    api_instance = snapshot_service_api.SnapshotServiceApi(api_client)
    snapshot_create_calculator_request = SnapshotCreateCalculatorRequest(None) # SnapshotCreateCalculatorRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.snapshot_service_create_calculator(snapshot_create_calculator_request)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling SnapshotServiceApi->snapshot_service_create_calculator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_create_calculator_request** | [**SnapshotCreateCalculatorRequest**](SnapshotCreateCalculatorRequest.md)|  |

### Return type

[**SnapshotCreateCalculatorResponse**](SnapshotCreateCalculatorResponse.md)

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

# **snapshot_service_edit**
> SnapshotEditResponse snapshot_service_edit(id, snapshot_edit_request)



edit snapshot user fields

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import snapshot_service_api
from vps_generated.model.snapshot_edit_response import SnapshotEditResponse
from vps_generated.model.snapshot_edit_request import SnapshotEditRequest
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
    api_instance = snapshot_service_api.SnapshotServiceApi(api_client)
    id = "id_example" # str | 
    snapshot_edit_request = SnapshotEditRequest(None) # SnapshotEditRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.snapshot_service_edit(id, snapshot_edit_request)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling SnapshotServiceApi->snapshot_service_edit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **snapshot_edit_request** | [**SnapshotEditRequest**](SnapshotEditRequest.md)|  |

### Return type

[**SnapshotEditResponse**](SnapshotEditResponse.md)

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

# **snapshot_service_get_all**
> SnapshotGetAllResponse snapshot_service_get_all()



get all snapshots

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import snapshot_service_api
from vps_generated.model.snapshot_get_all_response import SnapshotGetAllResponse
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
    api_instance = snapshot_service_api.SnapshotServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.snapshot_service_get_all()
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling SnapshotServiceApi->snapshot_service_get_all: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SnapshotGetAllResponse**](SnapshotGetAllResponse.md)

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

# **snapshot_service_get_all_restores**
> SnapshotGetAllRestoresResponse snapshot_service_get_all_restores()



get restore list

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import snapshot_service_api
from vps_generated.model.snapshot_get_all_restores_response import SnapshotGetAllRestoresResponse
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
    api_instance = snapshot_service_api.SnapshotServiceApi(api_client)
    id = "id_example" # str | snapshot id. Optional, full list at 0 (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.snapshot_service_get_all_restores(id=id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling SnapshotServiceApi->snapshot_service_get_all_restores: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| snapshot id. Optional, full list at 0 | [optional]

### Return type

[**SnapshotGetAllRestoresResponse**](SnapshotGetAllRestoresResponse.md)

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

# **snapshot_service_remove**
> SnapshotRemoveResponse snapshot_service_remove(id)



remove the snapshot

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import snapshot_service_api
from vps_generated.model.snapshot_remove_response import SnapshotRemoveResponse
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
    api_instance = snapshot_service_api.SnapshotServiceApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.snapshot_service_remove(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling SnapshotServiceApi->snapshot_service_remove: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**SnapshotRemoveResponse**](SnapshotRemoveResponse.md)

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

# **snapshot_service_restore**
> SnapshotRestoreResponse snapshot_service_restore(id, snapshot_restore_request)



create a restore for the snapshot

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import snapshot_service_api
from vps_generated.model.snapshot_restore_response import SnapshotRestoreResponse
from vps_generated.model.snapshot_restore_request import SnapshotRestoreRequest
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
    api_instance = snapshot_service_api.SnapshotServiceApi(api_client)
    id = "id_example" # str | 
    snapshot_restore_request = SnapshotRestoreRequest(None) # SnapshotRestoreRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.snapshot_service_restore(id, snapshot_restore_request)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling SnapshotServiceApi->snapshot_service_restore: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **snapshot_restore_request** | [**SnapshotRestoreRequest**](SnapshotRestoreRequest.md)|  |

### Return type

[**SnapshotRestoreResponse**](SnapshotRestoreResponse.md)

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

