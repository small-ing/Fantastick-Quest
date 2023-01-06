#Feel free to use parts of the code below in your final project!

#The code below is for generating map5 as seen in the Maps folder in the Final Project Scaffold. You can edit it to your own liking!

import pygame, sys, time
from pygame.locals import *
from player import Player

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.mixer.init()
pygame.font.init()


MAIN_MENU_FONT = pygame.font.Font('alagard.ttf', 64)
PLAY_FONT = pygame.font.Font('alagard.ttf', 56)


CHAR_FONT = pygame.font.Font('alagard.ttf', 24)


FOREST_SOUND = pygame.mixer.Sound("audio/forest_ambience.wav")
CAVE_SOUND = pygame.mixer.Sound("audio/cave_ambience.wav")
DUNGEON_SOUND = pygame.mixer.Sound("audio/dungeon_ambience.wav")
# sound_name.play(-1)
# sound_name.stop()

WINDOW_SIZE = (480, 360)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
#display = pygame.Surface((240, 180))  # used as the surface for rendering, which is scaled
#All maps are made for this screen resolution, if you want a different size screen, you need to edit the map file or make your own.
pygame.display.set_caption(' Fantastick Quest')

clock = pygame.time.Clock()
frame = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 500

tile_size = (16, 16)
spawn_list = [pygame.Rect(48, 144, 16, 16), pygame.Rect(122, 416, 16, 16), pygame.Rect(126, 176, 16, 16)]

'''dirt = pygame.image.load('dirt.png').convert_alpha()  # How the images are loaded in
dirt = pygame.transform.scale(dirt, tile_size)  #Changing image to 16x16

grass = pygame.image.load('grass.png').convert_alpha()  # How the images are loaded in
grass = pygame.transform.scale(grass, tile_size)  #Changing image to 16x16'''

arrow = pygame.image.load('arrow2a.png').convert_alpha()
arrow = pygame.transform.scale(arrow, (16,16))

forest_grass = pygame.image.load('tile_sets/forest_sprites/terrain_5x5.png').convert_alpha()  # How the images are loaded 
forest_grass = pygame.transform.scale(forest_grass, tile_size)  #Changing image to 16x16
forest_dirt = pygame.image.load('tile_sets/forest_sprites/terrain_5x5_dirt.png').convert_alpha()  # How the images are loaded in
forest_dirt = pygame.transform.scale(forest_dirt, tile_size)  #Changing image to 16x16
forest_left_slope = pygame.image.load('tile_sets/forest_sprites/terrain_slope_left.png').convert_alpha()  # How the images are loaded in
forest_left_slope = pygame.transform.scale(forest_left_slope, tile_size)  #Changing image to 16x16
forest_right_slope = pygame.image.load('tile_sets/forest_sprites/terrain_slope_right.png').convert_alpha()  # How the images are loaded in
forest_right_slope = pygame.transform.scale(forest_right_slope, tile_size)  #Changing image to 16x16
forest_left_slope_water = pygame.image.load('tile_sets/forest_sprites/terrain_water_left.png').convert_alpha()  # How the images are loaded in
forest_left_slope_water = pygame.transform.scale(forest_left_slope_water, tile_size)  #Changing image to 16x16
forest_right_slope_water = pygame.image.load('tile_sets/forest_sprites/terrain_water_right.png').convert_alpha()  # How the images are loaded in
forest_right_slope_water = pygame.transform.scale(forest_right_slope_water, tile_size)  #Changing image to 16x16
forest_water = pygame.image.load('tile_sets/forest_sprites/water_5x5.png').convert_alpha()  # How the images are loaded in
forest_water = pygame.transform.scale(forest_water, tile_size)  #Changing image to 16x16
forest_underwater = pygame.image.load('tile_sets/forest_sprites/terrain_underwater.png').convert_alpha()  # How the images are loaded in
forest_underwater = pygame.transform.scale(forest_underwater, tile_size)  #Changing image to 16x16
forest_deep = pygame.image.load('tile_sets/forest_sprites/water_5x5_deep.png').convert_alpha()  # How the images are loaded in
forest_deep = pygame.transform.scale(forest_deep, tile_size)  #Changing image to 16x16
forest_deep_slope_right = pygame.image.load('tile_sets/forest_sprites/terrain_underwater_slope_right.png').convert_alpha()  # How the images are loaded in
forest_deep_slope_right = pygame.transform.scale(forest_deep_slope_right, tile_size)  #Changing image to 16x16
forest_deep_slope_left = pygame.image.load('tile_sets/forest_sprites/terrain_underwater_slope_left.png').convert_alpha()  # How the images are loaded in
forest_deep_slope_left = pygame.transform.scale(forest_deep_slope_left, tile_size)  #Changing image to 16x16

