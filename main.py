import pygame
import os

pygame.font.init()
pygame.mixer.init()

# screen size and name
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gunlaxy")


# font
HEALTH_FONT = pygame.font.SysFont("Comic Sans MS", 30)
WINNER_FONT = pygame.font.SysFont("Comic Sans MS", 50)

# color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# velocity, fps,... all of game experiment
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)
FPS = 60
VEL = 5
BULLET_VEL = 10
MAX_BULLETS = 5
MAX_HEALTH = 10

# spaceship size
SPACESHIP_WIDTH = 70
SPACESHIP_HEIGHT = 60

# sprite of spaceship
YELLOW_SPACESHIP = pygame.image.load(os.path.join("assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
RED_SPACESHIP = pygame.image.load(os.path.join("assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
SPACE = pygame.transform.scale(pygame.image.load(os.path.join("assets", "space.png")), (WIDTH, HEIGHT))

# event
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# sound
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("assets", "hit.wav"))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join("assets", "gunfire.wav"))

def draw_winner(winner_text):
    draw_text = WINNER_FONT.render(winner_text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)
    
    
def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
        
    pygame.display.update()
    
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # move left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: # move right
        yellow.x += VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: # move down
        yellow.y += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # move up
        yellow.y -= VEL
        
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width + 10: # move left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH + 10:  # move right
        red.x += VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15: # move down
        red.y += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: # move up
        red.y -= VEL
        
def handle_bullet(red_bullets, yellow_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
            
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def main():
    
    # rectangle of spaceship
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    # array of bullet
    red_bullets = []
    yellow_bullets = []
    
    # health
    red_health = MAX_HEALTH
    yellow_health = MAX_HEALTH
    
    clock = pygame.time.Clock()
    run = True
    
    # game loop
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            
            # quit game
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            # keydown
            if event.type == pygame.KEYDOWN:
                # fire
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            # health changed
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
                
        # winner appears
        winner_text = ""
        if red_health <= 0:
            winner_text = "Red Wins!"
        if yellow_health <= 0:
            winner_text = "Yellow Wins!"
        if winner_text != "":
            draw_winner(winner_text)
            break        
        
        # print(yellow_bullets, red_bullets)
        
        # movement of spaceship
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        
        # bullet fired
        handle_bullet(red_bullets, yellow_bullets, yellow, red)
        
        # draw window
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
        
    # return main() when the game is over
    main()
    
if __name__ == "__main__":
    main()

