import os
from constructs import Construct
from aws_cdk import (
    Stage,
    Environment,
    Stack,
    aws_lambda as _lambda,
    aws_s3 as _s3,
    aws_events as events,
    aws_events_targets as targets,
    Duration
)
import pathlib

class ComputeStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        event_bridge_lambda = _lambda.Function(
            self,
            "event-bridge-lambda",
            function_name="event-bridge-lambda",
            code=_lambda.Code.from_asset(
                str(pathlib.Path("../lambda/event_bridge_lambda").resolve())
            ),
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="index.handler",
        )

        bucket = _s3.Bucket.from_bucket_name(self, "bucket", "test-54-buck-tech")
        bucket.enable_event_bridge_notification()

        default_event_bus = events.EventBus.from_event_bus_name(
            self, "event-bud", "default"
        )

        s3_object_events = events.Rule(
            self,
            "s3-bucket-event",
            enabled=True,
            rule_name="buck-event-54",
            event_bus=default_event_bus,
            event_pattern={
                "source": ["aws.s3"],
                "detail_type": ["Object Created"],
                "detail": {"bucket": {"name": [bucket.bucket_name]}},
            },
        )
        s3_object_events.add_target(
            targets.LambdaFunction(
                handler=event_bridge_lambda,
                max_event_age=Duration.minutes(30),
                retry_attempts=3
            )
        )


class LambdaWithEventBridge(Stage):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        self.compute_stack = ComputeStack(self, "compute-stack")


class LambdaWithEventBridgeEnvironments(Stage):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        dev_stage = LambdaWithEventBridge(
            self,
            "dev",
            env=Environment(
                account=os.environ.get("CDK_DEFAULT_ACCOUNT"),
                region=os.environ.get("CDK_DEFAULT_REGION"),
            ),
        )