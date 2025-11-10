#!/bin/python

import urllib.request
import boto3

URL = "https://media.giphy.com/media/3ohs4gt7vnva8bqmAg/giphy.gif"
FILE = "scooby.gif"
BUCKET = "ds2002-f25-wqa8hw"
EXPIRES = 604800

urllib.request.urlretrieve(URL, FILE)

s3 = boto3.client("s3", region_name="us-east-1")
with open(FILE, 'rb') as data:
	s3.put_object(
		Body=data,
		Bucket=BUCKET,
		Key=FILE
	)

response = s3.generate_presigned_url(
	'get_object',
	Params={'Bucket': BUCKET, 'Key': FILE},
	ExpiresIn=EXPIRES
)

print(response)
