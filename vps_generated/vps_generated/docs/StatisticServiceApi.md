# vps_generated.StatisticServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statistic_service_get_cpu**](StatisticServiceApi.md#statistic_service_get_cpu) | **GET** /v1/vps/statistic/cpu/{id} | 
[**statistic_service_get_cpu_details**](StatisticServiceApi.md#statistic_service_get_cpu_details) | **GET** /v1/vps/statistic/cpu-details/{id} | 
[**statistic_service_get_disk**](StatisticServiceApi.md#statistic_service_get_disk) | **GET** /v1/vps/statistic/disk/{id} | 
[**statistic_service_get_disk_usage**](StatisticServiceApi.md#statistic_service_get_disk_usage) | **GET** /v1/vps/statistic/disk-usage/{id} | 
[**statistic_service_get_load_average**](StatisticServiceApi.md#statistic_service_get_load_average) | **GET** /v1/vps/statistic/load-average/{id} | 
[**statistic_service_get_memory**](StatisticServiceApi.md#statistic_service_get_memory) | **GET** /v1/vps/statistic/memory/{id} | 
[**statistic_service_get_network**](StatisticServiceApi.md#statistic_service_get_network) | **GET** /v1/vps/statistic/network/{id} | 
[**statistic_service_get_process_list**](StatisticServiceApi.md#statistic_service_get_process_list) | **GET** /v1/vps/statistic/processes/{id} | 


# **statistic_service_get_cpu**
> StatisticGetCpuResponse statistic_service_get_cpu(id)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import statistic_service_api
from vps_generated.model.statistic_get_cpu_response import StatisticGetCpuResponse
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
    api_instance = statistic_service_api.StatisticServiceApi(api_client)
    id = "id_example" # str | 
    period = "period_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.statistic_service_get_cpu(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling StatisticServiceApi->statistic_service_get_cpu: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.statistic_service_get_cpu(id, period=period)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling StatisticServiceApi->statistic_service_get_cpu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **period** | **str**|  | [optional]

### Return type

[**StatisticGetCpuResponse**](StatisticGetCpuResponse.md)

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

# **statistic_service_get_cpu_details**
> StatisticGetCpuDetailsResponse statistic_service_get_cpu_details(id)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import statistic_service_api
from vps_generated.model.statistic_get_cpu_details_response import StatisticGetCpuDetailsResponse
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
    api_instance = statistic_service_api.StatisticServiceApi(api_client)
    id = "id_example" # str | 
    period = "period_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.statistic_service_get_cpu_details(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling StatisticServiceApi->statistic_service_get_cpu_details: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.statistic_service_get_cpu_details(id, period=period)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling StatisticServiceApi->statistic_service_get_cpu_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **period** | **str**|  | [optional]

### Return type

[**StatisticGetCpuDetailsResponse**](StatisticGetCpuDetailsResponse.md)

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

# **statistic_service_get_disk**
> StatisticGetDiskResponse statistic_service_get_disk(id)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import statistic_service_api
from vps_generated.model.statistic_get_disk_response import StatisticGetDiskResponse
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
    api_instance = statistic_service_api.StatisticServiceApi(api_client)
    id = "id_example" # str | 
    period = "period_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.statistic_service_get_disk(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling StatisticServiceApi->statistic_service_get_disk: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.statistic_service_get_disk(id, period=period)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling StatisticServiceApi->statistic_service_get_disk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **period** | **str**|  | [optional]

### Return type

[**StatisticGetDiskResponse**](StatisticGetDiskResponse.md)

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

# **statistic_service_get_disk_usage**
> StatisticGetDiskUsageResponse statistic_service_get_disk_usage(id)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import statistic_service_api
from vps_generated.model.statistic_get_disk_usage_response import StatisticGetDiskUsageResponse
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
    api_instance = statistic_service_api.StatisticServiceApi(api_client)
    id = "id_example" # str | 
    period = "period_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.statistic_service_get_disk_usage(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling StatisticServiceApi->statistic_service_get_disk_usage: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.statistic_service_get_disk_usage(id, period=period)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling StatisticServiceApi->statistic_service_get_disk_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **period** | **str**|  | [optional]

### Return type

[**StatisticGetDiskUsageResponse**](StatisticGetDiskUsageResponse.md)

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

# **statistic_service_get_load_average**
> StatisticGetLoadAverageResponse statistic_service_get_load_average(id)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import statistic_service_api
from vps_generated.model.statistic_get_load_average_response import StatisticGetLoadAverageResponse
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
    api_instance = statistic_service_api.StatisticServiceApi(api_client)
    id = "id_example" # str | 
    period = "period_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.statistic_service_get_load_average(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling StatisticServiceApi->statistic_service_get_load_average: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.statistic_service_get_load_average(id, period=period)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling StatisticServiceApi->statistic_service_get_load_average: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **period** | **str**|  | [optional]

### Return type

[**StatisticGetLoadAverageResponse**](StatisticGetLoadAverageResponse.md)

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

# **statistic_service_get_memory**
> StatisticGetMemoryResponse statistic_service_get_memory(id)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import statistic_service_api
from vps_generated.model.statistic_get_memory_response import StatisticGetMemoryResponse
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
    api_instance = statistic_service_api.StatisticServiceApi(api_client)
    id = "id_example" # str | 
    period = "period_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.statistic_service_get_memory(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling StatisticServiceApi->statistic_service_get_memory: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.statistic_service_get_memory(id, period=period)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling StatisticServiceApi->statistic_service_get_memory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **period** | **str**|  | [optional]

### Return type

[**StatisticGetMemoryResponse**](StatisticGetMemoryResponse.md)

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

# **statistic_service_get_network**
> StatisticGetNetworkResponse statistic_service_get_network(id)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import statistic_service_api
from vps_generated.model.statistic_get_network_response import StatisticGetNetworkResponse
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
    api_instance = statistic_service_api.StatisticServiceApi(api_client)
    id = "id_example" # str | 
    period = "period_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.statistic_service_get_network(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling StatisticServiceApi->statistic_service_get_network: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.statistic_service_get_network(id, period=period)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling StatisticServiceApi->statistic_service_get_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **period** | **str**|  | [optional]

### Return type

[**StatisticGetNetworkResponse**](StatisticGetNetworkResponse.md)

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

# **statistic_service_get_process_list**
> StatisticGetProcessListResponse statistic_service_get_process_list(id)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import statistic_service_api
from vps_generated.model.statistic_get_process_list_response import StatisticGetProcessListResponse
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
    api_instance = statistic_service_api.StatisticServiceApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.statistic_service_get_process_list(id)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling StatisticServiceApi->statistic_service_get_process_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**StatisticGetProcessListResponse**](StatisticGetProcessListResponse.md)

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

