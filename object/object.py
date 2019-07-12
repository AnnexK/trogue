from object.position import Position

class Object:
    def __init__(self, ch, pos):
        self.char = ch
        self._pos = Position(*pos)

    @property
    def pos(self):
        return self.pos.lvl, self.pos.y, self.pos.x