dungeon_midgcs = pygame.image.load('tile_sets/dungeon_sprites/midground_center_shadowed.png').convert_alpha() #How the images are loaded in
dungeon_midgcs = pygame.transform.scale(dungeon_midgcs,tile_size) #Changing image to 16x16 
dungeon_midgls= pygame.image.load('tile_sets/dungeon_sprites/midground_left_B_shadowed.png').convert_alpha() #How the images are loaded in
dungeon_midgls= pygame.transform.scale(dungeon_midgls,tile_size)#Changing image to 16x16
dungeon_midgrs = pygame.image.load('tile_sets/dungeon_sprites/midground_right_B_shadowed.png').convert_alpha() #How the images are loaded in
dungeon_midgrs = pygame.transform.scale(dungeon_midgrs,tile_size) #Changing image to 16x16 

dungeon_pillartopnorm = pygame.image.load('tile_sets/dungeon_sprites/fg_pillar_top_A.png').convert_alpha() #How the images are loaded in
dungeon_pillartopnorm = pygame.transform.scale(dungeon_pillartopnorm,tile_size) #Changing image to 16x16 
dungeon_pillarmiddlenorm = pygame.image.load('tile_sets/dungeon_sprites/fg_pillar_center_A.png').convert_alpha() #How the images are loaded in
dungeon_pillarmiddlenorm = pygame.transform.scale(dungeon_pillarmiddlenorm,tile_size) #Changing image to 16x16 
dungeon_pillarbottomnorm = pygame.image.load('tile_sets/dungeon_sprites/fg_pillar_bottom_A.png').convert_alpha() #How the images are loaded in
dungeon_pillarbottomnorm = pygame.transform.scale(dungeon_pillarbottomnorm,tile_size) #Changing image to 16x16 
dungeon_bpillartop = pygame.image.load('tile_sets/dungeon_sprites/fg_pillar_top_B.png').convert_alpha() #How the images are loaded in
dungeon_bpillartop = pygame.transform.scale(dungeon_bpillartop,tile_size) #Changing image to 16x16 
dungeon_spikesdown = pygame.image.load('tile_sets/dungeon_sprites/spikes_B_down.png').convert_alpha() #How the images are loaded in
dungeon_spikesdown = pygame.transform.scale(dungeon_spikesdown,tile_size) #Changing image to 16x16 
dungeon_fullstairs = pygame.image.load('tile_sets/dungeon_sprites/terrain_slope_floor_B_full.png').convert_alpha() #How the images are loaded in
dungeon_fullstairs = pygame.transform.scale(dungeon_fullstairs,tile_size) #Changing image to 16x16 
dungeon_halfstairs = pygame.image.load('tile_sets/dungeon_sprites/terrain_slope_floor_B_half.png').convert_alpha() #How the images are loaded in
dungeon_halfstairsstairs = pygame.transform.scale(dungeon_halfstairs,tile_size) #Changing image to 16x16 
dungeon_understairs = pygame.image.load('tile_sets/dungeon_sprites/terrain_center_B.png').convert_alpha() #How the images are loaded in
dungeon_understairs = pygame.transform.scale(dungeon_understairs,tile_size) #Changing image to 16x16 
dungeon_largechain = pygame.image.load('tile_sets/dungeon_sprites/bg_chain_hanging.png').convert_alpha() #How the images are loaded in
dungeon_largechain = pygame.transform.scale(dungeon_largechain,tile_size) #Changing image to 16x16 
dungeon_bpillarbottom = pygame.image.load('tile_sets/dungeon_sprites/fg_pillar_bottom_B.png').convert_alpha() #How the images are loaded in
dungeon_bpillarbottom = pygame.transform.scale(dungeon_bpillarbottom,tile_size) #Changing image to 16x16 
dungeon_bpillarmiddle = pygame.image.load('tile_sets/dungeon_sprites/fg_pillar_top_C.png').convert_alpha() #How the images are loaded in
dungeon_bpillarmiddle = pygame.transform.scale(dungeon_bpillarmiddle,tile_size) #Changing image to 16x16 
dungeon_upspikes = pygame.image.load('tile_sets/dungeon_sprites/spikes_A_up.png').convert_alpha() #How the images are loaded in
dungeon_upspikes = pygame.transform.scale(dungeon_upspikes,tile_size) #Changing image to 16x16 
dungeon_lbmiddlepillar = pygame.image.load('tile_sets/dungeon_sprites/fg_pillar_center_B.png').convert_alpha() #How the images are loaded in
dungeon_lbmiddlepillar = pygame.transform.scale(dungeon_lbmiddlepillar,tile_size) #Changing image to 16x16 
dungeon_rockset1 = pygame.image.load('tile_sets/forest_sprites/rock_1.png').convert_alpha() #How the images are loaded in
dungeon_rockset1 = pygame.transform.scale(dungeon_rockset1,tile_size) #Changing image to 16x16 
dungeon_bspikeup = pygame.image.load('tile_sets/dungeon_sprites/spikes_B_up.png').convert_alpha() #How the images are loaded in
dungeon_bspikeup = pygame.transform.scale(dungeon_bspikeup,tile_size) #Changing image to 16x16 

