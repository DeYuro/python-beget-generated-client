# SnapshotRestore


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | restore order id | [optional] 
**snapshot** | [**SnapshotSnapshot**](SnapshotSnapshot.md) |  | [optional] 
**vps_id** | **str** | target vps id | [optional] 
**vps_name** | **str** | target vps name | [optional] 
**target_type** | **str** | restore type: existing or new vps | [optional] 
**date_create** | **str** | start restore datetime (RFC3339) | [optional] 
**date_complete** | **str** | finish restore datetime (RFC3339) | [optional] 
**status** | **str** | current restore status | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


