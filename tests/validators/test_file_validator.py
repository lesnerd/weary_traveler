import pytest

from validators.file_validator import FileValidator

EXISTING_FILE_PATH = '/Users/lesnerd/Desktop/cartica_test_cases/Cartica test cases - Json.json'
NOT_EXISTING_FILE_PATH = 'dummy_file_path'

class TestFileValidator:
    def test_validate_existing(self):
        try:
            FileValidator.validate(EXISTING_FILE_PATH)
        except:
            pytest.fail('Could not find the file.')

    def test_validate_not_existing(self):
        with pytest.raises(IOError):
            FileValidator.validate(NOT_EXISTING_FILE_PATH)