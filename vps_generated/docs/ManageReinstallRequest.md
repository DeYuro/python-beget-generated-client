# ManageReinstallRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор Vps (uuid) | [optional] 
**operating_system_id** | **int** | Идентификатор ОС (required) | [optional] 
**ssh_keys** | **[int]** | ID публичных ssh-ключей (предварительно созданные в системе) | [optional] 
**password** | **str** | Пароль (должен включать минимум 1 upper, 1 lower, 1 digit, 1 special char. Мин длина - 8 символов) | [optional] 
**software** | [**[ManageSoftwareInstallInfo]**](ManageSoftwareInstallInfo.md) | Информация о ПО, которое необходимо установить | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


