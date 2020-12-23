# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, getopt
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

# args
localFile = ''
bucket = ''

try:
    opts, args = getopt.getopt(sys.argv[1:], 'a:s:f:e:b:')
except getopt.GetoptError as err:
    print(str(err))
    exit()

for k, val in opts:
    if k == '-a':
        secret_id = val
    elif k == '-s':
        secret_key = val
    elif k == '-f':
        localFile = val
    elif k == '-e':
        region = val
    elif k == '-b':
        bucket_name = val

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
client = CosS3Client(config)

# upload
if os.path.isfile(localFile):
    client.put_object_from_local_file(
        Bucket=bucket_name,
        LocalFilePath=os.path.basename(localFile),
        Key=localFile,
    )
else:
    print(localFile + ' not exists!')

exit()
