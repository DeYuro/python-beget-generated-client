# ManageVpsInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор Vps (uuid) | [optional] 
**slug** | **str** | ЧПУ-френдли имя Vps (может быть пустой строкой) | [optional] 
**display_name** | **str** | Отображаемое имя Vps | [optional] 
**hostname** | **str** | Имя хоста (в ОС) | [optional] 
**configuration** | [**ManageVpsConfiguration**](ManageVpsConfiguration.md) |  | [optional] 
**status** | **str** | Текущий статус Vps | [optional] 
**ssh_keys** | [**[StructuresSshKeyInfo]**](StructuresSshKeyInfo.md) | Информация об ssh-ключах | [optional] 
**has_password** | **bool** | Возможен ли вход по паролю | [optional] 
**manage_enabled** | **bool** | Доступно ли управление данной Vps | [optional] 
**description** | **str** | Дескрипшн для пользователя | [optional] 
**date_create** | **str** | Дата создания (в формате W3C) | [optional] 
**operating_system** | [**StructuresOperatingSystem**](StructuresOperatingSystem.md) |  | [optional] 
**ip_address** | **str** | Основной IP-адрес | [optional] 
**rescue_mode** | **bool** | Включен rescue-режим | [optional] 
**migrating** | **bool** | VPS находится в состоянии миграции на другой хост | [optional] 
**host_unavailable** | **bool** | Нет возможности получать информацию с хоста, на котором находится vps | [optional] 
**unblocking** | **bool** | VPS находится в состоянии разблокировки | [optional] 
**restoring** | **bool** | VPS находится в состоянии восстановления из резервной копии | [optional] 
**disk_used** | **str** | Занято места на главном разделе, Мб | [optional] 
**disk_left** | **str** | Осталось свободного места на главном разделе, Мб | [optional] 
**additional_ip_address** | **[str]** | Информация о дополнительных IP-адресах VPS | [optional] 
**beget_ssh_access_allowed** | **bool** | Согласие на доступ к пользовательской машине через SSH-ключи BeGet Необходимо для использования пользователем файлового менеджера | [optional] 
**archived** | **bool** | VPS заархивирована, управление невозможно | [optional] 
**unarchiving** | **bool** | VPS в процессе разархивации | [optional] 
**private_network** | [**[StructuresAttachedPrivateNetwork]**](StructuresAttachedPrivateNetwork.md) | Приватные сети к которым подключена VPS | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


