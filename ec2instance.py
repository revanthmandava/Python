#!/usr/bin/env python
from __future__ import print_function
import sys
import boto3
def lambda_handler(event, context):
   ec2 = boto3.client('ec2')
   ec2_resource = boto3.resource('ec2')
   response = ec2.describe_instances()
   for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print ("InstanceIDs", instance['InstanceId'])
            ec2_resource.instances.filter(InstanceIds=[instance['InstanceId']]).terminate()
            #res = instance.terminate(instance['InstanceId'])
