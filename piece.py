row_to_file = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}


class Piece():
    name = None
    is_white = None
    rank = None
    file = None

    def __repr__(self):
        color = "White" if self.is_white else "Black"
        if self.rank and self.file:
            return f'Piece(\'{self.name}\', {color}, {row_to_file[self.file]}{self.rank+1})'
        else:
            return f'Piece(\'{self.name}\', {color})'

    def __init__(self, name, is_white, rank=None, file=None):
        self.name = name
        self.is_white = is_white
        self.rank = rank
        self.file = file
