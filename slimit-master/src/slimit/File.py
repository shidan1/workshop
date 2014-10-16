def OpenFile(path):
    try:
        with open(path) as inputFileHandle:
            return inputFileHandle.read()

    except IOError:
        return None

