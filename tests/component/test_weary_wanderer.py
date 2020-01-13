from globals import PROJECT_ROOT
from main import path_finder_service

WEARY_WANDERER_ARRAY_FILE='{project_root}/input_files/file1.csv'.format(project_root=PROJECT_ROOT)

class TestWearyWanderer(object):
    def test_find(self):
        actual_result = path_finder_service.find(WEARY_WANDERER_ARRAY_FILE)
        assert actual_result