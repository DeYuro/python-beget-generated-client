# vps_generated.NetworkServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_service_create_private_network**](NetworkServiceApi.md#network_service_create_private_network) | **POST** /v1/vps/private-network | 
[**network_service_get_network_info**](NetworkServiceApi.md#network_service_get_network_info) | **GET** /v1/vps/network | 
[**network_service_order_ip_address**](NetworkServiceApi.md#network_service_order_ip_address) | **POST** /v1/vps/network | 
[**network_service_remove_ip_address**](NetworkServiceApi.md#network_service_remove_ip_address) | **DELETE** /v1/vps/network/{ip_address} | 
[**network_service_suggest_private_address**](NetworkServiceApi.md#network_service_suggest_private_address) | **POST** /v1/vps/private-network/{network_id}/suggested-address | 


# **network_service_create_private_network**
> NetworkCreatePrivateNetworkResponse network_service_create_private_network()



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import network_service_api
from vps_generated.model.network_create_private_network_response import NetworkCreatePrivateNetworkResponse
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
    api_instance = network_service_api.NetworkServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.network_service_create_private_network()
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling NetworkServiceApi->network_service_create_private_network: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**NetworkCreatePrivateNetworkResponse**](NetworkCreatePrivateNetworkResponse.md)

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

# **network_service_get_network_info**
> NetworkGetNetworkInfoResponse network_service_get_network_info()



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import network_service_api
from vps_generated.model.network_get_network_info_response import NetworkGetNetworkInfoResponse
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
    api_instance = network_service_api.NetworkServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.network_service_get_network_info()
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling NetworkServiceApi->network_service_get_network_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**NetworkGetNetworkInfoResponse**](NetworkGetNetworkInfoResponse.md)

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

# **network_service_order_ip_address**
> NetworkOrderIpAddressResponse network_service_order_ip_address(network_order_ip_address_request)



Заказ дополнительных IP-адресов для пользователя

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import network_service_api
from vps_generated.model.network_order_ip_address_response import NetworkOrderIpAddressResponse
from vps_generated.model.network_order_ip_address_request import NetworkOrderIpAddressRequest
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
    api_instance = network_service_api.NetworkServiceApi(api_client)
    network_order_ip_address_request = NetworkOrderIpAddressRequest(None) # NetworkOrderIpAddressRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.network_service_order_ip_address(network_order_ip_address_request)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling NetworkServiceApi->network_service_order_ip_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_order_ip_address_request** | [**NetworkOrderIpAddressRequest**](NetworkOrderIpAddressRequest.md)|  |

### Return type

[**NetworkOrderIpAddressResponse**](NetworkOrderIpAddressResponse.md)

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

# **network_service_remove_ip_address**
> NetworkRemoveIpAddressResponse network_service_remove_ip_address(ip_address)



Отмена заказа дополнительного IP адреса пользователя

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import network_service_api
from vps_generated.model.network_remove_ip_address_response import NetworkRemoveIpAddressResponse
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
    api_instance = network_service_api.NetworkServiceApi(api_client)
    ip_address = "ip_address_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.network_service_remove_ip_address(ip_address)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling NetworkServiceApi->network_service_remove_ip_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**|  |

### Return type

[**NetworkRemoveIpAddressResponse**](NetworkRemoveIpAddressResponse.md)

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

# **network_service_suggest_private_address**
> NetworkSuggestPrivateAddressResponse network_service_suggest_private_address(network_id, network_suggest_private_address_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import vps_generated
from vps_generated.api import network_service_api
from vps_generated.model.network_suggest_private_address_request import NetworkSuggestPrivateAddressRequest
from vps_generated.model.network_suggest_private_address_response import NetworkSuggestPrivateAddressResponse
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
    api_instance = network_service_api.NetworkServiceApi(api_client)
    network_id = "network_id_example" # str | 
    network_suggest_private_address_request = NetworkSuggestPrivateAddressRequest(None) # NetworkSuggestPrivateAddressRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.network_service_suggest_private_address(network_id, network_suggest_private_address_request)
        pprint(api_response)
    except vps_generated.ApiException as e:
        print("Exception when calling NetworkServiceApi->network_service_suggest_private_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**|  |
 **network_suggest_private_address_request** | [**NetworkSuggestPrivateAddressRequest**](NetworkSuggestPrivateAddressRequest.md)|  |

### Return type

[**NetworkSuggestPrivateAddressResponse**](NetworkSuggestPrivateAddressResponse.md)

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

