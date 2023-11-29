import boto3
import sys

sys.path.append('/app')
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


def folder_exists(folder_name):
    s3 = boto3.client('s3')
    folder_prefix = f'{folder_name}/'
    response = s3.list_objects_v2(Bucket='discordbottranscription', Prefix=folder_prefix)

    if 'Contents' in response:
        return True
    else:
        return False

def create_folder(folder_name):
    s3 = boto3.client('s3')
    folder_key = f'{folder_name}/'
    s3.put_object(Bucket='discordbottranscription', Key=folder_key)