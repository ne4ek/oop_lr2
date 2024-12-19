import sys, pygame, random, math

pygame.init()
pygame.display.set_caption("ООП ЛР №2")
pygame.font.init()
random.seed()

SPEED = 0.36
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE
SEPARATION = 10
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 25
KEY = {"UP": 1, "DOWN": 2, "LEFT": 3, "RIGHT": 4}
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.HWSURFACE)

score_font = pygame.font.Font(None, 38)
score_numb_font = pygame.font.Font(None, 28)
game_over_font = pygame.font.Font(None, 46)
play_again_font = score_numb_font
score_msg = score_font.render("Score:", 1, pygame.Color("green"))
score_msg_size = score_font.size("Score")

background_color = pygame.Color(74, 74, 74)
black = pygame.Color(0, 0, 0)

gameClock = pygame.time.Clock()


def checkCollision(posA, As, posB, Bs):
    if (
        posA.x < posB.x + Bs
        and posA.x + As > posB.x
        and posA.y < posB.y + Bs
        and posA.y + As > posB.y
    ):
        return True
    return False


def checkLimits(entity):
    if entity.x > SCREEN_WIDTH:
        entity.x = SNAKE_SIZE
    if entity.x < 0:
        entity.x = SCREEN_WIDTH - SNAKE_SIZE
    if entity.y > SCREEN_HEIGHT:
        entity.y = SNAKE_SIZE
    if entity.y < 0:
        entity.y = SCREEN_HEIGHT - SNAKE_SIZE