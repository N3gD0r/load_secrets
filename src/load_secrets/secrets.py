from botocore.exceptions import ClientError

import boto3
import json


def get_secrets(secret_name: str) -> dict:
    session = boto3.session.Session()
    secrets_manager_client = session.client(
        service_name='secretsmanager'
    )

    try:
        secret = secrets_manager_client.get_secret_value(SecretId=secret_name)
        creds = json.loads(secret['SecretString'])
        return creds
    except (ClientError, json.JSONDecodeError, ValueError) as e:
        return {}

