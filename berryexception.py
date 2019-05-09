import enum


class BerryException(Exception):
    keys = enum.Enum('keys','ONE TWO UNKNOWN')
    __errors = {keys.ONE: 'Error One'}

    def __init__(self, key):

        if isinstance(key, BerryException.keys):
            self.key = key
            self.message = BerryException.__errors[key]
        else:
            self.key = BerryException.keys.UNKNOWN
            self.message = key