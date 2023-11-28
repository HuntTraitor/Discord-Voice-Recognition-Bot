import boto3
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

def upload(file_path, guildID):
    print(file_path)
    s3 = boto3.client('s3')
    s3.upload_file(file_path, 'discordbottranscription', 'transcription.txt')

# upload("transcriptions/1167939648530694165--2023-11-28 22:40:42.txt")