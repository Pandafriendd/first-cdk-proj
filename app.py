#!/usr/bin/env python3

from aws_cdk import core

from cdk_helloworld.cdk_helloworld_stack import CdkHelloworldStack


app = core.App()
CdkHelloworldStack(app, "cdk-helloworld", env={'region': 'us-west-2'})

app.synth()