cave_bg = pygame.image.load('tile_sets/cave_sprites/bg1.png').convert_alpha()
cave_bg = pygame.transform.scale(cave_bg, (960, 640))

dungeon_bg = pygame.image.load('tile_sets/dungeon_sprites/bg_dungeon.png').convert_alpha()
dungeon_bg = pygame.transform.scale(dungeon_bg, (960, 640))

forest_sky_bg = pygame.image.load('tile_sets/forest_sprites/bg_sky.png').convert_alpha()
forest_sky_bg = pygame.transform.scale(forest_sky_bg, (960,640))
forest_tree1_bg = pygame.image.load('tile_sets/forest_sprites/bg_tree_1.png').convert_alpha()
forest_tree1_bg = pygame.transform.scale(forest_tree1_bg, (960,640))
forest_tree2_bg = pygame.image.load('tile_sets/forest_sprites/bg_tree_2.png').convert_alpha()
forest_tree2_bg = pygame.transform.scale(forest_tree2_bg, (960,640))
forest_tree3_bg = pygame.image.load('tile_sets/forest_sprites/bg_tree_3.png').convert_alpha()
forest_tree3_bg = pygame.transform.scale(forest_tree3_bg, (960,640))

portal_rock1 = pygame.image.load('tile_sets/forest_sprites/rock_1.png')
portal_rock2 = pygame.image.load('tile_sets/forest_sprites/rock_2.png')
portal_rock3 = pygame.transform.flip(pygame.image.load('tile_sets/forest_sprites/rock_3.png'), False, True)
portal_rock4 = pygame.transform.flip(pygame.image.load('tile_sets/forest_sprites/rock_4.png'), False, True)

cave_fbc = pygame.image.load('tile_sets/cave_sprites/terrain_fill_bottom_center.png')
cave_fbc = pygame.transform.scale(cave_fbc, (16,16))
cave_bc = pygame.image.load('tile_sets/cave_sprites/terrain_bottom_center.png')
cave_bc = pygame.transform.scale(cave_bc, (16,16))
cave_bl = pygame.image.load('tile_sets/cave_sprites/terrain_bottom_left.png')
cave_bl = pygame.transform.scale(cave_bl, (16,16))
cave_br = pygame.image.load('tile_sets/cave_sprites/terrain_bottom_right.png')
cave_br = pygame.transform.scale(cave_br, (16,16))

