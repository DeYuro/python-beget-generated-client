# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from auth_generated.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from auth_generated.model.auth_auth_request import AuthAuthRequest
from auth_generated.model.auth_auth_response import AuthAuthResponse
from auth_generated.model.auth_refresh_token_response import AuthRefreshTokenResponse
from auth_generated.model.auth_switch_user_request import AuthSwitchUserRequest
from auth_generated.model.auth_switch_user_response import AuthSwitchUserResponse
from auth_generated.model.key_get_key_response import KeyGetKeyResponse
