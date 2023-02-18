import boto3

ec2 = boto3.resource("ec2")

for instance in ec2.instances.all():
    print("Instance id is {} and Instance type is {} ".format(instance.instance_id, instance.instance_type))
    # Instance id is i-0bed83164f56d3eb9 and Instance type is t2.micro 