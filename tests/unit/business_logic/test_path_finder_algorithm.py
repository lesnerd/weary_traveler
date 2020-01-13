from services.business_logic.path_finder_algorithm import PathFinderAlgorithm


class TestPathFinderAlgorithm:
    def test_find_given_input_return_true(self):
        arr = [4, 4, 1, 1, 2, 2, 1000, 1]
        if not PathFinderAlgorithm.find(arr):
            assert False
        assert True

    def test_find_one_item_return_true(self):
        arr = [0]
        if not PathFinderAlgorithm.find(arr):
            assert False
        assert True

    def test_find_straight_to_end_return_true(self):
        arr = [3, 2, 0, 1]
        if not PathFinderAlgorithm.find(arr):
            assert False
        assert True

    def test_find_can_stuck_if_go_in_wrong_direction_return_true(self):
        arr = [1, 2, 4, 1, 5, 100, 1, 100, 1, 1, 1, 1]
        if not PathFinderAlgorithm.find(arr):
            assert False
        assert True

    def test_find_given_input_return_false(self):
        arr = [4, 2, 1, 3, 2, 2, 1000, 1]
        if PathFinderAlgorithm.find(arr):
            assert False
        assert True

    def test_find_with_zeros_return_false(self):
        arr = [2, 0, 0, 1, 0]
        if PathFinderAlgorithm.find(arr):
            assert False
        assert True

    def test_find_long_input_return_false(self):
        arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
        if PathFinderAlgorithm.find(arr):
            assert False
        assert True
