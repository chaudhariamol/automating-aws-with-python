# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
key_name='python_automation_key'
key_path=key_name+'.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
key_name='python_automation_key1'
key_path=key_name+'.pem'

key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file:
	key_file.write(key.key_material)
    
import os, stat
os.chmod(key_path, stat.S_IRUSR|stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-la')
ami_name='amzn2-ami-hvm-2.0.20190115-x86_64-gp2'
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
img = ec2.Image('ami-04328208f4f0cf1fe')
img.name
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst = instances[0]
inst.public_dns_name
inst.wait_until_running()
inst.reload() ##reoad data from AWS
inst.public_dns_name
inst.security_groups
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CiderIp': '92.238.29.57/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '92.238.29.57/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '92.238.29.57/32'}]}])
