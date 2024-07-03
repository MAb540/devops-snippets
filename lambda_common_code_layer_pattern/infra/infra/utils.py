import aws_cdk as cdk

from constructs import Construct


def get_config(scope: Construct, env: str) -> dict:
    app = cdk.App.of(scope)
    unparsed_env = app.node.try_get_context(env)
    build_config = unparsed_env["Parameters"]
    return build_config
