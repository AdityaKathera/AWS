# Script to check if S3 Bucket CORS exists 
import boto3
from botocore.exceptions import ClientError
from datetime import timezone, date, datetime, timedelta
results = []
def scan():
    s3 = boto3.client('s3')

    bucket_list = s3.list_buckets()
    for bucket in bucket_list['Buckets']:
        try:
            bucket_policy = s3.get_bucket_policy(Bucket=bucket['Name'])
            results.append({
                'BucketName': bucket['Name'],
                'BucketPolicy': 'Policy Exists, Please check your AWS account to view the policy'
            })

        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchBucketPolicy':
                results.append({
                'BucketName': bucket['Name'],
                'BucketPolicy': 'Bucket Policy does not exist'
            })
            else:
                results.append({
                'BucketName': 'Unexpected Error',
            })
    print(results)
scan()