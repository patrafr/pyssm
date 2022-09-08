import boto3

AWS_REGION = "ap-southeast-1"

ec2_resource = boto3.resource('ec2', region_name=AWS_REGION)

volumes = ec2_resource.volumes.all()

for volume in ec2_resource.volumes.filter(
    Filters = [
        {
            "Name": "tag:Name",
            "Values": [
                "hands-on-cloud-ebs-boto3",
            ]
        }
    ]
    ):
    print(f"Volume {volume.id} ({volume.size} GiB) type: {volume.volume_type} -> {volume.state}")
    #print(volume)