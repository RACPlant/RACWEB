from app import app
from flask import abort, jsonify


@app.route("/", methods=['GET'])
def welcome():
    return jsonify({'msg': 'Bem vindos!'})

# TODO: criar endpoint referente ao raspberry
#
# 'position': 'front-yard',  # lat long?
# 'label': 'Front Yard Station',
# 'started_at': '2019-11-05 10:50:31'
#
# 'position': 'back-yard',  # lat long?
# 'label': 'Front Yard Station',
# 'started_at': '2019-11-05 10:50:31'
@app.route("/raspberry/<path:rasp_id>/arduino/", methods=['GET'])
def list_arduino(rasp_id):
    raspberry_id = __raspberry_params(rasp_id)
    # TODO: filter by specific raspberry_id
    return jsonify(
        [
            {
                'ard-01': {
                    'id': '0',
                    'port': '/dev/tty/ACM0',
                    'radiation': 'r1',
                    'temperature': 't1'
                }
            },
            {
                'ard-02': {
                    'id': '1',
                    'port': '/dev/tty/ACM1',
                    'radiation': 'r2',
                    'temperature': 't2'
                }
            }
        ]
    )


@app.route("/raspberry/<path:rasp_id>/arduino/<path:ard_id>/slots/", methods=['GET'])
def list_slots(rasp_id, ard_id):
    raspberry_id = __raspberry_params(rasp_id)
    arduino_id = __arduino_params(ard_id)
    # TODO: access data from specified arduino and retrieve associated slots
    return jsonify(
        [
            {
                'botanical-name': 'Abelia chinensis',
                'name': 'Pimenteira',
                'pump': 'p1',
                'humidity': 'h1'
            },
            {
                'botanical-name': 'Abelia floribunda',
                'name': 'Samambaia',
                'pump': 'p2',
                'humidity': 'h2'
            }
        ]
    )


def __arduino_params(ard_id):
    if not ard_id or not ard_id.isnumeric():
        abort(404)
        return
    return int(ard_id)


def __raspberry_params(rasp_id):
    if not rasp_id or not rasp_id.isnumeric():
        abort(404)
        return
    return int(rasp_id)
