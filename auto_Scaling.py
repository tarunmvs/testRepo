import boto3
from botocore.exceptions import ClientError
import argparse

def auto_scaling(autoscaling_group_name,min_instances,max_instances,desired_instances,template_name):
    # Try to creat auto scaling group.
    try:
        client = boto3.client('autoscaling')
        response = client.create_auto_scaling_group(
            AutoScalingGroupName=autoscaling_group_name,
            LaunchTemplate={
                'LaunchTemplateName': template_name,
                'Version': '1'
            },
            MinSize=min_instances,
            MaxSize=max_instances,
            DesiredCapacity=desired_instances,
            DefaultCooldown=300,
            AvailabilityZones=[
                'us-east-1a',
            ]
        )

        print(response)

    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="s3 multi part upload")
    parser.add_argument("autoscaling_group_name",help="autoscaling group name")
    parser.add_argument("min_instances",help="minimum number of instances", type = int)
    parser.add_argument("max_instances",help="maximum number of instances", type = int)
    parser.add_argument("desired_instances",help="desired number of instances", type = int)
    parser.add_argument("template_name",help="name of template")

    args = parser.parse_args()

    autoscaling_group_name = args.autoscaling_group_name
    min_instances = args.min_instances
    max_instances = args.max_instances
    desired_instances = args.desired_instances
    template_name = args.template_name
    auto_scaling(autoscaling_group_name,min_instances,max_instances,desired_instances,template_name)
