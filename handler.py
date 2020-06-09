"""
Simple example for Lambda->SQS->Lambda.
"""

import os
import boto3

# SQS_CLIENT = boto3.client('sqs')

SQS_CLIENT = boto3.Session(region_name='ap-south-1').client(
    'sqs',
    aws_access_key_id='x',
    aws_secret_access_key='x',
    endpoint_url='http://localhost:9324')


def start(event, context):
    """
    First Lambda function. Triggered manually.
    """
    # print(SQS_CLIENT.send_message(
    #     QueueUrl=os.getenv('SQS_URL'),
    #     MessageBody='test'
    # ))
    SQS_CLIENT.send_message(QueueUrl=os.getenv(
        'SQS_URL'), MessageBody="This is a test message")
    print("Hello sqs! From Akash")
    return 'Done Start'


def end(event, context):
    """
    Second Lambda function. Triggered by the SQS.
    """
    print(event)
    print("Bye bye sqs! From Akash")
    return 'Done End'
