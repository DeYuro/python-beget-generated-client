# StructuresOperatingSystem

Описывает ОС для установки на Vps (пара дистрибутив + версия)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Идентификатор ОС | [optional] 
**distro_name** | **str** | Системное имя дистрибутива (например, для группировки) | [optional] 
**distro_display_name** | **str** | Отображаемое имя дистрибутива | [optional] 
**version** | **str** | Версия дистрибутива (отображаемое значение) | [optional] 
**active** | **bool** | Доступна ли ОС для выбора пользователю (визуально) | [optional] 
**requirements** | [**StructuresOperatingSystemRequirements**](StructuresOperatingSystemRequirements.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


