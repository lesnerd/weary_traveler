import pandas
import pytest

from globals import PROJECT_ROOT
from loaders.tsv_steps_array_loader import TSVStepsArrayLoader

FILE_CONTAINING_ARRAY_LOCATION = "{project_root}/tests/unit/files/ok.tsv".format(project_root=PROJECT_ROOT)
FILE_NOT_CONTAINING_ARRAY_LOCATION = "{project_root}/tests/unit/files/not_ok.tsv".format(project_root=PROJECT_ROOT)
EMPTY_FILE = "{project_root}/tests/unit/files/empty_tsv.tsv".format(project_root=PROJECT_ROOT)

class TestTSVStepsArrayLoader:
    def test_load_has_array(self):
        array = TSVStepsArrayLoader.load(FILE_CONTAINING_ARRAY_LOCATION)
        assert isinstance(array, list) and len(array) > 0

    def test_load_has_no_array_content(self):
        with pytest.raises(OSError):
            array = TSVStepsArrayLoader.load(FILE_NOT_CONTAINING_ARRAY_LOCATION)

    def test_load_empty_file(self):
        with pytest.raises(pandas.errors.EmptyDataError):
            array = TSVStepsArrayLoader.load(EMPTY_FILE)


