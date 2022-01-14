# auth_generated.KeyServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**key_service_get_key**](KeyServiceApi.md#key_service_get_key) | **GET** /v1/auth/key | 


# **key_service_get_key**
> KeyGetKeyResponse key_service_get_key()



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import auth_generated
from auth_generated.api import key_service_api
from auth_generated.model.key_get_key_response import KeyGetKeyResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.beget.com
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_generated.Configuration(
    host = "https://api.beget.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = auth_generated.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with auth_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_service_api.KeyServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.key_service_get_key()
        pprint(api_response)
    except auth_generated.ApiException as e:
        print("Exception when calling KeyServiceApi->key_service_get_key: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**KeyGetKeyResponse**](KeyGetKeyResponse.md)

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

