#!/usr/bin/env python3

import aws_cdk as cdk
from infra.event_stack import LambdaWithEventBridgeEnvironments

app = cdk.App()


LambdaWithEventBridgeEnvironments(app,"lambda-with-event-bridge")
app.synth()
