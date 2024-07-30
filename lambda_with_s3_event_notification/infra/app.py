#!/usr/bin/env python3


import aws_cdk as cdk
from infra.s3_event_notification_stack import LambdaWithS3EventNotificationEnvironments

app = cdk.App()
LambdaWithS3EventNotificationEnvironments(app,'lambda-with-s3-event-notifications')

app.synth()
