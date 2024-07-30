import os
from aws_cdk import (
    Stage,
    Stack,
    Environment,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_s3_notifications as s3_notifications,
)
from constructs import Construct
import pathlib


class ComputeStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(self, "test-bucki-90", bucket_name="test-bucki-90")

        event_notification_lambda = _lambda.Function(
            self,
            "s3-event-notification-lambda",
            function_name="s3-event-notification-lambda",
            code=_lambda.Code.from_asset(
                str(pathlib.Path("../lambda/s3_event_notification").resolve())
            ),
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="index.handler",
        )

        bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3_notifications.LambdaDestination(event_notification_lambda),
        )


class LambdaWithS3EventNotification(Stage):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.compute_stack = ComputeStack(self, "compute-stack")


class LambdaWithS3EventNotificationEnvironments(Stage):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        dev_stage = LambdaWithS3EventNotification(
            self,
            "dev",
            env=Environment(
                account=os.environ.get("CDK_DEFAULT_ACCOUNT"),
                region=os.environ.get("CDK_DEFAULT_REGION"),
            ),
        )
