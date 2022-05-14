import pygame

pygame.init()

Screen_width = 480  #가로 크기
screen_height = 640  #세로 크기
screen = pygame.display.set_mode((Screen_width, screen_height))

pygame.display.set_caption( "nado game" ) # 게임 이름


#이벤트 루프
running = True
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running = False



#pygame 종료
pygame.quit()