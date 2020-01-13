from enums.file_type import FileType
from loaders.csv_steps_array_loader import CSVStepsArrayLoader
from loaders.json_steps_array_loader import JsonStepsArrayLoader
from loaders.tsv_steps_array_loader import TSVStepsArrayLoader


class FileStepsArrayLoaderResolver(object):
    def __init__(self):
        self.__loader_by_type = {
            FileType.CSV: CSVStepsArrayLoader,
            FileType.TSV: TSVStepsArrayLoader,
            FileType.JSON: JsonStepsArrayLoader,
        }

    def resolve(self, file_type):
        loader = self.__loader_by_type.get(file_type)

        if loader is None:
            raise RuntimeError("File type {} is not supported".format(file_type)) #check if there is a better error type

        return loader