mage_1 = pygame.image.load("Crops/mage1_crop.png").convert_alpha()
mage_1 = pygame.transform.scale(mage_1, (96, 96))

archer_1 = pygame.image.load("Crops/archer1_crop.png").convert_alpha()
archer_1 = pygame.transform.scale(archer_1, (96, 96))

sword_1 = pygame.image.load("Crops/sword1_crop.png").convert_alpha()
sword_1 = pygame.transform.scale(sword_1, (96, 96))

shield_1 = pygame.image.load("Crops/shield1_crop.png").convert_alpha()
shield_1 = pygame.transform.scale(shield_1, (96, 96))

true_scroll = [0, 0]


def load_map(path):
    '''Function to load the map file and split it into list.

    Inputs:
    path: the folder where the map is stored

    Outputs:
    game_map: the map on the screen
    
    '''
    f = open(path + '.txt', 'r')
    data = f.read()
    f.close
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map


def draw_text(text, font, color, surface, x, y, angle):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(pygame.transform.rotate(textobj, angle), textrect)


def get_xy_to_center_text(text, font):
    textobj = font.render(text, 1, (0, 0, 0))
    print("X: " + str((480 - textobj.get_rect()[2]) / 2))
    print("Y: " + str((360 - textobj.get_rect()[3]) / 2))
    print("WIDTH: " + str(textobj.get_rect()[2]))


#Loads map file
game_maps = []
game_maps.append(load_map('Maps/forest_map'))
game_maps.append(load_map('Maps/cave_map'))
game_maps.append(load_map('Maps/dungeon_map'))

test_player = Player()

stage = 0
click = None
main_menu = True
char_select = False
gaming = False
#get_xy_to_center_text("Mage", CHAR_FONT)
#get_xy_to_center_text("Archer", CHAR_FONT)
#get_xy_to_center_text("Knight", CHAR_FONT)
#get_xy_to_center_text("Vanguard", CHAR_FONT)

