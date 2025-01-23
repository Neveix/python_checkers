
from render.game_renderer import GameRenderer
from render.checker import CheckerType

game_renderer = GameRenderer()

game_renderer.set_checker((0,0), CheckerType.BLACK_QUEEN)
game_renderer.set_checker((2,3), CheckerType.WHITE)
game_renderer.set_checker((1,4), CheckerType.BLACK)
game_renderer.set_checker((5,7), CheckerType.WHITE)
game_renderer.set_checker((6,1), CheckerType.WHITE_QUEEN)

assert CheckerType.WHITE.is_queen() == False
assert CheckerType.WHITE_QUEEN.is_queen() == True
assert CheckerType.BLACK.is_queen() == False
assert CheckerType.BLACK_QUEEN.is_queen() == True

game_renderer.start_game_loop()