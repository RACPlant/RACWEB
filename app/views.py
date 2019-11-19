from app import app
from flask import abort, jsonify
import model


@app.route("/", methods=['GET'])
def welcome():
    return jsonify({'msg': 'Bem vindos!'})


@app.route("/raspberry/<path:rasp_id>/arduino/", methods=['GET'])
def list_arduino(rasp_id):
    __raspberry_params(rasp_id)
    objs = model.Arduino.all()
    return jsonify(objs)


@app.route("/raspberry/<path:rasp_id>/arduino/<path:ard_id>/slots/", methods=['GET'])
def list_slots(rasp_id, ard_id):
    raspberry_id = __raspberry_params(rasp_id)
    arduino_id = __arduino_params(ard_id)
    # TODO: access data from specified arduino and retrieve associated slots
    return jsonify(
        {
            "0": {
                'botanical_name': 'Abelia chinensis',
                'name': 'Pimenteira',
                'pump': 'p1',
                'humidity': 'h1'
            },
            "1": {
                'botanical_name': 'Abelia floribunda',
                'name': 'Samambaia',
                'pump': 'p2',
                'humidity': 'h2'
            }
        }
    )


def __arduino_params(ard_id):
    if not ard_id or not ard_id.isnumeric():
        abort(404)
        return
    c_id = int(ard_id)
    if not model.Arduino.check_id(c_id):
        abort(404)
        return
    return int(c_id)


def __raspberry_params(rasp_id):
    if not rasp_id or not rasp_id.isnumeric():
        abort(404)
        return
