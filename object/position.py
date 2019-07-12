class Position:
    def __init__(self, L, y, x):
        self.set_pos(L, y, x)

    def set_pos(self, L=None, y=None, x=None):
        if (L is not None and L < 0) or (y is not None and y < 0) or (x is not None and x < 0):
            raise ValueError('Incorrect coordinates')
        self._level = L if L is not None else self._level
        self._y = y if y is not None else self._y
        self._x = x if x is not None else self._x

    @property
    def lvl(self):
        return self._level

    @property
    def y(self):
        return self._y

    @property
    def x(self):
        return self._x

    