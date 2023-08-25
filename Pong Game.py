import pygame

pygame.init()

#INITIALS
WIDTH, HIGHT = 1280,720
wn = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("Pong Game By Hasiru")

running = True
#Colors
WHITE = 255,255,255
RED = 255,0,0
#Ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HIGHT/2 -radius
ball_speed_x, ball_speed_y = 0.5, 0.5

#Paddles
right_paddle_width, right_paddle_hight = 20,140
left_paddle_width, left_paddle_hight = 20,140
left_paddle_y = HIGHT/2 - left_paddle_hight/2
right_paddle_y = HIGHT/2 - right_paddle_hight/2
left_paddle_x,right_paddle_x = 100 - right_paddle_width/2, WIDTH -(100 - right_paddle_width/2)


#movement animation
right_paddle_y_move = 0
left_paddle_y_move = 0
paddle_speed = 0.6

#player count tool
right_paddle_count = 0
left_paddle_count = 0
right_score = 0
left_score = 0
right_score_x, right_score_y = right_paddle_x + 20, right_paddle_y + right_paddle_width/2
left_score_x, left_score_y = left_paddle_x - 40, left_paddle_y + left_paddle_width/2

#font
myfont = pygame.font.SysFont("monospace", 27)

# MAIN
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Player movements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                right_paddle_y_move = -paddle_speed
            elif event.key == pygame.K_DOWN:
                right_paddle_y_move = paddle_speed
            elif event.key == pygame.K_w:
                left_paddle_y_move = -paddle_speed
            elif event.key == pygame.K_s:
                left_paddle_y_move = paddle_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                right_paddle_y_move = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                left_paddle_y_move = 0
    
    # Update paddle positions based on movement
    right_paddle_y += right_paddle_y_move
    left_paddle_y += left_paddle_y_move


    #movement

    #ball coming back loop
    if ball_y <= 0 or ball_y >= HIGHT - 2 * radius:
        ball_speed_y *= -1
    
    if ball_x <=0 or ball_x >= WIDTH:
        ball_x = WIDTH/2 - radius
        ball_y = HIGHT/2 - radius



    #right side paddle when ball hits 
    if right_paddle_y < ball_y < right_paddle_y + right_paddle_hight :
        if ball_x != right_paddle_x:
            ball_speed_x *= 1
        elif ball_x >= right_paddle_x:
            ball_speed_x *= -1
            right_paddle_count += 1
            right_score += 1

    #left side paddle when ball hits
    if left_paddle_y < ball_y < left_paddle_y + left_paddle_hight :
        if ball_x != left_paddle_x + 25:
            ball_speed_x *= 1
        elif ball_x >= left_paddle_x:
            ball_speed_x *= -1
            left_paddle_count += 1
            left_score += 1

    #Calculate the count tool
    if ball_x > right_paddle_x:
        right_paddle_count = 0
        right_score = 0
    
    if ball_x < left_paddle_x:
        left_paddle_count = 0
        left_score = 0


    if right_paddle_count == 3:
        right_paddle_hight = 170
    elif right_paddle_count < 3:
        right_paddle_hight = 140
    
    if left_paddle_count == 3:
        left_paddle_hight = 170
    elif left_paddle_count < 3:
        left_paddle_hight = 140

    #ball movement
    if ball_y + radius != HIGHT:
        ball_x += ball_speed_x
        ball_y += ball_speed_y

    #stop paddles to go over the window
    if left_paddle_y <= 0 or left_paddle_y + left_paddle_hight >= HIGHT:
        left_paddle_y_move = 0
    if right_paddle_y <= 0 or right_paddle_y + right_paddle_hight >= HIGHT:
        right_paddle_y_move = 0
    wn.fill((0,0,0))



    pygame.draw.circle(wn, WHITE, (ball_x,ball_y), radius)
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x,left_paddle_y, left_paddle_width, left_paddle_hight))
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x,right_paddle_y, right_paddle_width, right_paddle_hight))
    #update the score
    right_scoretext = myfont.render("  {0}".format(right_score),1 ,(WHITE))
    wn.blit(right_scoretext, (right_score_x, right_score_y))
    left_scoretext = myfont.render("{0}".format(left_score),1 ,(WHITE))
    wn.blit(left_scoretext, (left_score_x, left_score_y))
    pygame.display.update()

