class StepsArrayValidator(object):
    @staticmethod
    def validate(steps_array):
        for number in steps_array:
            if not isinstance(number, int):
                raise TypeError('The given array supports integer values only.')