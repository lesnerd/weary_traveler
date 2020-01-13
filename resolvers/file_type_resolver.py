from enums.file_type import FileType
import os


class FileTypeResolver(object):

    @staticmethod
    def resolve(file_path):
        file_extension = os.path.splitext(file_path)[-1].split('.')[-1].upper()

        try:
            file_type = FileType[file_extension]
        except KeyError as e:
            if file_extension == '':
                raise RuntimeError('Not specified file extension.')
            raise RuntimeError('Unsupported file type {}.'.format(file_extension))

        return file_type