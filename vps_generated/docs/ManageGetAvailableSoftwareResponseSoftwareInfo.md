# ManageGetAvailableSoftwareResponseSoftwareInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Внутреннее имя (напр. redmine) | [optional] 
**display_name** | **str** | Отображаемое имя (напр. Redmine) | [optional] 
**version** | **str** | Версия (напр. 1.0.1) | [optional] 
**type** | **str** | Тип ПО (панель управления, обычное ПО) | [optional] 
**description** | **str** | Описание ПО | [optional] 
**description_version** | **str** | Дополнительное описание для конкретной версии ПО | [optional] 
**image_id** | **[int]** | Список ID образов, для которых возможна установка этого ПО | [optional] 
**variable** | **[str]** | Список дополнительных полей, которые необходимо передать для установки ПО | [optional] 
**requirements** | [**ManageGetAvailableSoftwareResponseSoftwareInfoRequirements**](ManageGetAvailableSoftwareResponseSoftwareInfoRequirements.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


