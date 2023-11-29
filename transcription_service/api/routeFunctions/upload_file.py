import boto3
import sys
import os

sys.path.append('/app')
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from api.helpers.s3_helpers import folder_exists, create_folder

# Uploads file to subsequent guildId folder
def upload(guildID):
    transcription_path = "/app/transcriptions"
    folder_path = os.path.abspath(transcription_path)
    files = os.listdir(folder_path)

    for file in files:
        if not file.startswith('.'): # ignore hidden files
            id, filename = file.split("--")
            if id == guildID:
                if not folder_exists(id):
                    create_folder(id)
                    print(f"Created folder for {id}")

                try:
                    s3 = boto3.client('s3')
                    s3.upload_file(f'/app/transcriptions/{file}', 'discordbottranscription', f'{id}/{filename}')
                except Exception as upload_error:
                    print(f"Error uploading {file} to S3: {upload_error}")     
