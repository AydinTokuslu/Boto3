import boto3
client = boto3.client('s3')

file_reader = open('s3-create_bucket.py').read()
response = client.put_object(
    ACL='private',
    Body=file_reader,
    Bucket='javahomecloud123',
    Key='s3-create_bucket.py'
)