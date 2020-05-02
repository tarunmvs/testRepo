import boto3

session = boto3.Session(profile_name='pythonAutomation')

s3 = session.resource('s3')

s3.create_bucket(Bucket = "botopythonautomation-1234",CreateBucketConfiguration={'LocationConstraint':'us-east-2'})

for bucket in s3.buckets.all():
    print(bucket)
