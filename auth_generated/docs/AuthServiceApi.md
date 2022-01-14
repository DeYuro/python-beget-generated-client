# auth_generated.AuthServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_service_auth**](AuthServiceApi.md#auth_service_auth) | **POST** /v1/auth | 
[**auth_service_logout**](AuthServiceApi.md#auth_service_logout) | **POST** /v1/auth/logout | 
[**auth_service_refresh_token**](AuthServiceApi.md#auth_service_refresh_token) | **POST** /v1/auth/refresh | 
[**auth_service_switch_user**](AuthServiceApi.md#auth_service_switch_user) | **POST** /v1/auth/switch | 


# **auth_service_auth**
> AuthAuthResponse auth_service_auth(auth_auth_request)



Запрос авторизации пользователя.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import auth_generated
from auth_generated.api import auth_service_api
from auth_generated.model.auth_auth_request import AuthAuthRequest
from auth_generated.model.auth_auth_response import AuthAuthResponse
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
    api_instance = auth_service_api.AuthServiceApi(api_client)
    auth_auth_request = AuthAuthRequest(None) # AuthAuthRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.auth_service_auth(auth_auth_request)
        pprint(api_response)
    except auth_generated.ApiException as e:
        print("Exception when calling AuthServiceApi->auth_service_auth: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_auth_request** | [**AuthAuthRequest**](AuthAuthRequest.md)|  |

### Return type

[**AuthAuthResponse**](AuthAuthResponse.md)

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

# **auth_service_logout**
> bool, date, datetime, dict, float, int, list, str, none_type auth_service_logout()



Выход пользователя. Обязательно наличие токена в заголовках в виде Authorization: BEARER {JWT}

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import auth_generated
from auth_generated.api import auth_service_api
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
    api_instance = auth_service_api.AuthServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.auth_service_logout()
        pprint(api_response)
    except auth_generated.ApiException as e:
        print("Exception when calling AuthServiceApi->auth_service_logout: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **auth_service_refresh_token**
> AuthRefreshTokenResponse auth_service_refresh_token()



Запрос обновления токена. Обязательно наличие токена в заголовках в виде Authorization: BEARER {JWT}

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import auth_generated
from auth_generated.api import auth_service_api
from auth_generated.model.auth_refresh_token_response import AuthRefreshTokenResponse
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
    api_instance = auth_service_api.AuthServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.auth_service_refresh_token()
        pprint(api_response)
    except auth_generated.ApiException as e:
        print("Exception when calling AuthServiceApi->auth_service_refresh_token: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthRefreshTokenResponse**](AuthRefreshTokenResponse.md)

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

# **auth_service_switch_user**
> AuthSwitchUserResponse auth_service_switch_user(auth_switch_user_request)



Переключение пользователя. Обязательно наличие токена в заголовках в виде Authorization: BEARER {JWT}

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import auth_generated
from auth_generated.api import auth_service_api
from auth_generated.model.auth_switch_user_request import AuthSwitchUserRequest
from auth_generated.model.auth_switch_user_response import AuthSwitchUserResponse
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
    api_instance = auth_service_api.AuthServiceApi(api_client)
    auth_switch_user_request = AuthSwitchUserRequest(None) # AuthSwitchUserRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.auth_service_switch_user(auth_switch_user_request)
        pprint(api_response)
    except auth_generated.ApiException as e:
        print("Exception when calling AuthServiceApi->auth_service_switch_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_switch_user_request** | [**AuthSwitchUserRequest**](AuthSwitchUserRequest.md)|  |

### Return type

[**AuthSwitchUserResponse**](AuthSwitchUserResponse.md)

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

