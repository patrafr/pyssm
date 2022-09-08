import boto3

AWS_REGION = "ap-southeast-1"

ec2_resource = boto3.resource('ec2', region_name=AWS_REGION)

for volume in ec2_resource.volumes.filter(
    VolumeIds=[
        'vol-043a70f4f80c6fd04',
        'vol-0f573dccd785ac897',
    ],
):
    print(f'Volume {volume.id} ({volume.size} GiB) -> {volume.state}')