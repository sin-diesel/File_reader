
class FileReader:

    def __init__(self, path_to_file):

        self._path_to_file = None

        if isinstance(path_to_file, str):
            self._path_to_file = path_to_file
        else:
            print("File path provided is not a string")

    def print_path(self):

        if (self._path_to_file is not None):
            print(self._path_to_file)
        else:
            print("Path not defined")