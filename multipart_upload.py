import threading
import boto3
import os
import argparse
import sys

from boto3.s3.transfer import TransferConfig

s3 = boto3.resource('s3')

def multi_part_upload_with_s3(bucket_name,file_name,key_name):
    config = TransferConfig(multipart_threshold=1024, max_concurrency=5,
                            multipart_chunksize=1024, use_threads=True)
    file_path = os.path.dirname(__file__) + file_name
    s3.meta.client.upload_file(file_path, bucket_name, key_name,
                            ExtraArgs={'ContentType': 'text/pdf'},
                            Config=config,
                            )

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="s3 multi part upload")
    parser.add_argument("bucket_name",help="Enter the bucket name")
    parser.add_argument("file_name",help="enter the name of file to upload")
    parser.add_argument("key_name",help="enter the key name")

    args = parser.parse_args()

    bucket_name = args.bucket_name
    file_name = args.file_name
    key_name = args.key_name

    multi_part_upload_with_s3(bucket_name,file_name,key_name)
