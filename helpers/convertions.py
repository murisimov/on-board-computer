
def a(string):
    return string.encode('ascii')


def s(string):
    if isinstance(string, (bytes, bytearray)):
        return string.decode('utf-8')
    else:
        return str(string)
