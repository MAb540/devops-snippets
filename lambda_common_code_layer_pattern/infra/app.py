#!/usr/bin/env python3

import aws_cdk as cdk


from infra.event_stack import EventDrivenEnvironments

app = cdk.App()

EventDrivenEnvironments(app, "event-driven-app")

app.synth()