from resolvers.file_steps_array_loader_resolver import FileStepsArrayLoaderResolver
from resolvers.file_type_resolver import FileTypeResolver
from services.business_logic.path_finder_algorithm import PathFinderAlgorithm
from services.path_finder_service import PathFinderService
from validators.file_validator import FileValidator
from validators.steps_array_validator import StepsArrayValidator

if __name__ == '__main__':
    path_finder = PathFinderService(FileValidator,
                                    StepsArrayValidator,
                                    FileTypeResolver,
                                    FileStepsArrayLoaderResolver(),
                                    PathFinderAlgorithm)

    user_input = input("Please enter full file path to CVS, TSV or Json files: ")

    if path_finder.find(user_input):
        exit(0)
    else:
        exit(1)