#get_xy_to_center_text("QUEST", MAIN_MENU_FONT)
FOREST_SOUND.play(-1)
while True:
    while main_menu:
        screen.fill((0, 0, 0))
        screen.blit(pygame.transform.scale(pygame.image.load("fantastick.png"), (480,360)),(0,0))
        #print("main menu background drawn")
        mx, my = pygame.mouse.get_pos()
        draw_text("FANTASTICK", MAIN_MENU_FONT, (0, 0, 0), screen, 58, 12, 0)
        draw_text("FANTASTICK", MAIN_MENU_FONT, (255, 255, 255), screen, 56, 10,
                  0)
        draw_text("QUEST", MAIN_MENU_FONT, (0, 0, 0), screen, 142, 76, 0)
        draw_text("QUEST", MAIN_MENU_FONT, (255, 255, 255), screen, 140, 74,
                  0)
        #print("main menu text drawn")
        play_button = pygame.Rect(27.5, 250, 175, 75)
        #pygame.draw.rect(screen, (255, 255, 255), play_button, 5, 25)
        draw_text("Play!", PLAY_FONT, (0, 0, 0), screen, 58, 262, 0)
        draw_text("Play!", PLAY_FONT, (255, 255, 255), screen, 56, 260, 0)

        if play_button.collidepoint((mx, my)):
            pygame.draw.rect(screen, (26, 51, 76), play_button, 0, 25)
            pygame.draw.rect(screen, (255, 255, 255), play_button, 5, 25)
            draw_text("Play!", PLAY_FONT, (0, 0, 0), screen, 58, 262, 0)
            draw_text("Play!", PLAY_FONT, (255, 255, 255), screen, 56, 260, 0)
            if click:
                print("Play!")
                main_menu = False
                char_select = True
        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(60)

    while char_select:
        screen.fill((0, 0, 0))
        # MAGE_2, ARCHER_3, HERO_SHIELD_1, SWORD_1
        draw_text("CHOOSE YOUR", PLAY_FONT, (255, 255, 255), screen, 61.5, 0,
                  0)
        draw_text("CHARACTER", PLAY_FONT, (255, 255, 255), screen, 88.5, 56, 0)
        mx, my = pygame.mouse.get_pos()

        screen.blit(mage_1, (19, 150))
        screen.blit(archer_1, (134, 150))
        screen.blit(sword_1, (249, 150))
        screen.blit(shield_1, (354, 150))

        mage_rect = pygame.Rect(19, 150, 96, 96)
        draw_text("Mage", CHAR_FONT, (255, 255, 255), screen, 38, 260, 0)
        archer_rect = pygame.Rect(134, 150, 96, 96)
        draw_text("Archer", CHAR_FONT, (255, 255, 255), screen, 143.5, 260, 0)
        sword_rect = pygame.Rect(249, 150, 96, 96)
        draw_text("Knight", CHAR_FONT, (255, 255, 255), screen, 258, 260, 0)
        shield_rect = pygame.Rect(354, 150, 96, 96)
        draw_text("Tank", CHAR_FONT, (255, 255, 255), screen, 373, 260, 0)
        
        if archer_rect.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(134, 150, 96, 96), 4)
            if click:
                print("Archer Selected")
                test_player.set_char(0)
                char_select = False
                gaming = True
        if mage_rect.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(19, 150, 96, 96), 4)
            if click:
                print("Mage Selected")
                test_player.set_char(1)
                char_select = False
                gaming = True

        if sword_rect.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(249, 150, 96, 96), 4)
            if click:
                print("Sword Selected")
                test_player.set_char(3)
                char_select = False
                gaming = True
        if shield_rect.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(354, 150, 96, 96), 4)
            if click:
                print("Shield Selected")
                test_player.set_char(2)
                char_select = False
                gaming = True
        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(60)

    while gaming:
        screen.fill((25, 35, 75))  #Sets the sky-blue BG color
        mx, my = pygame.mouse.get_pos()
        true_scroll[0] += (test_player.rect.x - true_scroll[0] - 104) / 10
        true_scroll[1] += (test_player.rect.y - true_scroll[1] - 240) / 10
        scroll = true_scroll.copy()
        scroll[0] = int(true_scroll[0])
        scroll[1] = int(true_scroll[1])
        #scroll = [0, 0]
        
        if stage == 0:
            screen.blit(forest_sky_bg, (0 - (scroll[0] * 0.05), 0 - (scroll[1] * 0.02)) )
            screen.blit(forest_tree3_bg, (0 - (scroll[0] * 0.1), 0 - (scroll[1] * 0.1)) )
            screen.blit(forest_tree2_bg, (0 - (scroll[0] * 0.2), 0 - (scroll[1] * 0.1)) )
            screen.blit(forest_tree1_bg, (0 - (scroll[0] * 0.3), 0 - (scroll[1] * 0.1)) )
            if test_player.rect.colliderect(pygame.Rect(2520,304,100,16)):
                stage += 1
                test_player.rect = pygame.Rect(122, 416, 16, 16)
                FOREST_SOUND.stop()
                CAVE_SOUND.play(-1)
        elif stage == 1:
            screen.blit(cave_bg, (0 - (scroll[0] * 0.2), 0 - (scroll[1] * 0.1)) )
            if test_player.rect.colliderect(pygame.Rect(2520,416,100,16)):
                stage += 1
                test_player.rect = pygame.Rect(126, 176, 16, 16)
                CAVE_SOUND.stop()
                DUNGEON_SOUND.play(-1)
        elif stage == 2:
            screen.blit(dungeon_bg, (-400 - (scroll[0] * 0.1), -100 - (scroll[1] * 0.05)) )
            if test_player.rect.colliderect(pygame.Rect(32,816,100,16)):
                DUNGEON_SOUND.stop()
                screen.fill((5,200,10))
                draw_text("you win...", MAIN_MENU_FONT, (255,255,255),screen,64,64,10)
                draw_text("you died... " + str(test_player.fake_deaths) + " times", CHAR_FONT, (255,255,255),screen,96,244,350)
                pygame.display.update()
                time.sleep(15)
                pygame.quit()
                quit()

        tile_rects = []
        reset_tile_list = []
        y = 0
        for row in game_maps[stage]:
            x = 0
            for tile in row:
                if tile == '1':
                    screen.blit(cave_fbc, (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == '2':
                    screen.blit(cave_bc,
                                (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == '3':
                    if stage == 0:
                        screen.blit(forest_left_slope_water, (x * 16 - scroll[0], y * 16 - scroll[1]))
                    else:
                        screen.blit(cave_bl,
                                (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == '4':
                    if stage == 0:
                        screen.blit(forest_right_slope_water, (x * 16 - scroll[0], y * 16 - scroll[1]))
                    else:
                        screen.blit(cave_br,
                                (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == 'd':
                    screen.blit(forest_dirt, (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == 'g':
                    screen.blit(forest_grass,  (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == 'r':
                  screen.blit(forest_right_slope,  (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == 'l':
                  screen.blit(forest_left_slope,  (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == 'w':
                  screen.blit(forest_water,  (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == 'u':
                  screen.blit(forest_underwater,  (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == '<':
                  screen.blit(forest_deep_slope_left,  (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == '>':
                  screen.blit(forest_deep_slope_right,  (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == '9':
                  screen.blit(forest_deep,  (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == '5':
                    screen.blit(dungeon_midgcs,  
                                (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == '6':
                    screen.blit(dungeon_midgls,  
                                (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == '8':
                    screen.blit(dungeon_pillartopnorm,  
                                (x * 16 - scroll[0], y * 16 - scroll[1]))  
                elif tile == 'y':
                  screen.blit(dungeon_pillarmiddlenorm, (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == 't':
                  screen.blit(dungeon_pillarbottomnorm, (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == 'q':
                    screen.blit(dungeon_bpillartop,  
                                (x * 16 - scroll[0], y * 16 - scroll[1]))  
                elif tile == 'z':
                    screen.blit(dungeon_spikesdown ,  
                                (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == '^':
                    screen.blit(arrow,  
                                (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == 'x':
                    screen.blit(dungeon_fullstairs ,  
                                (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == 'c':
                    screen.blit(dungeon_halfstairs ,  
                                (x * 16 - scroll[0], y * 16 - scroll[1])) 
                elif tile == 'v':
                    screen.blit(dungeon_understairs ,  
                                (x * 16 - scroll[0], y * 16 - scroll[1])) 
                elif tile == 'b':
                    screen.blit(dungeon_largechain ,  
                                (x * 16 - scroll[0], y * 16 - scroll[1]))   
                elif tile == 'n':
                    screen.blit(dungeon_bpillarbottom , 
                                (x * 16 - scroll[0], y * 16 - scroll[1]))  
                elif tile == 'm':
                    screen.blit(dungeon_bpillarmiddle , 
                                (x * 16 - scroll[0], y * 16 - scroll[1]))  
                elif tile == 'f':
                    screen.blit(dungeon_upspikes , 
                                (x * 16 - scroll[0], y * 16 - scroll[1]))  
                    
                elif tile == 'a':
                    screen.blit(dungeon_lbmiddlepillar ,                               (x * 16 - scroll[0], y * 16 - scroll[1])) 
                elif tile == 's':
                    screen.blit(dungeon_rockset1 ,                                      (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == 'o':
                    screen.blit(dungeon_bspikeup ,                                      (x * 16 - scroll[0], y * 16 - scroll[1]))
                elif tile == 'p':
                    screen.blit(portal_rock1, (x* 16 - scroll[0] - 16, y * 16 - scroll[1] - 16) )
                    screen.blit(portal_rock2, (x* 16 - scroll[0] - 8, y * 16 - scroll[1]) )
                    screen.blit(portal_rock1, (x* 16 - scroll[0] - 16, y * 16 - scroll[1] - 104) )
                    screen.blit(portal_rock3, (x* 16 - scroll[0] - 16, y * 16 - scroll[1]-64) )
                    screen.blit(portal_rock4, (x* 16 - scroll[0]-8, y * 16 - scroll[1] - 64) )
                # catch-all for un-implemented tiles
                elif tile != '0':              
                    screen.blit(dirt, (x * 16 - scroll[0], y * 16 - scroll[1]))                    
                if tile != '0':
                    if tile == 'f' or tile == 'z':
                        reset_tile_list.append(pygame.Rect((x * 16, y * 16,16,16)))
                    elif tile == '9' or tile == 'w':
                        reset_tile_list.append(pygame.Rect((x * 16, y * 16,16,16)))
                    elif tile == '<' or tile == '>':
                        reset_tile_list.append(pygame.Rect((x * 16, y * 16,16,16)))
                    elif tile == 'u':
                        reset_tile_list.append(pygame.Rect((x * 16, y * 16,16,16)))
                    elif tile == '^':
                        pass
                    else:
                        tile_rects.append(pygame.Rect((x * tile_size[0]), (y * tile_size[1]), tile_size[0], tile_size[1]))
                x += 1
            y += 1
        #pygame.Rect(48, 144, 16, 16), pygame.Rect(122, 416, 16, 16), pygame.Rect(126, 176, 16, 16)
        draw_text("Deaths: " + str(test_player.fake_deaths), CHAR_FONT, (255,255,255), screen, 25,25,0 )
        if stage == 0:
            test_player.update(tile_rects, reset_tile_list, pygame.Rect(48, 144, 16, 16))
        elif stage == 1:
            test_player.update(tile_rects, reset_tile_list, pygame.Rect(122, 416, 16, 16))
        elif stage == 2:
            test_player.update(tile_rects, reset_tile_list, pygame.Rect(126, 176, 16, 16))              

        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= 2:
                #print("frame_reset")
                frame = 0
        #screen.blit(pygame.transform.scale(test_player.idle_frames[frame], (48, 48)),(test_player.rect.x - scroll[0] - 16,test_player.rect.y - scroll[1] - 24))
        if test_player.is_jumping:
            screen.blit(pygame.transform.scale(pygame.image.load('hand2.png'), (16,16)), (mx+4,my))
        else:
            screen.blit(pygame.transform.scale(pygame.image.load('hand1.png'), (16,16)), (mx+4,my))
        test_player.draw(48, frame, screen,
                         test_player.rect.x - scroll[0] - 16,
                         test_player.rect.y - scroll[1] - 24)
        #pygame.draw.rect(screen, (255, 255, 255), (test_player.rect.x - scroll[0], test_player.rect.y - scroll[1], 16, 16))
        #pygame.draw.rect(screen, (255, 255, 255), (test_player.rect.x, test_player.rect.y, 16, 16))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                WINDOW = pygame.display.set_mode(event.size)
            if event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == K_d:
                    test_player.right = True
                if event.key == K_LEFT or event.key == K_a:
                    test_player.left = True
                if event.key == K_UP or event.key == K_w:
                    test_player.is_jumping = True
                    test_player.action = 2
                    if test_player.air_timer < 10:
                        test_player.y_momentum = -5
            if event.type == KEYUP:
                if event.key == K_RIGHT or event.key == K_d:
                    test_player.right = False
                if event.key == K_LEFT or event.key == K_a:
                    test_player.left = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    #print("YOU CLICKED SO HOPEFULLY YOU MOVED")
                    #print(test_player.movement)
                    if test_player.is_jumping:
                        test_player.movement[0] += (mx - test_player.rect.x +
                                                    scroll[0])
                        test_player.movement[1] += (my - test_player.rect.y +
                                                    scroll[1])
                    #print(test_player.movement)
            #print("Player Rect: " + str(test_player.rect))
            #print(reset_tile_list)
            if test_player.rect.y >= 800 and stage != 2:
                test_player.kill_player()
            elif test_player.rect.y >= 3000:
                test_player.kill_player()
            
          
            if test_player.is_dead:
                pygame.draw.rect(screen, (170,35,35), (0,0,480,360))
                draw_text("you died...", MAIN_MENU_FONT, (255,255,255),screen,64,64,10)
                pygame.display.update()
                time.sleep(5)
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(60)
