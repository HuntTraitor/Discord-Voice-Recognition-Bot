import boto3
import sys

sys.path.append('/app')
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

# checks if folder exists (NOT OBVIOUS HAHA!)
def folder_exists(folder_name):
    try:
        s3 = boto3.client('s3')
        folder_prefix = f'{folder_name}/'
        response = s3.list_objects_v2(Bucket='discordbottranscription', Prefix=folder_prefix)
    except Exception as e:
        print(f"Failed to check if folder exists for {folder_name}: {e}")

    if 'Contents' in response:
        return True
    else:
        return False

# Creates folder in s3 bucket
# Convention is you should pass a guildId in the folder_name parameter
def create_folder(folder_name):
    try:
        s3 = boto3.client('s3')
        folder_key = f'{folder_name}/'
        s3.put_object(Bucket='discordbottranscription', Key=folder_key)
    except Exception as e:
        print(f"Failed to create folder for {folder_name}: {e}")
