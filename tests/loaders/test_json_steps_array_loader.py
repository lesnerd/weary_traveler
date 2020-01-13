import pytest

from loaders.json_steps_array_loader import JsonStepsArrayLoader


FILE_CONTAINING_ARRAY_LOCATION = "../files/full_json.json"
EMPTY_FILE = "../files/empty_json.json"

class TestJsonStepsArrayLoader:
    def test_load_has_array(self):
        array = JsonStepsArrayLoader.load(FILE_CONTAINING_ARRAY_LOCATION)
        assert isinstance(array, list) and len(array) > 0

    def test_load_empty_file(self):
        with pytest.raises(OSError):
            array = JsonStepsArrayLoader.load(EMPTY_FILE)