from flask import Flask, make_response, jsonify
from route_functions.upload_file import upload

app = Flask(__name__)

@app.route('/upload/<filename>')
def upload(filename):

    result = upload(filename)

    if result:
        reponse_data = {'message': 'Success'}
        status_code = 200
    else:
        response_data = {'message':'Failure'}
        status_code = 400
    
    response = make_response(jsonify(response_data), status_code)
    return response

if __name__ == '__main__':
    app.run()