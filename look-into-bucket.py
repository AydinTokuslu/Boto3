import boto3

# aradığımız bir bucketın içindeki objeleri listeleme

s3 = boto3.resource("s3")

my_bucket=s3.Bucket("osvaldo-vpc-44")

for file in my_bucket.objects.all():
    print(file.key)
    print(my_bucket.name)

# folder içini görmek

# for file in my_bucket.objects.filter(Prefix="FOLDER ISMI (UZANTISI DAHIL)"):
#     print(file.key)
#     print(my_bucket.name)