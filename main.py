import pygame
import os
import sys

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
FPS = 60
VEL = 5
BULLET_VEL = 10
MAX_BULLETS = 5
MAX_HEALTH = 10

# spaceship size
SPACESHIP_WIDTH = 60
SPACESHIP_HEIGHT = 50

# red bullet size
BULLET_WIDTH = 20
BULLET_HEIGHT = 60

# sprite
BULLET_SPR = [pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bullet", "bullet1.png")), (BULLET_WIDTH, BULLET_HEIGHT)), 90),
              pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bullet", "bullet2.png")), (BULLET_WIDTH, BULLET_HEIGHT)), 90),
              pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bullet", "bullet3.png")), (BULLET_WIDTH, BULLET_HEIGHT)), 90)]
BIGBULLET_SPR = [pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bigbullet", "bigbullet1.png")), (BULLET_WIDTH, BULLET_HEIGHT)), 270),
                 pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bigbullet", "bigbullet2.png")), (BULLET_WIDTH, BULLET_HEIGHT)), 270),
                 pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bigbullet", "bigbullet3.png")), (BULLET_WIDTH, BULLET_HEIGHT)), 270),
                 pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bigbullet", "bigbullet4.png")), (BULLET_WIDTH, BULLET_HEIGHT)), 270)]
BG_SPR = [pygame.transform.scale(pygame.image.load(os.path.join("assets", "background", "bg1.png")), (WIDTH, HEIGHT)),
          pygame.transform.scale(pygame.image.load(os.path.join("assets", "background", "bg2.png")), (WIDTH, HEIGHT)),
          pygame.transform.scale(pygame.image.load(os.path.join("assets", "background", "bg3.png")), (WIDTH, HEIGHT)),
          pygame.transform.scale(pygame.image.load(os.path.join("assets", "background", "bg4.png")), (WIDTH, HEIGHT)),
          pygame.transform.scale(pygame.image.load(os.path.join("assets", "background", "bg5.png")), (WIDTH, HEIGHT)),
          pygame.transform.scale(pygame.image.load(os.path.join("assets", "background", "bg6.png")), (WIDTH, HEIGHT)),
          pygame.transform.scale(pygame.image.load(os.path.join("assets", "background", "bg7.png")), (WIDTH, HEIGHT)),
          pygame.transform.scale(pygame.image.load(os.path.join("assets", "background", "bg8.png")), (WIDTH, HEIGHT)),
          pygame.transform.scale(pygame.image.load(os.path.join("assets", "background", "bg9.png")), (WIDTH, HEIGHT))]
FIGHTER_SPR = [pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "fighter_engine", "fighter_engine1.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90),
               pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "fighter_engine", "fighter_engine2.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90),
               pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "fighter_engine", "fighter_engine3.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90),
               pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "fighter_engine", "fighter_engine4.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90),
               pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "fighter_engine", "fighter_engine5.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90),
               pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "fighter_engine", "fighter_engine6.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90),
               pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "fighter_engine", "fighter_engine7.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90),
               pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "fighter_engine", "fighter_engine8.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90),
               pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "fighter_engine", "fighter_engine9.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90),
               pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "fighter_engine", "fighter_engine10.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)]
BOMBER_SPR = [pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bomber", "bomber1.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270),
              pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bomber", "bomber2.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270),
              pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bomber", "bomber3.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270),
              pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bomber", "bomber4.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270),
              pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bomber", "bomber5.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270),
              pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bomber", "bomber6.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270),
              pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bomber", "bomber7.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270),
              pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bomber", "bomber8.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270),
              pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bomber", "bomber9.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270),
              pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bomber", "bomber10.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)]

# event
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# sound
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("assets", "audio", "hit.wav"))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join("assets", "audio", "gunfire.wav"))

def draw_winner(winner_text):
    draw_text = WINNER_FONT.render(winner_text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)
    
def draw_bullet(bullet, BULLET_SPR, value):
    if value[0] >= len(BULLET_SPR):
        value[0] = 0
    image = BULLET_SPR[value[0]]
   
    WIN.blit(image, (bullet.x - 7, bullet.y - 7))
    value[0] += 1
    
def draw_space(BG_SPR, value):
    if value[0] >= len(BG_SPR):
        value[0] = 0
    image = BG_SPR[value[0]]
   
    WIN.blit(image, (0, 0))
    value[0] += 1
    
def draw_spaceship(ss, FIGHTER_SPR, value):
    if value[0] >= len(FIGHTER_SPR):
        value[0] = 0
    image = FIGHTER_SPR[value[0]]
    
    WIN.blit(image, (ss.x, ss.y))
    value[0] += 1

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, value_bul, value_big, value_bg, value_fighter, value_bomber):
    
    # draw the window
    draw_space(BG_SPR, value_bg)
        
    # draw the spaceship
    draw_spaceship(yellow, BOMBER_SPR, value_bomber)
    draw_spaceship(red, FIGHTER_SPR, value_fighter)
    
    # draw text of health
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    
    # draw bullets
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
        draw_bullet(bullet, BULLET_SPR, value_bul)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, BLACK, bullet)
        draw_bullet(bullet, BIGBULLET_SPR, value_big)
        
    pygame.display.update()
    
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # move left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < WIDTH // 2 - 5: # move right
        yellow.x += VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: # move down
        yellow.y += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # move up
        yellow.y -= VEL
        
def red_handle_movement(keys_pressed, red, value):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > WIDTH // 2 - 5 + 10 + 10: # move left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH + 10:  # move right
        red.x += VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15: # move down
        red.y += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: # move up
        red.y -= VEL
    WIN.blit(FIGHTER_SPR[0], (0, 0))
    draw_spaceship(red, FIGHTER_SPR, value)
        
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
    
    value_bul = [0]
    value_big = [0]
    value_bg = [0]
    value_fighter = [0]
    value_bomber = [0]
    
    # game loop
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            
            # quit game
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
                
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
            winner_text = "Bomber Wins!"
        if yellow_health <= 0:
            winner_text = "Fighter Wins!"
        if winner_text != "":
            draw_winner(winner_text)
            # main()
            break
        
        # movement of spaceship
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red, value_fighter)
        
        # bullet fired
        handle_bullet(red_bullets, yellow_bullets, yellow, red)
        
        # draw window
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, value_bul, value_big, value_bg, value_fighter, value_bomber)
        
    # return main() when the game is over
    main()
    
if __name__ == "__main__":
    main()

