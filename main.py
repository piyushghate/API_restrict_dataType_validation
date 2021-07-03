from flask import Flask, jsonify, request
from json import dumps, loads
from handler_file import function101
from marshmallow import Schema, fields, ValidationError

from utils import logger

class BaseSchema(Schema):
    age = fields.Integer(required=True)
    firstName = fields.String(required=True)
    lastName = fields.String(required=True)

class ExtendedSchema(BaseSchema):
    value = fields.Integer()

app = Flask(__name__)
app.config["DEBUG"] = True

@app.before_request
def check():
    logger.info("request.host_url--> %s", str(request.host_url))
    if request.host_url != "http://127.0.0.1:5000/":
        return {"Message": "Not Authorized", "Status": "Failed"}, 400

@app.route('/path123', methods=['POST'])
def home():
    json_data = request.get_json()
    logger.info("request_json --> %s", str(json_data))
    schema = ExtendedSchema()
    try:
        result = schema.load(json_data)
        logger.info ("result--> %s", str(result))
    except ValidationError as err:
        logger.info("err --> %s",str(err))
        return jsonify(err.messages), 400

    #data_now_json_str = dumps(result)
    logger.info("request_json2 --> %s", str(json_data))
    processed_values = function101(json_data)
    return processed_values

app.run()
