import threading
import boto3
import os
import sys

from boto3.s3.transfer import TransferConfig

BUCKET_NAME = "testbucketpythonautomation"
s3 = boto3.resource('s3')

def multi_part_upload_with_s3():
    config = TransferConfig(multipart_threshold=1024, max_concurrency=5,
                            multipart_chunksize=1024, use_threads=True)
    file_path = os.path.dirname(__file__) + 'largefile.pdf'
    key_path = 'multipart_files/largefile.pdf'
    s3.meta.client.upload_file(file_path, BUCKET_NAME, key_path,
                            ExtraArgs={'ContentType': 'text/pdf'},
                            Config=config,
                            )

if __name__ == '__main__':
    multi_part_upload_with_s3()
