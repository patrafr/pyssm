import boto3

AWS_REGION = "ap-southeast-1"

ec2_resource = boto3.resource('ec2', region_name=AWS_REGION)

volume = ec2_resource.Volume('vol-0b69cf5ec4f7360db')

if volume.state == "available":
    volume.delete()
    print("Volume succesfully deleted")
else:
    print("Unable to delete attached volume!")