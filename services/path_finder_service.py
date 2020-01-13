class PathFinderService(object):
    def __init__(self,
                 file_validator,
                 steps_array_validator,
                 file_type_resolver,
                 file_steps_array_loader_resolver,
                 path_finder_algo):
        self.__file_validator = file_validator
        self.__steps_array_validator = steps_array_validator
        self.__file_type_reoslver = file_type_resolver
        self.__file_steps_array_loader_resolver = file_steps_array_loader_resolver
        self.__path_finder_algorithm = path_finder_algo

    def find(self, file_path):
        self.__file_validator.validate(file_path)

        file_type = self.__file_type_reoslver.resolve(file_path)

        loader = self.__file_steps_array_loader_resolver.resolve(file_type)
        steps_array = loader.load(file_path)

        self.__steps_array_validator.validate(steps_array)

        return self.__path_finder_algorithm.find(steps_array)