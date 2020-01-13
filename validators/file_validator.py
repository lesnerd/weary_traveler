import os


class FileValidator(object):
    @staticmethod
    def validate(file_path):
        if not os.path.isfile(file_path):
            raise IOError("No such file path {}".format(file_path))