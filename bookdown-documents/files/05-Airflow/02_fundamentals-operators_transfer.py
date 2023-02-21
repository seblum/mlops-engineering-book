
# pip install 'apache-airflow-providers-google'
# pip install 'apache-airflow-providers-amazon'
# pip install 'apache-airflow-providers-microsoft-azure'

from airflow.providers.google.cloud.transfers.azure_fileshare_to_gcs import AzureFileShareToGCSOperator
from airflow.providers.amazon.aws.transfers.dynamodb_to_s3 import DynamoDBToS3Operator
from airflow.providers.amazon.aws.transfers.google_api_to_s3 import GoogleApiToS3Operator
from airflow.models import DAG
from pendulum import datetime

# DISCLAIMER
# This script is not fully functional. Please adhere to the official documentation

transfer_operator_fundamentals = DAG(
    dag_id='transfer_operator_fundamentals',
    start_date=datetime(2023, 1, 1, tz="Europe/Amsterdam"),
    schedule_interval=None
)


# GoogleApiToS3Operator

google_sheet_id = <GOOGLE-SHEET-ID >
google_sheet_range = <GOOGLE-SHEET-RANGE >
s3_destination_key = <S3-DESTINATION-KEY >

task_google_sheets_values_to_s3 = GoogleApiToS3Operator(
    task_id="google_sheet_data_to_s3",
    google_api_service_name="sheets",
    google_api_service_version="v4",
    google_api_endpoint_path="sheets.spreadsheets.values.get",
    google_api_endpoint_params={
        "spreadsheetId": google_sheet_id, "range": google_sheet_range},
    s3_destination_key=s3_destination_key,
)


# DynamoDBToS3Operator

table_name = <TABLE-NAME >
bucket_name = <BUCKET-NAME >

backup_db = DynamoDBToS3Operator(
    task_id="backup_db",
    dynamodb_table_name=table_name,
    s3_bucket_name=bucket_name,
    # Max output file size in bytes.  If the Table is too large, multiple files will be created.
    file_size=20,
)


# AzureFileShareToGCSOperator

azure_share_name = <AZURE-SHARE-NAME >
bucket_name = <BUCKET-NAME >
azure_directory_name = <AZURE-DIRECTORY-NAME >

sync_azure_files_with_gcs = AzureFileShareToGCSOperator(
    task_id="sync_azure_files_with_gcs",
    share_name=azure_share_name,
    dest_gcs=bucket_name,
    directory_name=azure_directory_name,
    replace=False,
    gzip=True,
    google_impersonation_chain=None,
)
