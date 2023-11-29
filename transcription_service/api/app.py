from flask import Flask, make_response, jsonify, request
from routeFunctions.upload_file import upload
from helpers.file_helpers import delete_files

app = Flask(__name__)

@app.route('/upload', methods=['PUT'])
def upload_file():
    try:
        data = request.get_json()
        guildID = data['guild']

        upload(guildID)
        delete_files(guildID)
        
        response_data = {'success': True, 'data': data}
        response = make_response(jsonify(response_data), 200)
        return response
    except Exception as e:
        print(e)
        response_data = {'success': False, 'error': str(e)}
        response = make_response(jsonify(response_data), 400)
        return response
    

if __name__ == '__main__':
    app.run(host='10.10.0.3', port='8000')