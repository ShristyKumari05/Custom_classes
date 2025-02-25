class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._iter_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._iter_index == 0:
            self._iter_index += 1
            return {'length': self.length}
        elif self._iter_index == 1:
            self._iter_index += 1
            return {'width': self.width}
        else:
            raise StopIteration
        