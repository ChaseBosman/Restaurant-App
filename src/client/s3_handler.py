import logging
import boto3
import botocore
from botocore.exceptions import ClientError


class S3Handler:

    @staticmethod
    def upload_file(file_name, bucket, object_name=None):
        """Upload a file to an S3 bucket

        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = file_name

        # Upload the file
        s3_client = boto3.client('s3')
        try:
            response = s3_client.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    @staticmethod
    def download_file(file_name, bucket, new_file_name):
        s3_client = boto3.client('s3')
        try:
            s3_client.head_object(Bucket=bucket, Key=file_name,)
        except ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("doesnt exist")
                return False
            else:
                print("Critical error")
                return False
        else:
        # file exists so download it

            with open(new_file_name, 'wb') as file:
                s3_client.download_fileobj(bucket, file_name, file)
            return True

