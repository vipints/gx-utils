from boto.s3.connection import S3Connection

aws_access_key = ''
aws_secret_access_key = '' 

aws_s3_bucket_name = ''

conn = S3Connection(aws_access_key, aws_secret_access_key) 
bucket = conn.get_bucket(aws_s3_bucket_name) 

for key in bucket.list():
    try:
        res = key.get_contents_to_filename(key.name)
    except:
        print("%s : Failed to fetch from bucket %s" % (key.name, aws_s3_bucket_name))
