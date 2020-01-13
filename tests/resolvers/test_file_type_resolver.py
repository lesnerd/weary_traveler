import pytest

from enums.file_type import FileType
from resolvers.file_type_resolver import FileTypeResolver

SUPPORTED_FILE_EXTENSION = 'cartica/files/steps.csv'
UNSUPPORTED_FILE_EXTENSION = 'cartica/files/steps.txt'
INVALID_FILE_PATH = 'cartica/files/steps'


class TestFileTypeResolver(object):
    def test_resolve(self):
        actual_file_type = FileTypeResolver.resolve(SUPPORTED_FILE_EXTENSION)

        assert actual_file_type == FileType.CSV

    def test_resolve_unsupported_file_type(self):
        with pytest.raises(RuntimeError):
            FileTypeResolver.resolve(UNSUPPORTED_FILE_EXTENSION)

    def test_resolve_invalid_file_path(self):
        with pytest.raises(RuntimeError):
            FileTypeResolver.resolve(INVALID_FILE_PATH)


