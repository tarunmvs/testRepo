import boto3
from botocore.exceptions import ClientError
import argparse

def launchTemplate(template_name):
    # Try to creat auto scaling group.
    try:
        client = boto3.client('ec2')
        response = client.create_launch_template(
            LaunchTemplateData={
                'ImageId': 'ami-8c1be5f6',
                'InstanceType': 't2.small',
                'NetworkInterfaces': [
                    {
                        'AssociatePublicIpAddress': True,
                        'DeviceIndex': 0,
                    },
                ],
                'TagSpecifications': [
                    {
                        'ResourceType': 'instance',
                        'Tags': [
                            {
                                'Key': 'Name',
                                'Value': 'webserver',
                            },
                        ],
                    },
                ],
            },
            LaunchTemplateName=template_name,
            VersionDescription='WebVersion1',
        )

        print(response)
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Template created")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="aws launch template")
    parser.add_argument("template_name",help="launch template name")

    args = parser.parse_args()

    template_name = args.template_name
    launchTemplate(template_name)
