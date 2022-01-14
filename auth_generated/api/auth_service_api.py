"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from auth_generated.api_client import ApiClient, Endpoint as _Endpoint
from auth_generated.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from auth_generated.model.auth_auth_request import AuthAuthRequest
from auth_generated.model.auth_auth_response import AuthAuthResponse
from auth_generated.model.auth_refresh_token_response import AuthRefreshTokenResponse
from auth_generated.model.auth_switch_user_request import AuthSwitchUserRequest
from auth_generated.model.auth_switch_user_response import AuthSwitchUserResponse


class AuthServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.auth_service_auth_endpoint = _Endpoint(
            settings={
                'response_type': (AuthAuthResponse,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/v1/auth',
                'operation_id': 'auth_service_auth',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'auth_auth_request',
                ],
                'required': [
                    'auth_auth_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'auth_auth_request':
                        (AuthAuthRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'auth_auth_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.auth_service_logout_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/v1/auth/logout',
                'operation_id': 'auth_service_logout',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.auth_service_refresh_token_endpoint = _Endpoint(
            settings={
                'response_type': (AuthRefreshTokenResponse,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/v1/auth/refresh',
                'operation_id': 'auth_service_refresh_token',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.auth_service_switch_user_endpoint = _Endpoint(
            settings={
                'response_type': (AuthSwitchUserResponse,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/v1/auth/switch',
                'operation_id': 'auth_service_switch_user',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'auth_switch_user_request',
                ],
                'required': [
                    'auth_switch_user_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'auth_switch_user_request':
                        (AuthSwitchUserRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'auth_switch_user_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def auth_service_auth(
        self,
        auth_auth_request,
        **kwargs
    ):
        """auth_service_auth  # noqa: E501

        Запрос авторизации пользователя.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auth_service_auth(auth_auth_request, async_req=True)
        >>> result = thread.get()

        Args:
            auth_auth_request (AuthAuthRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AuthAuthResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['auth_auth_request'] = \
            auth_auth_request
        return self.auth_service_auth_endpoint.call_with_http_info(**kwargs)

    def auth_service_logout(
        self,
        **kwargs
    ):
        """auth_service_logout  # noqa: E501

        Выход пользователя. Обязательно наличие токена в заголовках в виде Authorization: BEARER {JWT}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auth_service_logout(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.auth_service_logout_endpoint.call_with_http_info(**kwargs)

    def auth_service_refresh_token(
        self,
        **kwargs
    ):
        """auth_service_refresh_token  # noqa: E501

        Запрос обновления токена. Обязательно наличие токена в заголовках в виде Authorization: BEARER {JWT}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auth_service_refresh_token(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AuthRefreshTokenResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.auth_service_refresh_token_endpoint.call_with_http_info(**kwargs)

    def auth_service_switch_user(
        self,
        auth_switch_user_request,
        **kwargs
    ):
        """auth_service_switch_user  # noqa: E501

        Переключение пользователя. Обязательно наличие токена в заголовках в виде Authorization: BEARER {JWT}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auth_service_switch_user(auth_switch_user_request, async_req=True)
        >>> result = thread.get()

        Args:
            auth_switch_user_request (AuthSwitchUserRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AuthSwitchUserResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['auth_switch_user_request'] = \
            auth_switch_user_request
        return self.auth_service_switch_user_endpoint.call_with_http_info(**kwargs)

