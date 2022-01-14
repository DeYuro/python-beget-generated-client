
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.backup_service_api import BackupServiceApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from vps_generated.api.backup_service_api import BackupServiceApi
from vps_generated.api.manage_service_api import ManageServiceApi
from vps_generated.api.network_service_api import NetworkServiceApi
from vps_generated.api.snapshot_service_api import SnapshotServiceApi
from vps_generated.api.ssh_key_service_api import SshKeyServiceApi
from vps_generated.api.statistic_service_api import StatisticServiceApi
