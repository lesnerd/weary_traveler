class PathFinderAlgorithm(object):

    @staticmethod
    def find(steps_array):
        if steps_array is None:
            return False
        arrayLength = len(steps_array)
        if arrayLength == 0 or arrayLength == 1 or steps_array[0] == arrayLength:
            return True
        visited_indexs = [None] * arrayLength
        stack = []
        stack.append(steps_array[0])
        visited_indexs[0] = True
        while len(stack) > 0:
            currentIndex = stack.pop()
            step_beckwards = currentIndex - steps_array[currentIndex]
            step_forward = currentIndex + steps_array[currentIndex]
            if step_forward == arrayLength - 1 or currentIndex == arrayLength - 1:
                return True
            if step_beckwards >= 0 and visited_indexs[step_beckwards] is None:
                stack.append(step_beckwards)
                visited_indexs[step_beckwards] = True
            if step_forward < arrayLength and visited_indexs[step_forward] is None:
                stack.append(step_forward)
                visited_indexs[step_forward] = True

        return False