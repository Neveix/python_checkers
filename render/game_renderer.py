import pygame

class GameRenderer:
    def __init__(self):
        pygame.init()
        self.init_screen()
        self.init_board()
        self.mouse_pos = (0,0)
        self.pressed_keys = [False]*256
        self.pressed_mouse_keys = [False]*10
        self.running = False
        self.BG_FILL_COLOR = (10,) * 3
        self.WHITE_CELL_COLOR = (140,) * 3
        self.BLACK_CELL_COLOR = (20,) * 3
    
    def init_screen(self, window_size: tuple[int, int] = (1920, 1080)):
        self.window_size = window_size
        self.window_half_width = window_size[0] / 2
        self.whw = self.window_half_width
        self.window_half_height = window_size[1] / 2
        self.whh = self.window_half_height
        self.screen = pygame.display.set_mode(
            window_size, pygame.WINDOWFOCUSGAINED)
        pygame.display.init()
    
    def init_board(self, size: int = None):
        "Default `size` is `window_size` height."
        if size is None:
            size = self.window_size[1]
        self.board_size = size
        self.cell_size = size / 8
    
    def render_board(self):
        for y in range(8):
            for x in range(8):
                if (x + y) % 2 == 0:
                    color = self.WHITE_CELL_COLOR
                else:
                    color = self.BLACK_CELL_COLOR
                rect = (self.whw+(-4 + x)*self.cell_size, self.whh+(-4 + y)*self.cell_size, 
                    self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, color, rect, width=0)
    
    def render_checkers(self):
        pass
    
    def handle_event(self, event: pygame.Event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.MOUSEMOTION:
            self.mouse_pos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.pressed_mouse_keys[event.button] = True
        if event.type == pygame.MOUSEBUTTONUP:
            self.pressed_mouse_keys[event.button] = False
        if event.type == pygame.KEYDOWN:
            if event.key > 0 and event.key < 256:
                self.pressed_keys[event.key] = True
            if event.key == pygame.K_F9:
                self.running = False
        if event.type == pygame.KEYUP:
            if event.key > 0 and event.key < 256:
                self.pressed_keys[event.key] = False
    
    def start_game_loop(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.screen.fill(self.BG_FILL_COLOR)
            self.render_board()
            self.render_checkers()
            pygame.display.update()
    
    #def __del__(self):
        # self.screen.fill((0,0,0))
        # pygame.display.update()
        #exit()

