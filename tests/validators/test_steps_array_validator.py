import pytest

from validators.steps_array_validator import StepsArrayValidator

VALID_ARRAY = [1, 2, 3, 4]
INVALID_ARRAY = [1, 2, 'f']

class TestStepsArrayValidator:
    def test_validate_valid(self):
        try:
            StepsArrayValidator.validate(VALID_ARRAY)
        except:
            pytest.fail('Invalid file content.')

    def test_validate_invalid(self):
        with pytest.raises(TypeError):
            StepsArrayValidator.validate(INVALID_ARRAY)