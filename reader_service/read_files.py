import os

class ReadFiles(object):
    def __init__(self, dirPath):
        self.dirPath = dirPath

    def readAllFilesInDir(self):
        filesDataMap = {}
        for filename in os.listdir(self.dirPath):
            if filename.endswith(".txt"):
                file_directory = os.path.join(self.dirPath, filename)
                f = open(file_directory, "r")
                filesDataMap[filename] = f.read()
                f.close()

        return filesDataMap