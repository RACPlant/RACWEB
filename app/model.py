import os
import helper


BASE_DIR = os.path.dirname(__file__)
DATA = os.path.join(BASE_DIR, 'data.json')


class Arduino:
    def __init__(self, ard_id):
        self.id = ard_id
        self.port = None
        self.radiation = None
        self.temperature = None
        self.slots = []

    def load(self):
        data = helper.json_reader(DATA)
        for arduino in data:
            if self.id == arduino['id']:
                self.port = arduino['port']
                self.radiation = arduino['radiation']
                self.temperature = arduino['temperature']
        return self

    @classmethod
    def check_id(cls, ard_id):
        data = helper.json_reader(DATA)
        for arduino in data:
            if ard_id == arduino['id']:
                return True
        return False

    @classmethod
    def all(cls):
        data = helper.json_reader(DATA)
        return [Arduino(arduino['id']).load() for arduino in data]


class Slot:
    def __init__(self, slot_id):
        self.id = slot_id
        self.botanical_name = None
        self.name = None
        self.pump = None
        self.humidity = None


class Reader:
    pass
