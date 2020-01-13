import json
import os


class JsonStepsArrayLoader(object):
    @staticmethod
    def load(file_path):
        if os.stat(file_path).st_size > 0:
            with open(file_path, 'r') as file:
                return json.load(file)
        raise OSError('File is empty.')