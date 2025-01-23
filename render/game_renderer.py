import pygame

class GameRenderer:
    def __init__(self):
        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode(
            (1920, 1020), pygame.WINDOWFOCUSGAINED)
        self.mouse_pos = (0,0)
        self.pressed_keys = [False]*256
        self.pressed_mouse_keys = [False]*10
        self.running = False
        self.BG_FILL_COLOR = (65,65,65)
    
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
            pygame.display.update()
    
    #def __del__(self):
        # self.screen.fill((0,0,0))
        # pygame.display.update()
        #exit()

