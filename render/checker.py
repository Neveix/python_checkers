from enum import Enum

class CheckerType(Enum):
    WHITE = 0
    WHITE_QUEEN = 1
    BLACK = 2
    BLACK_QUEEN = 3
    def is_queen(self):
        return (self == CheckerType.WHITE_QUEEN) or (self == CheckerType.BLACK_QUEEN)
    def get_color_normal(self):
        if self == CheckerType.WHITE_QUEEN or self == CheckerType.WHITE:
            return (190,) * 3
        else:
            return (45,) * 3
    def get_color_border(self):
        if self == CheckerType.WHITE_QUEEN or self == CheckerType.WHITE:
            return (220,) * 3
        else:
            return (30,) * 3