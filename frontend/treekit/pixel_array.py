class PixelArray:
    def __init__(self, n):
        self.n = n
        self.bytearr = bytearray(n * 3)

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise Exception('Key must be an int')

        idx = key * 3
        self.bytearr[idx:idx + 3] = value

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise Exception('Key must be an int')

        idx = key * 3
        return tuple(self.bytearr[idx:idx + 3])
