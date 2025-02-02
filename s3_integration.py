import boto3
import json
from config import s3_client, S3_BUCKET_NAME


def upload_to_s3(data, file_name, folder="interactions"):
    """
    Uploads data to S3 in JSON format.

    :param data: The data to be uploaded to S3.
    :param file_name: The name of the file that will be created in S3.
    :param folder: The folder in S3 where the file will be stored. Default is "interactions".
    """
    # Upload data to S3
    s3_client.put_object(
        Bucket=S3_BUCKET_NAME,
        Key=f"{folder}/{file_name}.json",  # Path where the file will be stored
        Body=json.dumps(data),  # Convert data to JSON before sending
        ContentType='application/json'
    )
    print(f"File {file_name}.json successfully uploaded to S3!")
