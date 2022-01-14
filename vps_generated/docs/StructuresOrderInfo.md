# StructuresOrderInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор задания | [optional] 
**vps_id** | **str** | Идентификатор VPS (uuid) | [optional] 
**vps_name** | **str** | Имя сервера, на который выполнялось восстановление | [optional] 
**type** | **str** | Тип задания | [optional] 
**date_create** | **str** | Дата создания задания (RFC3339) | [optional] 
**date_complete** | **str** | Дата завершения задания (RFC3339) | [optional] 
**path** | **[str]** | Список путей для восстановления/скачивания | [optional] 
**status** | **str** | Статус завершения | [optional] 
**copy_info** | [**StructuresCopyInfo**](StructuresCopyInfo.md) |  | [optional] 
**affect_live** | **bool** | Операция производится без выключения VPS | [optional] 
**target** | **str** | Директория, в которую производилось восстановление (актуально для выборочного восстановления файлов) | [optional] 
**error_details** | [**StructuresOrderInfoErrorDetails**](StructuresOrderInfoErrorDetails.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


