import json
import pytest

from aws_cdk import core
from cdk-helloworld.cdk_helloworld_stack import CdkHelloworldStack


def get_template():
    app = core.App()
    CdkHelloworldStack(app, "cdk-helloworld")
    return json.dumps(app.synth().get_stack("cdk-helloworld").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
