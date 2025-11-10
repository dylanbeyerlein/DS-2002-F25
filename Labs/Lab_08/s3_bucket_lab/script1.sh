#!/bin/bash

FILE="$1"
BUCKET="$2"
EXPIRES="$3"

aws s3 cp "$FILE" "s3://$BUCKET/$FILE"
aws s3 presign --expires-in "$EXPIRES" "s3://$BUCKET/$FILE"
