import botconfig as cfg
import boto3
import pprint
from botocore.exceptions import ClientError

instance_id = cfg.instance_id
pp = pprint.PrettyPrinter(indent=4)

def describeInstances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(InstanceIds=[instance_id])
    #pp.pprint(response)
    #response = response['Reservations'][0]['Instances'][0]['State']['Name']
    return(response)

def describeStatus(response):
    status = response['Reservations'][0]['Instances'][0]['State']['Name']
    return(status)

def startInstance():
    ec2 = boto3.client('ec2')
    try:
        response = ec2.start_instances(InstanceIds=[instance_id])
        print(response)
    except ClientError as e:
        print(e)

def stopInstance():
    ec2 = boto3.client('ec2')
    try:
        response = ec2.stop_instances(InstanceIds=[instance_id])
        print(response)
    except ClientError as e:
        print(e)