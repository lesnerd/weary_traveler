import pytest

from globals import PROJECT_ROOT
from loaders.json_steps_array_loader import JsonStepsArrayLoader


FILE_CONTAINING_ARRAY_LOCATION = "{project_root}/tests/unit/files/full_json.json".format(project_root=PROJECT_ROOT)
EMPTY_FILE = "{project_root}/tests/unit/files/empty_json.json".format(project_root=PROJECT_ROOT)

class TestJsonStepsArrayLoader:
    def test_load_has_array(self):
        array = JsonStepsArrayLoader.load(FILE_CONTAINING_ARRAY_LOCATION)
        assert isinstance(array, list) and len(array) > 0

    def test_load_empty_file(self):
        with pytest.raises(OSError):
            array = JsonStepsArrayLoader.load(EMPTY_FILE)