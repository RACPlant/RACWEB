from app import app
from flask import abort, jsonify


@app.route("/", methods=['GET'])
def welcome():
    return jsonify({'msg': 'Bem vindos!'})


@app.route("/arduino/", methods=['GET'])
def list_arduino():
    return jsonify(
        [
            {
                'ard-01': {
                    'position': 'front-yard',  # lat long?
                    'label': 'Front Yard Station',
                    'started_at': '2019-11-05 10:50:31'
                }
            },
            {
                'ard-02': {
                    'position': 'back-yard',  # lat long?
                    'label': 'Front Yard Station',
                    'started_at': '2019-11-05 10:50:31'
                }
            }
        ]
    )


@app.route("/arduino/<path:ard_id>/plants/", methods=['GET'])
def list_plants(ard_id):
    arduino_id = __arduino_params(ard_id)
    # TODO: access data from specified arduino and retrieve associated plants
    return jsonify(
        [
            {
                'plant-01': {
                    'type': 'Capsicum frutescens',
                    'name': 'Pimenteira'
                }
            },
            {
                'plant-02': {
                    'type': 'Nephrolepis Exaltata',
                    'name': 'Samambaia'
                }
            }
        ]
    )


def __arduino_params(ard_id):
    if not ard_id or not ard_id.isnumeric():
        abort(404)
        return
    return int(ard_id)
