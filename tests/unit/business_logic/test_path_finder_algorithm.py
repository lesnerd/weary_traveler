from services.business_logic.path_finder_algorithm import PathFinderAlgorithm

true_array = [[4, 4, 1, 1, 2, 2, 1000, 1],
                   [1, 2, 4, 1, 5, 100, 1, 100, 1, 1, 1, 1],
                   [3, 2, 0, 1],
                   [2, 0, 1, 1, 0],
                   [1],
                   [0]]

false_array = [[4, 2, 1, 3, 2, 2, 1000, 1],
                    [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9],
                    [2, 2, 0, 1],
                    [2, 0, 0, 1, 0]]

class TestPathFinderAlgorithm:
    def test_find_with_result_true(self):
        for arr in true_array:
            if not PathFinderAlgorithm.find(arr):
                assert False
        assert True

    def test_find_with_result_false(self):
        for arr in false_array:
            if PathFinderAlgorithm.find(arr):
                assert False
        assert True
