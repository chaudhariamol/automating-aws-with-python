import boto3
session = boto3.Session(profile_name='pythonAutomation')
as_client = session.client('autoscaling')
#as_client.describe_auto_scaling_groups()
#as_client.describe_policies()

#execute scalaup or down policy from boto3
#as_client.execute_policy(AutoScalingGroupName= 'NotifonExampleGroup', PolicyName= 'ScaleDown')
as_client.execute_policy(AutoScalingGroupName= 'NotifonExampleGroup', PolicyName= 'ScalaUp')
