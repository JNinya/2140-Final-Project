class File:
    def __init__(self, file_name):
        file = open(file_name, "r", encoding="utf8")
        self.__data = file.read()
        file.close()

    def raw_data(self):
        return self.__data