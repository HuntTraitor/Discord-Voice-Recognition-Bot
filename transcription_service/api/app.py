from flask import Flask, make_response, jsonify, request, render_template, send_file, redirect
from routeFunctions.upload_file import upload
from helpers.file_helpers import delete_files
import sys
import boto3

sys.path.append('/app')
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

app = Flask(__name__)

# enbables or disables use for AWS to not overload it when testing
USE_AWS = True

# This route uploads files
# You want to pass in a guildId string body - EX. "1234567"
@app.route('/upload', methods=['PUT'])
def upload_file():
    try:
        data = request.get_json()
        guildID = data['guild']

        if USE_AWS:
            upload(guildID)
            delete_files(guildID)
        
        response_data = {'success': True, 'data': data}
        response = make_response(jsonify(response_data), 200)
        return response
    except Exception as e:
        print(f"Error on a /upload request: {e}")
        response_data = {'success': False, 'error': str(e)}
        response = make_response(jsonify(response_data), 400)
        return response
    
@app.route('/list/<guildId>', methods=['GET'])
def list_files(guildId):
    try:
        s3 = boto3.client('s3')

        folder_path = f'{guildId}/'
        objects = s3.list_objects_v2(Bucket='discordbottranscription', Prefix=folder_path)
        text_files = [obj['Key'] for obj in objects.get('Contents', []) if obj['Key'].endswith('.txt')]
        html = render_template('file_list.html', text_files=text_files)
        return html
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    

@app.route('/download_file/<guildId>/<filename>', methods=['GET'])
def download_file(guildId, filename):
    try:
        s3 = boto3.client('s3')
        folder_path = f'{guildId}/'
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={'Bucket':'discordbottranscription', 'Key': folder_path + filename},
            ExpiresIn=500
        )
        return redirect(url)
    except Exception as e:
        return jsonify({'error': str(e)}), 400



if __name__ == '__main__':
    app.run(host='10.10.0.3', port='8000')