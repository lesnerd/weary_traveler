import pandas
import pytest

from loaders.csv_steps_array_loader import CSVStepsArrayLoader

FILE_CONTAINING_ARRAY_LOCATION = "../files/ok.csv"
FILE_NOT_CONTAINING_ARRAY_LOCATION = "../files/not_ok.csv"
EMPTY_FILE = "../files/empty_csv.csv"


class TestCSVStepsArrayLoader:
    def test_load_has_array(self):
        array = CSVStepsArrayLoader.load(FILE_CONTAINING_ARRAY_LOCATION)
        assert isinstance(array, list) and len(array) > 0

    def test_load_has_no_array_content(self):
        with pytest.raises(OSError):
            array = CSVStepsArrayLoader.load(FILE_NOT_CONTAINING_ARRAY_LOCATION)
            print(array)

    def test_load_empty_file(self):
        with pytest.raises(pandas.errors.EmptyDataError):
            array = CSVStepsArrayLoader.load(EMPTY_FILE)
