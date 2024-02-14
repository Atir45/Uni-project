import pygame
import os 
import random
WIDTH = 800
HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 60
tile_size = 50
primary_background_image = pygame.transform.scale(pygame.image.load(os.path.join('back.png')), (800,800))

curse_group = pygame.sprite.Group()

#updates the screen
def draw_window():
    WIN.fill(WHITE)
    WIN.blit(primary_background_image,(0, 0))  
    player.update()
    world.draw()
    pygame.display.update()
    

#draws grids for easy world building
def draw_grid():
    for line in range(0, 16):
        pygame.draw.line(WIN, (255,255,255), (0,line * tile_size),(WIDTH , line * tile_size))
        pygame.draw.line(WIN, (255,255,255), (line * tile_size, 0),(line * tile_size, HEIGHT))




#draws player
class Player():
    def __init__(self, x , y):
        Health = 100
        width_character = 40
        height_character = 90
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1,7):
            img_right = (pygame.image.load(os.path.join(f'GOJO{num}.png')))
            img_right = pygame.transform.scale(img_right,(width_character , height_character))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width= self.image.get_width()
        self.height= self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
    
    def update(self):
        dx = 0
        dy = 0
        walk_cooldown = 6
        #get keypress
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
             self.vel_y = -18
             self.jumped = True
             if self.rect.y < 0:
                 self.rect.top = 0

                
        if key[pygame.K_SPACE] == False:
            self.jumped = False
            self.image = self.images_right[self.index]
        if key[pygame.K_LEFT]and self.rect.x > dx:
           dx -= 5  
           self.counter += 1
           self.direction = -1
           self.image = self.images_left[self.index]
        if key[pygame.K_RIGHT] and self.rect.x < 800 - self.width - dx :
           dx += 5
           self.counter += 1
           self.direction = 1
        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

        #handle animation
           
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                 self.index =0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]
           
       

        #add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        #check for collison 
        
        for tile in world.tile_list:
            #check for collision in x direction
            if tile[1].colliderect(self.rect.x + dx , self.rect.y , self.width , self.height):
                dx = 0
            #check for collision in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy , self.width , self.height):
                #check if below the ground i.e jumping 
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0
                
        

        #update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.height))

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        WIN.blit(self.image , self.rect)
        
#draws world
class World():
    def __init__(self,data):
        self.tile_list =[]
        tile_set_1 = pygame.image.load(os.path.join('tile_set_1.png'))
        tile_set_2 = pygame.image.load(os.path.join('tile_set_2.png'))
        tile_set_3 = pygame.image.load(os.path.join('tile_set_3.png'))
        tile_set_4 = pygame.image.load(os.path.join('tile_set_4.png'))
        tile_set_5 = pygame.image.load(os.path.join('tile_set_5.png'))
        tile_set_6 = pygame.image.load(os.path.join('tile_set_6.png'))
        tile_set_7 = pygame.image.load(os.path.join('tile_set_7.png'))
        row_count = 0

        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(tile_set_1, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count*tile_size
                    img_rect.y = row_count*tile_size
                    tile = (img , img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(tile_set_2, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count*tile_size
                    img_rect.y = row_count*tile_size
                    tile = (img , img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(tile_set_3, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count*tile_size
                    img_rect.y = row_count*tile_size
                    tile = (img , img_rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    img = pygame.transform.scale(tile_set_4, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count*tile_size
                    img_rect.y = row_count*tile_size
                    tile = (img , img_rect)
                    self.tile_list.append(tile)    
                if tile == 5:
                    img = pygame.transform.scale(tile_set_5, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count*tile_size
                    img_rect.y = row_count*tile_size
                    tile = (img , img_rect)
                    self.tile_list.append(tile)
                if tile == 6:
                    img = pygame.transform.scale(tile_set_6, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count*tile_size
                    img_rect.y = row_count*tile_size
                    tile = (img , img_rect)
                    self.tile_list.append(tile)
                if tile == 7:
                    img = pygame.transform.scale(tile_set_7, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count*tile_size
                    img_rect.y = row_count*tile_size
                    tile = (img , img_rect)
                    self.tile_list.append(tile)
                if tile == 8:
                    Curse = Enemy(col_count*tile_size, row_count*tile_size)
                    curse_group.add(Curse)
                col_count = col_count + 1
            row_count = row_count + 1
    def draw(self):
        for tile in self.tile_list:
            WIN.blit(tile[0], tile[1])
            
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('curse1.png')),(tile_size,tile_size))
        self.rect =self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



world_data = [
     [4,7,7,7,7,7,7,7,7,7,7,7,7,7,7,4],
     [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
     [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
     [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
     [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
     [5,0,0,0,0,0,0,0,0,8,0,0,0,0,0,6],
     [1,1,0,0,4,4,0,0,1,1,1,0,0,0,0,6],
     [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
     [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
     [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
     [5,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4],
     [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
     [5,0,0,0,0,0,0,3,3,3,0,0,0,0,0,6],
     [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
     [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
     ]


player = Player(100, 410)
world = World(world_data)





#handles initiation
def main():
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
        draw_window()
       
    pygame.quit()







if __name__ == "__main__":
    main()