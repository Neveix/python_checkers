from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from render.game_renderer import GameRenderer

class GameState:
    WHITE_SELECT_CHECKER = 0
    WHITE_SELECT_POS = 1
    BLACK_SELECT_CHECKER = 2
    BLACK_SELECT_POS = 3

class LogicWrapper:
    def __init__(self, game_renderer: "GameRenderer"):
        self._white_turn = True
        self.game_renderer = game_renderer
        self.game_state = GameState.WHITE_SELECT_CHECKER
    
    def cell_click(self, pos: tuple[int,int]) -> None:
        self.game_renderer.clear_checker_path()
        bx,by = pos
        checker = self.game_renderer.get_checker((bx,by))
        if checker == None:
            return
        poses = [(bx-1,by-1),(bx-1,by+1),(bx+1,by-1),(bx+1,by+1)]
        for pos in poses:
            if not self.game_renderer.is_on_board(pos):
                continue
            self.game_renderer.add_checker_path(pos)
    
    def is_white_turn(self) -> bool:
        self._white_turn = False
        
    def get_required_moves(self) -> list[tuple[int,int]]:
        return []
    
    def get_checker_moves(self, pos: tuple[int,int]) -> list[tuple[int,int]]:
        bx,by = pos
        poses = [(bx-1,by-1),(bx-1,by+1),(bx+1,by-1),(bx+1,by+1)]
        accepted = []
        for pos in poses:
            if self.is_on_board(pos):
                accepted.append(pos)
        return accepted
    