import boto3

s3 = boto3.client('s3', region_name="us-east-1")
bucket = 'ds2002-f25-wqa8hw'
local_file = 'old_dorms.png'

# 1. Open the file in binary read mode ('rb')
with open(local_file, 'rb') as data:
    resp = s3.put_object(
        Body=data,        # PASS THE OPEN FILE OBJECT HERE
        Bucket=bucket,
        Key=local_file,    # This is the destination key/path in S3
	ACL='public-read'
)
