"""
Create the Music and User tables

This is intended to be used within a continuous integration test.
As such, it presumes that it is creating the tables in a local
DynamoDB instance.

It may work with the full AWS DynamoDB service but it has
not been tested on that.
"""

# Standard libraries

# Installed packages
import boto3

# Local modules

# Function definitions

def create_tables(url, region, access_key_id, secret_access_key, music, user):
    dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url=url,
        region_name=region,
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key)
    """
    ProvisionedThroughput is meaningless for local DynamoDB instances but
    required by the API.

    These create_table() calls are asynchronous and so will run in parallel.
    """
    mt = dynamodb.create_table(
        TableName=music,
        AttributeDefinitions=[{ "AttributeName": "music_id", "AttributeType": "S" }],
        KeySchema=[{ "AttributeName": "music_id", "KeyType": "HASH" }],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5}
    )
    ut = dynamodb.create_table(
        TableName=user,
        AttributeDefinitions=[{ "AttributeName": "user_id", "AttributeType": "S" }],
        KeySchema=[{ "AttributeName": "user_id", "KeyType": "HASH" }],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5}
    )
    """
    The order in which we wait for the tables is irrelevant.  We can only
    proceed after both exist.
    """
    mt.wait_until_exists()
    ut.wait_until_exists()
