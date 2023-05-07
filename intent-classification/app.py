from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import time
import pkl2txt

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def hello_world():
    return 'Send requests to /classify to get responses'

@app.route("/classify", methods=["POST", "GET"])
def response():
    query = dict(request.form)['query']
    result = pkl2txt.findIntent(query)
    return jsonify({"intent" : result})

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port="5500")
