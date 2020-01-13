from unittest.mock import MagicMock

from enums.file_type import FileType
from services.path_finder_service import PathFinderService

STEPS_ARRAY = [1, 2, 3]

FILE_PATH = 'dummy_file_path'


class TestPathFinderService(object):
    def setup_method(self):
        self.__file_validator = MagicMock()
        self.__steps_array_validator = MagicMock()
        self.__file_type_resolver = MagicMock()
        self.__file_steps_array_loader_resolver = MagicMock()
        self.__path_finder_algo = MagicMock()

        self.__service = PathFinderService(
            self.__file_validator,
            self.__steps_array_validator,
            self.__file_type_resolver,
            self.__file_steps_array_loader_resolver,
            self.__path_finder_algo)

    def test_find(self):
        file_loader_mock = MagicMock()

        self.__file_type_resolver.resolve.return_value = FileType.CSV
        self.__file_steps_array_loader_resolver.resolve.return_value = file_loader_mock
        file_loader_mock.load.return_value = STEPS_ARRAY
        self.__path_finder_algo.find.return_value = True

        actual_result = self.__service.find(FILE_PATH)

        assert actual_result, "Result was not as expected"

        self.__file_validator.validate.assert_called_with(FILE_PATH)
        self.__file_type_resolver.resolve.assert_called_with(FILE_PATH)
        self.__file_steps_array_loader_resolver.resolve.assert_called_with(FileType.CSV)
        file_loader_mock.load.assert_called_with(FILE_PATH)
        self.__steps_array_validator.validate.assert_called_with(STEPS_ARRAY)
        self.__path_finder_algo.find.assert_called_with(STEPS_ARRAY)







