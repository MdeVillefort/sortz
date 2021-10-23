import pygame
from random import randint
from sorters import bubble_sort

class Visualizer:
    def __init__(self, sorter, fps):
        self._init_pygame()
        self.sorter = sorter
        self.fps = fps
        self.screen = pygame.display.set_mode((800, 600))
        self.black = 0, 0, 0
        self.white = 255, 255, 255
        self.clock = pygame.time.Clock()
        self.is_sorted = False
        self.paused = False

        # Create list of bars as (Surface, Rect) tuples
        self.bars = []
        for _ in range(100):
            surf = pygame.Surface((8, randint(10, 600)))
            rect = surf.get_rect()
            self.bars.append((surf, rect))
        
        # Color screen and rectangles
        self.screen.fill(self.black)
        for surf, _ in self.bars:
            surf.fill(self.white)

        # Set initial position of bars on screen
        self.xcoords = []
        screen_height = self.screen.get_rect().height
        for i, (surf, rect) in enumerate(self.bars):
            rect.bottom = screen_height
            rect.left = 8 * i
            self.xcoords.append(8 * i)

    def main_loop(self):
        while True:
            self._handle_input()
            self._sort()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Sorting Visualizer")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.paused = not self.paused
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.fps = self.fps + 1 if self.fps < 60 else 60
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.fps = self.fps - 1 if self.fps > 1 else 1

    def _sort(self):
        # Sort and update position if needed
        if not self.is_sorted:
            self.is_sorted = self.sorter(self.bars, once = True)

            for (_, rect), xcoord in zip(self.bars, self.xcoords):
                rect.left = xcoord

    def _draw(self):
        self.screen.fill(self.black)
        for surf, rect in self.bars:
            self.screen.blit(surf, rect)

        # Maintain framerate
        self.clock.tick(self.fps)

        pygame.display.flip()
