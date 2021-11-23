class PixelArray:
    def __init__(self, n):
        self.n = n
        self.bytearr = bytearray(n * 3)

    def fill(self, value):
        self[:] = value

    def __setitem__(self, key, value):
        if isinstance(key, int):
            key = slice(key, key + 1)

        if isinstance(key, slice):
            start = 0 if key.start is None else key.start
            stop = self.n if key.stop is None else key.stop
            step = 1 if key.step is None else key.step

            key = tuple(range(start, stop, step))

        if not isinstance(key, tuple):
            raise Exception('Key must be an int/tuple/slice')

        for i in key:
            idx = i * 3
            self.bytearr[idx:idx + 3] = value

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise Exception('Key must be an int')

        idx = key * 3
        return tuple(self.bytearr[idx:idx + 3])
