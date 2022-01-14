# ManageGetStatusesResponseStatusInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор Vps (uuid) | [optional] 
**status** | **str** |  | [optional] 
**rescue_mode** | **bool** | Включен rescue-режим | [optional] 
**migrating** | **bool** | VPS находится в состоянии миграции на другой хост | [optional] 
**manage_enabled** | **bool** | Доступно ли управление VPS | [optional] 
**restoring** | **bool** | VPS находится в состоянии восстановления из резервной копии | [optional] 
**archived** | **bool** | VPS заархивирована, управление невозможно | [optional] 
**unblocking** | **bool** | VPS разблокируется после отключения по оплате или архивации | [optional] 
**unarchiving** | **bool** | VPS в процессе разархивации | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


