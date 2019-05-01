import random, sys, time, math, pygame
from physics import *
from pygame.locals import *

global fps, display_width, display_length, screen_one, screen_two,screen_three,screen_four
#initiation and vars
pygame.init()
fps = 60
display_width = 1500
display_length = 1071
screen_one = False #game
screen_two = False #level
screen_three = False #setting
screen_four = True #menu
screen_five = False #opening screen
#colors:
Aqua = (0,255,255)
Black = (0,0,0)
Blue = (0,0,255)
Fuchsia = (255,0,255)
Gray = (128,128,128)
Green = (0,128,0)
Lime = (0,255,0)
Maroon = (128,0,0)
Navy_Blue = (0,0,128)
Olive = (128,128,0)
Purple = (128,0,128)
Red = (255,0,0)
Silver = (192,192,192)
Teal = (0,128,128)
White = (255,255,255)
Yellow = (255,255,0)
#create display and name of it and a clock
gameDisplay = pygame.display.set_mode((display_width,display_length))
pygame.display.set_caption('Graphic Test')
fpsClock = pygame.time.Clock()
pygame.font.init() 
levelFont = pygame.font.SysFont('Comic Sans MS', 60)
textsurface = levelFont.render('1', False, Black)
#loads all the images for the screens in
setting_screen = pygame.image.load('Settings.jpg')
level_screen = pygame.image.load('map.jpg')
menu_screen = pygame.image.load('Home_screen.jpg')
setting_button = pygame.image.load('setting_buttonIMG.jpg')
map_button = pygame.image.load('map_buttonIMG.jpg')
#game_screen = pygame.image.load('')#not created yet
#opening_screen = pygame.image.load('') #not created yet

#methods to display the screens

def level_Screen():
    gameDisplay.blit(level_screen, (0,0))
def menu_Screen():
    gameDisplay.blit(menu_screen, (0,0))
def setting_Screen():
    gameDisplay.blit(setting_screen, (0,0))
def game_Screen():
    gameDisplay.blit(game_screen, (0,0))
def opening_Screen():
    gameDisplay.blit(opening_screen, (0,0))
#method for opening screen clicks
def onClickScreen():
    for event in pygame.event.get():
        if event.type:
            screen_five = False
            screen_four = True
            
#method to run the game
def run_Game():
    #position var for the object
    x = (display_width*0.02)
    y = (display_length*0.65)

    x_change = 0
    y_change = 0
    someObj = thing([0,0], 1)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_Exit = True
            #movement control
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not(x < 0 + characterIMG_width/2):
                    x_change = -5
                elif event.key == pygame.K_RIGHT and not(x> display_width - characterIMG_width):
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not(y < 0):
                    y_change = -5
                elif event.key == pygame.K_DOWN and not(y> (display_length - characterIMG_length)):
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
            x += x_change
            y += y_change
            someObj.thrust(x,y)
#button methods
'''def menu_Buttons():
    x_pos =
    y_pos =
    obj_len =
    obj_width =
    currentScreen = 'menu'
    settingScreen = 'settings'
    mapScreen = 'map'
    button(x_pos, y_pos, obj_len, obj_width, currentScreen, )
    
def map_Buttons():
    x_pos =
    y_pos =
    obj_len =
    obj_width =
    currentScreen = 'map'
    settingScreen = 'settings'
    gameScreen = 'game'
    menuScreen = 'menu'
    button(x_pos, y_pos, obj_len, obj_width, currentScreen, )
 
def setting_Buttons():
    x_pos =
    y_pos =
    obj_len =
    obj_width = 
    currentScreen = 'settings'
    menuScreen = 'menu'
    button(x_pos, y_pos, obj_len, obj_width, currentScreen, )
    '''
#generates the button
def button(self,x,y,length,width,img1,action=None):
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if length>=mouse[0]>=x and width>=mouse[1]>y:
            self.screen.blit(img1,(x,y))
            '''
            if click[0]==1 and action!=None:
                if action=="play":
                    root=tk.Tk()
                    g=Gui(root)
                    root.mainloop()
                    
                elif action=="quit":
                    pygame.quit()
                    quit()
                elif action=="spawn":
                    
                    self.game(x,y)
                elif action=='sort':
                    self.bubble(self.sort_list,self.sort_type,self.sort_order)
                    '''
                
        else:
            pass

        

def game_loop():
    #global fps, display_width, display_length, screen_one, screen_two,screen_three,screen_four



    game_Exit = False
    #game update thing
    while not game_Exit:
        

        '''if event.type == QUIT:
            pygame.quit() 
'''
        #print('test')
        #mouse = pygame.mouse.get_pos()
        if(screen_one):
            game_Screen()
            run_Game()
        elif(screen_two):
            level_Screen()
            map_Buttons()
        elif(screen_three):
            setting_Screen()
            setting_Buttons()
        elif(screen_four):
            menu_Screen()
            
            button(0,489,300,1071,level_screen,'idk')
        elif(screen_five):
            opening_Screen()
            onClickScreen()
            
        else:
            pass
            
        #if x> display_width - characterIMG_width or x < 0:
            #out_of_bounds()
        #if y> display_length - characterIMG_length or x < 0:
            #out_of_bounds()
        #print (event)
        #mouse = pygame.mouse.get_pos()
        #print(mouse)
        #if 164+76+76 > mouse[0] >164 and 247+76+76 > mouse [1] > 247:
            #pygame.draw.circle(gameDisplay, green, (164,247), 76)
        #else:
            #pygame.draw.circle(gameDisplay, yellow, (164,247), 76)
        pygame.display.update()
        
        fpsClock.tick(fps)





game_loop() 
pygame.quit()
quit()
