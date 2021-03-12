class Search(object):
    def isValidPattern(self, pattern):
        if not pattern.isalnum():
            return False

        if " " in pattern:
            return False

        return True

class InvalidPattern(Exception):
    pass