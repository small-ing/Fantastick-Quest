import pygame
import spritesheet
import glob
'''player_sprite_sheet = []
player_sprite_sheet.append(pygame.image.load("default_mage_sheet_adj.png"))
player_sprite_sheet.append(pygame.image.load("default_mage_sheet_adj2.png"))
player_sprite_sheet.append(pygame.image.load("default_mage_sheet_adj3.png"))

player_sheet = []
for sheet in player_sprite_sheet:
    player_sheet.append(spritesheet.SpriteSheet(sheet))
'''
archer_idle = []
archer_idle.append(
    pygame.image.load('character_sprites/archer_idle/idle1_1.png'))
archer_idle.append(
    pygame.image.load('character_sprites/archer_idle/idle1_2.png'))
archer_idle.append(pygame.transform.flip(pygame.image.load('character_sprites/archer_idle/idle1_1.png'), True, False))
archer_idle.append(pygame.transform.flip(pygame.image.load('character_sprites/archer_idle/idle1_2.png'), True, False))

mage_idle = []
mage_idle.append(pygame.image.load('character_sprites/mage_idle/idle2_1.png'))
mage_idle.append(pygame.image.load('character_sprites/mage_idle/idle2_2.png'))
mage_idle.append(pygame.transform.flip(pygame.image.load('character_sprites/mage_idle/idle2_1.png'), True, False))
mage_idle.append(pygame.transform.flip(pygame.image.load('character_sprites/mage_idle/idle2_2.png'), True, False))

shield_idle = []
shield_idle.append(
    pygame.image.load('character_sprites/shield_idle/idle3_1.png'))
shield_idle.append(
    pygame.image.load('character_sprites/shield_idle/idle3_2.png'))
shield_idle.append(pygame.transform.flip(pygame.image.load('character_sprites/shield_idle/idle3_1.png'), True, False))
shield_idle.append(pygame.transform.flip(pygame.image.load('character_sprites/shield_idle/idle3_2.png'), True, False))

sword_idle = []
sword_idle.append(
    pygame.image.load('character_sprites/sword_idle/idle4_1.png'))
sword_idle.append(
    pygame.image.load('character_sprites/sword_idle/idle4_2.png'))
sword_idle.append(pygame.transform.flip(pygame.image.load('character_sprites/sword_idle/idle4_1.png'), True, False))
sword_idle.append(pygame.transform.flip(pygame.image.load('character_sprites/sword_idle/idle4_2.png'), True, False))

idle_animations = [archer_idle, mage_idle, shield_idle, sword_idle]

archer_dir = 'character_sprites/archer_walk'
archer_walk = []
for images in glob.iglob(f'{archer_dir}/*'):
    archer_walk.append(pygame.image.load(images))

mage_dir = 'character_sprites/mage_walk'
mage_walk = []
for images in glob.iglob(f'{mage_dir}/*'):
    mage_walk.append(pygame.image.load(images))

shield_dir = 'character_sprites/shield_walk'
shield_walk = []
for images in glob.iglob(f'{shield_dir}/*'):
    shield_walk.append(pygame.image.load(images))

sword_dir = 'character_sprites/sword_walk'
sword_walk = []
for images in glob.iglob(f'{sword_dir}/*'):
    sword_walk.append(pygame.image.load(images))

walk_animations = [archer_walk, mage_walk, shield_walk, sword_walk]

archer_dir = 'character_sprites/archer_jump'
archer_jump = []
for images in glob.iglob(f'{archer_dir}/*'):
    archer_jump.append(pygame.image.load(images))

mage_dir = 'character_sprites/mage_jump'
mage_jump = []
for images in glob.iglob(f'{mage_dir}/*'):
    mage_jump.append(pygame.image.load(images))

shield_dir = 'character_sprites/shield_jump'
shield_jump = []
for images in glob.iglob(f'{shield_dir}/*'):
    shield_jump.append(pygame.image.load(images))

sword_dir = 'character_sprites/sword_jump'
sword_jump = []
for images in glob.iglob(f'{sword_dir}/*'):
    sword_jump.append(pygame.image.load(images))

jump_animations = [archer_jump, mage_jump, shield_jump, sword_jump]

