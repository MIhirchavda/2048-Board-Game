import pygame
import numpy as np
from constant import CP, TEST_GRID

W = 400
H = W
SPACING = 10

def draw_game(screen, grid, myfont):
    screen.fill(CP['back'])
    for i in range(4):
        for j in range(4):
            n = grid[i][j]

            rect_x = j * W // 4 + SPACING
            rect_y = i * H // 4 + SPACING
            rect_w = W // 4 - 2*SPACING
            rect_h = H // 4 -2*SPACING
            pygame.draw.rect(screen, CP[n], pygame.Rect(rect_x, rect_y, rect_w, rect_h ), border_radius= 8)

            text_surface = myfont.render(f'{n}', True, (0, 0, 0))
            text_rect = text_surface.get_rect(center = (rect_x + rect_w/2, rect_y + rect_h/2))
            screen.blit(text_surface, text_rect)


from pygame.locals import *
def wait_for_key():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return 'q'
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    return 'u'
                elif event.key == K_RIGHT:
                    return 'r'
                elif event.key == K_LEFT:
                    return 'l'
                elif event.key == K_DOWN:
                    return 'd'
                elif event.key == K_q or event.key == K_ESCAPE:
                    return 'q'




def main():
    pygame.init()
    pygame.display.set_caption("2048")
    screen = pygame.display.set_mode((W, H))
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    running = True
    while running:
        np.random.shuffle(TEST_GRID)
        draw_game(screen, TEST_GRID,myfont)
        pygame.display.flip()
        key = wait_for_key()
        if key == 'q':
            running = False


if __name__ == "__main__":
    main()