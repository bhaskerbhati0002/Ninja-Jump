import pygame
import random
pygame.init()
screen_width = 690
screen_height = 390
gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ninja jump")
cyan = (0,255,255)
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)

font = pygame.font.SysFont(None, 45)

def text_screen(text, color,x,y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])

#images
background=pygame.image.load('gallery/sprites/ninja jump/nature.jpg')
base=pygame.image.load('gallery/sprites/ninja jump/base.jpg')
player=pygame.image.load('gallery/sprites/ninja jump/player.png')
hurdle1=pygame.image.load('gallery/sprites/ninja jump/hurdle1.png')
hurdle2=pygame.image.load('gallery/sprites/ninja jump/hurdle2.png')
warning=pygame.image.load('gallery/sprites/ninja jump/laser warning.PNG')

#sounds
move = pygame.mixer.Sound('gallery/audio/swoosh.wav')
hit = pygame.mixer.Sound('gallery/audio/hit.wav')
win = pygame.mixer.Sound('gallery/audio/point.wav')
laser = pygame.mixer.Sound('gallery/audio/laserdie.wav')
fire = pygame.mixer.Sound('gallery/audio/firedie.wav')
exit_game = False

#game variables
score = 0
player_x = 50
player_y = 180
velocity_player = 0.2
velocity_hurdle = 0.5
hurdle = [hurdle1, hurdle2]

def gameover():
    score = 0
    while exit_game!=True:
        for event in pygame.event.get():
            gamewindow.fill(white)
            text_screen("Hit 'ENTER' to play again.", red,150, 150)
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_RETURN:
                    play(exit_game, player_y,score)
        pygame.display.update()

def play(exit_game, player_y, score):
    hurdle_x = 650
    hurdle_y = 230
    a=random.randint(0,1)
    while exit_game != True:
        gamewindow.blit(background, [-5, -5])
        pygame.draw.rect(gamewindow, red, [0,10,690,5])
        gamewindow.blit(warning, [495, 15])
        gamewindow.blit(base, [-5, 310])
        text_screen("Score :" + str(score), cyan, 270, 350)
        gamewindow.blit(player, [player_x, player_y])
        gamewindow.blit(hurdle[a], [hurdle_x, 230])
        hurdle_x = hurdle_x - velocity_hurdle
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    move.play()
                    player_y = player_y - 80
                    if player_y<5:
                        laser.play()
                        gameover()

        if (50 < hurdle_x < 114 and player_y < 148):
            score = score +10
            win.play()
            play(exit_game,player_y,score)

        if (50 < hurdle_x < 115 and 148 < player_y < 231):
            if a==0:
                hit.play()
                gameover()
            if a==1:
                fire.play()
                gameover()

        if (player_y < 230):
            player_y = player_y + velocity_player
            pygame.display.update()
        pygame.display.update()


while exit_game!=True:

    gamewindow.blit(background, [-5, -5])
    gamewindow.blit(base, [-5, 310])
    gamewindow.blit(player, [50, player_y])
    text_screen('press "SPACE" to play', red, 170, 40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            move.play()
            play(exit_game, player_y, score)

    pygame.display.update()



