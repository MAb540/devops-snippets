import os
import pathlib
from constructs import Construct
from aws_cdk import (
    Stage,
    Environment,
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda,
)


class ComputeStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        scrap_lambda = _lambda.Function(
            self,
            "scrap_lambda",
            code=_lambda.Code.from_asset(str(pathlib.Path("../lambda/trap").resolve())),
            handler="index.handler",
            runtime=_lambda.Runtime.PYTHON_3_11,
            function_name="scrap-lambda",
        )

        trap_lambda = _lambda.Function(
            self,
            "trap_lambda",
            code=_lambda.Code.from_asset(str(pathlib.Path("../lambda/trap").resolve())),
            handler="index.handler",
            runtime=_lambda.Runtime.PYTHON_3_11,
            function_name="trap-lambda",
        )

        utils_layer = _lambda.LayerVersion(
            self,
            "test-utils-layer",
            code=_lambda.Code.from_asset(
                str(pathlib.Path("../lambda/utils_layer").resolve())
            ),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_11],
        )

        scrap_lambda.add_layers(utils_layer)
        trap_lambda.add_layers(utils_layer)



class EventDrivenStage(Stage):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.compute_stack = ComputeStack(self, "compute-stack")


class EventDrivenEnvironments(Stage):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        dev_stage = EventDrivenStage(
            self,
            "dev",
            env=Environment(
                account=os.environ.get("CDK_DEFAULT_ACCOUNT"),
                region=os.environ.get("CDK_DEFAULT_REGION"),
            ),
        )
