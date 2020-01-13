import pandas
import pytest

from globals import PROJECT_ROOT
from loaders.csv_steps_array_loader import CSVStepsArrayLoader

FILE_CONTAINING_ARRAY_LOCATION = "{project_root}/tests/unit/files/ok.csv".format(project_root=PROJECT_ROOT)
FILE_NOT_CONTAINING_ARRAY_LOCATION = "{project_root}/tests/unit/files/not_ok.csv".format(project_root=PROJECT_ROOT)
EMPTY_FILE = "{project_root}/tests/unit/files/empty_csv.csv".format(project_root=PROJECT_ROOT)


class TestCSVStepsArrayLoader:
    def test_load(self):
        array = CSVStepsArrayLoader.load(FILE_CONTAINING_ARRAY_LOCATION)
        assert isinstance(array, list) and len(array) > 0

    def test_load_has_no_array_content(self):
        with pytest.raises(OSError):
            CSVStepsArrayLoader.load(FILE_NOT_CONTAINING_ARRAY_LOCATION)

    def test_load_empty_file(self):
        with pytest.raises(pandas.errors.EmptyDataError):
            CSVStepsArrayLoader.load(EMPTY_FILE)
