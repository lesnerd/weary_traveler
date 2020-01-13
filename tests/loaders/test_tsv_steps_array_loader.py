import pandas
import pytest

from loaders.tsv_steps_array_loader import TSVStepsArrayLoader

FILE_CONTAINING_ARRAY_LOCATION = "../files/ok.tsv"
FILE_NOT_CONTAINING_ARRAY_LOCATION = "../files/not_ok.tsv"
EMPTY_FILE = "../files/empty_tsv.tsv"

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