class Player(pygame.sprite.Sprite):

    def generate_spritesheets(self):
        for image in idle_animations[self.char]:
            self.idle_frames.append(image)
        for image in walk_animations[self.char]:
            self.walk_frames.append(image)
        for image in jump_animations[self.char]:
            self.jump_frames.append(image)

    # 58 w 60 h
    def __init__(self):
        super().__init__()

        self.char = None  # redefine to change character
        self.idle_frames = []
        self.walk_frames = []
        self.jump_frames = []
        self.action = 0 # 0 means idle, 1 means walk, 2 means jump prob

        self.image = pygame.transform.scale(
            pygame.image.load("Crops/mage1_crop.png"),
            (16, 16))
        #print(spawn_list)
        self.rect = pygame.Rect(48, 144, 16, 16)
        self.movement = [0, 0]
        self.is_moving = False
        
        self.right = False
        self.left = False
        self.is_facing_left = False
        self.is_jumping = False
        self.fake_deaths = 0
        self.is_dead = False
        self.y_momentum = 0
        self.air_timer = 0

    def collision_test(self, tiles):
        hit_list = []
        for tile in tiles:
            if self.rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def move(self, tiles, reset_tiles, reset_spot):
        self.collision_types = {
            'top': False,
            'bottom': False,
            'right': False,
            'left': False
        }
        hit_list = self.collision_test(reset_tiles)
        if hit_list:
            #print('reset')
            self.fake_deaths += 1
            self.rect = reset_spot
        else:
            self.rect.y += self.movement[1]
            hit_list = self.collision_test(tiles)
            for tile in hit_list:
                if self.movement[1] > 0:
                    self.rect.bottom = tile.top
                    self.collision_types['bottom'] = True
                elif self.movement[1] < 0:
                    self.rect.top = tile.bottom
                    self.collision_types['top'] = True
    
            self.rect.x += self.movement[0]
            hit_list = self.collision_test(tiles)
            for tile in hit_list:
                if self.movement[0] > 0:
                    self.rect.right = tile.left
                    self.collision_types['right'] = True
                elif self.movement[0] < 0:
                    self.rect.left = tile.right
                    self.collision_types['left'] = True

        return self.collision_types

    def update(self, rects, reset_rects, reset_spot):
        if self.right:
            if not self.is_jumping:
                self.action = 1
            self.is_facing_left = False
            self.movement[0] += 1
        if self.left:
            if not self.is_jumping:
                self.action = 1
            self.is_facing_left = True
            self.movement[0] -= 1
        if not self.left and not self.right:
            if not self.is_jumping:
                self.action = 0
            else:
                self.action = 2
        self.movement[1] += self.y_momentum
        self.y_momentum += 0.15
        if self.y_momentum > 3:
            self.PLAYER_y_momentum = 3
        self.collisions = self.move(rects, reset_rects, reset_spot)

        if self.collisions['bottom']:
            self.y_momentum = 0
            self.air_timer = 0
            self.is_jumping = False
        else:
            self.air_timer += 1

        if self.collisions['top']:
            self.y_momentum = 0
        self.movement = [0, 0]

    def draw(self, scale, frame, surface, x, y):
        if self.action == 0:    
            if not self.is_facing_left:
                surface.blit(pygame.transform.scale(self.idle_frames[frame], (scale, scale)) , (x, y) )
            else:
                surface.blit(pygame.transform.scale(self.idle_frames[frame+2], (scale, scale)) , (x, y) )
        elif self.action == 1:
            if not self.is_facing_left:
                surface.blit(pygame.transform.scale(self.walk_frames[frame], (scale, scale)) , (x, y) )
            else:
                surface.blit(pygame.transform.scale(pygame.transform.flip(self.walk_frames[frame], True, False), (scale, scale)) , (x, y) )
        elif self.action == 2:
            if not self.is_facing_left:
                surface.blit(pygame.transform.scale(self.jump_frames[frame], (scale, scale)) , (x, y) )
            else:
                surface.blit(pygame.transform.scale(pygame.transform.flip(self.jump_frames[frame], True, False), (scale, scale)) , (x, y) )
        else:
            print("something broke")
            
    def set_char(self, char):
        self.char = char
        self.generate_spritesheets()

    def reset_char_spawn(self, stage, tile):
        if tile.colliderect(self.rect):
            print("SHOULD RESET AT STAGE " + str(stage))
            print(self.rect)
            print(spawn_list)
            print(spawn_list[stage])
            self.rect.x = spawn_list[stage][0]
            self.rect.y = spawn_list[stage][1]
            print(self.rect)
            return True
        return False

    def kill_player(self):
        self.is_dead = True