# ManageCreateVpsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Отображаемое имя Vps (required) | [optional] 
**hostname** | **str** | Имя хоста (в ОС) | [optional] 
**description** | **str** | Дескрипшн (опциональный). просто какой-нить текст | [optional] 
**configuration_id** | **str** | Идентификатор конфигурации (required) | [optional] 
**operating_system_id** | **int** | Идентификатор ОС oneof{source} | [optional] 
**snapshot_id** | **str** | Идентификатор снапшота, который восстановится в новую Vps oneof{source} | [optional] 
**ssh_keys** | **[int]** | ID публичных ssh-ключей (предварительно созданные в системе) | [optional] 
**password** | **str** | Пароль (должен включать минимум 1 upper, 1 lower, 1 digit, 1 special char. Мин длина - 8 символов) | [optional] 
**beget_ssh_access_allowed** | **bool** | Согласие на доступ к пользовательской машине через SSH-ключи BeGet Необходимо для использования пользователем файлового менеджера | [optional] 
**software** | [**[ManageSoftwareInstallInfo]**](ManageSoftwareInstallInfo.md) | Информация о ПО, которое необходимо установить | [optional] 
**private_networks** | [**[ManagePrivateNetworkInfo]**](ManagePrivateNetworkInfo.md) | Приватные сети, к которым необходимо подключить VPS | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


