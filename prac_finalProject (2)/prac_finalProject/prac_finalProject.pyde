add_library('minim')
import random
path = os.getcwd()
WIDTH = 1200
HEIGHT = 600
CELLDIM = 30
NUMOFCOLS = WIDTH//CELLDIM
NUMOFROWS = HEIGHT//CELLDIM

#import library for music and set the boolean value for instructions to appear as false.
player = Minim(this)
instructions = False
bg = ""

#2 different 2D arrays representing the maze. MAZE is used in level one as it has fewer walls and is therefore easy to navigate; MAZE2 is for level 2 and has more walls and so is harder. 
#the 1's represent walls, 2's in MAZE represent areas where the image of the player will come and 0's represent the pathways or areas where players can walk

MAZE = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
        [1,2,0,2,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,1,2,0,0,0,0,0,0,0,0,0,2,1],
        [1,2,0,2,1,2,0,2,2,2,2,2,2,2,2,0,2,2,2,2,2,2,0,2,2,2,2,1,2,0,2,2,2,2,2,2,2,0,2,1],
        [1,2,0,2,1,2,0,2,1,1,1,1,1,1,2,0,2,1,1,1,1,2,0,0,0,0,2,1,2,0,2,1,1,1,1,1,2,2,2,1],
        [1,2,0,2,2,2,0,2,2,2,2,1,2,2,2,0,2,2,2,2,1,2,0,2,2,2,2,1,2,0,2,1,2,2,2,1,1,1,1,1],
        [1,2,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,2,1,2,0,2,1,1,1,1,2,0,2,1,2,0,2,1,2,2,2,1],
        [1,2,2,2,2,2,2,2,2,0,2,1,2,2,2,2,2,2,0,2,1,2,0,2,2,2,2,2,2,0,2,2,2,0,2,1,2,0,2,1],
        [1,1,1,1,1,1,1,1,2,0,2,1,1,1,1,1,1,2,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,2,1],
        [1,2,2,2,2,2,2,2,2,0,2,2,2,2,2,2,1,2,0,0,0,0,0,2,2,2,2,2,0,2,2,2,0,0,0,0,0,0,2,1],
        [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,2,2,2,2,2,1,1,1,2,0,2,1,2,0,2,2,2,2,0,2,1],
        [1,2,0,2,2,2,0,2,2,2,2,2,2,2,2,2,1,2,0,2,1,1,1,1,1,2,2,2,0,2,1,2,0,2,1,1,2,0,2,1],
        [1,2,2,2,1,2,0,2,1,1,1,1,1,1,1,1,1,2,0,2,1,2,2,2,1,2,0,0,0,2,1,2,0,2,2,1,2,2,2,1],
        [1,1,1,1,1,2,0,2,1,2,2,2,1,2,2,2,1,2,0,2,1,2,0,2,1,2,2,2,0,2,1,2,0,2,1,1,1,1,1,1],
        [1,2,2,2,1,2,0,2,1,2,0,2,2,2,0,2,2,2,0,2,1,2,0,2,1,1,1,2,0,2,1,2,2,2,2,1,2,2,2,1],
        [1,2,0,2,2,2,0,2,1,2,0,0,0,0,0,0,0,0,0,2,2,2,0,2,2,2,2,2,0,2,1,1,1,1,1,1,2,0,2,1],
        [1,2,0,0,0,0,0,2,2,2,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,0,2,1],
        [1,2,2,2,2,2,0,0,0,0,0,2,1,1,1,1,1,2,0,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,2,1],
        [1,2,2,1,1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

MAZE2 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,0,1,0,1],
        [1,0,1,0,1,0,0,0,0,1,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,1,1,0,1,0,1,1,0,0,0,0,0,1,0,1],
        [1,0,0,0,1,0,1,1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1],
        [1,0,1,1,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,1,0,1],
        [1,0,0,0,0,0,1,0,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1],
        [1,1,1,1,0,1,1,0,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1],
        [1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,1,1,1,0,1,0,1,0,0,0,1],
        [1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1],
        [1,0,1,0,0,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,0,1],
        [1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,0,1],
        [1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1],
        [1,0,0,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1],
        [1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,1,1,1,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0,1,0,1],
        [1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


# create a list to store all the x and y coordinates of the pathways on both the maze. this helps randomly assign location of enemies, players, bombs, coins and the health kit.
# 
x_object = []
y_object = []

x_object2 = []
y_object2 = []

for j in range(HEIGHT//CELLDIM):
    for i in range(WIDTH//CELLDIM):
        if MAZE[j][i] == 0:
            y_object.append(j*CELLDIM)
            x_object.append(i*CELLDIM)

for j in range(HEIGHT//CELLDIM):
    for i in range(WIDTH//CELLDIM):
        if MAZE2[j][i] == 0:
            y_object2.append(j*CELLDIM)
            x_object2.append(i*CELLDIM)

# create a boolean variable to indicate when game should start and when it should end. Altered within the main Maze class to start/end game
startgame = False
gameover = False

# dictionary object used when coding the movement of the enemy
neighbors = [[1,0], [0,1], [0,-1], [-1,0], [-1,-1], [1,1], [-1,1],[1,-1]]

 #the x and y coordinates are defined upon instanciation as every onstance of a coin will have a different random x and y coordinate
#num _ frames = 4, this is used to make the coins rotate when displayed
# width and height of the coin image are instanciated since it will be different for both levels (i.e. 30x30 for level 1 and 15x15 for level2)
class Coins:
    def __init__(self, x, y, num_frames, w, h):
         global MAZE, MAZE2, x_object, y_object, x_object2, y_object2
         self.x = x
         self.y = y
         self.h = h
         self.w = w
         self.frame = 0
         self.num_frames = num_frames
     
    def update(self):
      #coin image updates itself after every 2 frames
        if frameCount%2 == 0:
          #load coin image, update self. frame value so it increments after 2 frames and returns to 0 after it's value is 4. 
            self.frame = (self.frame + 1) % self.num_frames
        
    #display takes x and y as argument because every coin has a differnt x and y coordinate so they don't overlap
    #display image for coin. 
    def display(self, x, y):
        img = loadImage(path + "/data/coin.png" ) 
        self.update()
        image(img, x, y, self.w, self.h, 0, CELLDIM*self.frame, 30, CELLDIM*self.frame +30)

#create class to define code for how the health kit will appear       
class HealthKit:
    def __init__(self):
         global MAZE, MAZE2, x_object,y_object, x_object2, y_object2
         self.x = 0 #instantiate at zero and make it random in attackByEenemy code for every instance
         self.y = 0 
         self.cnt = 0
        #the value of cnt becomes 1 when the kit needs to be displayed. it continues to increment till player collides with kit and at this instant self.cnt is reset to 0
      #load health kit and display it, dimentions remain same for both levels# this class has methods that dictat how tevery instance of the enemy will randomly move and how the enemy is to be diplayed in differnt levels #this class has methods that define when and where and how boms will appear. this is only a feature of level 2

    def display(self):
        img = loadImage(path + '/data/helth.png')
        image(img, self.x , self.y , 30, 30, 0, 0, 30,30)

#create a class  to define enemies
class Enemy:
  #class initializer
    def __init__(self, x, y):
        global MAZE, MAZE2, x_object,y_object, neighbors, img, x_object2, y_object2, maze_type
        self.x = x 
        self.y =  y 
        self.x_direc = 0
        self.y_direc = 0
        #ensures enemy can only move in 4 directions
        while self.x_direc == self.y_direc:
            self.x_direc = random.randint(-1,1)
            self.y_direc = random.randint(-1,1)
        self.up = True
        self.down = True
        self.left = True
        self.right = True
        self.d = 0
        self.frame = 0
        self.num_frames = 3
        # self.img = img
        
    #randomly moves the enemy in random direction and ensuring that it does not go through walls
    def move(self):
        count = 0
        while count < 4:
            direction = random.randint(0,4)
            #if possible to move right increase the x coordinates of enemy
            if self.right == True and direction == 1 and maze_type[self.y//CELLDIM][self.x//CELLDIM+1] == 0:
                self.x += CELLDIM 
                self.right = False
                self.left = False
                self.up = True
                self.down = True
                break
            else:
                count += 1
            #if left
            if self.left == True and direction == 2 and maze_type[self.y//CELLDIM][self.x//CELLDIM-1] == 0:
                self.x -= CELLDIM  
                self.left = False
                self.right = False
                self.up = True
                self.down = True 
                break
            else:
                count +=1
                
            #if up block is a pathway
            if self.up == True and direction == 3 and maze_type[self.y//CELLDIM - 1][self.x//CELLDIM] == 0: 
                self.y -= CELLDIM
                self.up = False
                self.down = False
                self.left = True
                self.right = True
                break
            else:
                count +=1
            #if down is pathway
            if self.down == False and direction == 4 and maze_type[self.y//CELLDIM + 1][self.x//CELLDIM] == 0:
                self.y += CELLDIM
                self.left = True
                self.right = True
                self.up = False
                self.down = False
                break
            else:
                count +=1
                    
        if maze_type[self.y//CELLDIM+self.y_direc][self.x//CELLDIM+self.x_direc] == 0:
            self.x += (CELLDIM*self.x_direc) 
            self.y += (CELLDIM*self.y_direc) 
        else:
            self.x_direc = 0
            self.y_direc = 0
            while self.x_direc == self.y_direc:
                self.x_direc = random.randint(-1,1)
                self.y_direc = random.randint(-1,1)
            
    def display(self):
        self.move() 
        if maze.game == 1:   
        
            if frameCount%1 == 0:
                self.frame = (self.frame + 1) % self.num_frames
            if self.x_direc == 1:
                image(self.img, self.x - CELLDIM, self.y - CELLDIM, 90, 90, 0, 90*self.frame, 90, 90*self.frame + 90)
            elif self.x_direc == -1:
                image(self.img, self.x - CELLDIM, self.y - CELLDIM, 90, 90, 90, 90*self.frame , 0, 90*self.frame +90 )
            else:
                cnt = 1
                image(self.img, self.x - CELLDIM, self.y - CELLDIM, 90, 90, 0, 90*(cnt + 3), 90, 90*(cnt + 3) + 90 )
                cnt += 1
                if cnt == 2:
                    cnt = 1
                       
        if maze.game == 2: 
            if frameCount%1 == 0:
                self.frame = (self.frame + 1) % self.num_frames
            if self.x_direc == 1:
                image(self.img, self.x , self.y , 30, 30, 0, 90*self.frame, 90, 90*self.frame + 90)
            elif self.x_direc == -1:
                image(self.img, self.x , self.y , 30, 30, 0, 90*self.frame, 90, 90*self.frame + 90)
            else:
                cnt = 1
                image(self.img, self.x , self.y,30, 30, 0, 90*self.frame, 90, 90*self.frame + 90 )
                cnt += 1
                if cnt == 2:
                    cnt = 1


class Bomb:
    def __init__(self, x, y, num_frames):
        global  maze_type,  x_object2, y_object2
        self.x = y 
        self.y = x 
        self.frame = 0
        self.num_frames = num_frames
        self.img = loadImage(path + "/data/bomb.png")
        self.appear = False
        

    def update(self):
        if frameCount%150 == 0:
            self.appear = True
     

        if frameCount%170 == 0:
            self.appear = False
            rand_int = random.randint(0,len(x_object2)-1)
            self.x = x_object2[rand_int]
            self.y = y_object2[rand_int]
          
        if self.appear == True:
            if frameCount%10 == 0:
                self.frame = (self.frame+1) % self.num_frames
                image(self.img, self.x, self.y ,30, 30, 0, self.frame *90, 90, self.frame *90 + 90)
                
#geneic player class with methods related to the player
class Characters:
     def __init__(self, x, y, d, w, h):
         global MAZE, x_object,y_object, x_object2, y_object2, maze_type
         self.d = d #Direction to indicate splites moves
         self.x = x 
         self.y =  y 
         self.w = w
         self.h = h
         self.health = 3
         self.score = 0 
        

    
     def move(self):
        self.vx = 0
        self.vy = 0
     def collision(self, object, health):
      #checks if object collides with anyhrion
        if sqrt(((self.x - object.x)**2) + ((self.y - object.y)**2)) <= CELLDIM:
            health.cnt = 1
            self.health -= 1
            rand_int = random.randint(0,len(x_object)-1)
            object.x = x_object[rand_int]
            object.y = y_object[rand_int]
        
                 #defines situation in which health kit should appear that is collison with other plyer or enemy
             
     def healthkit_appears(self):
        #use self.cnt to track collision of player and enemy or player, if collision occurs, self.cnt  = 1 
        # only if there is a collision, a health kit will appear, this kit will continue to appear till the player gets it (self.cnt increments by 1)
        # the kit wont appear only if self.cnt is 0, which is either when there is no collision or when player gets the kit. 
        if maze.game == 1:
            self.collision(maze.e, maze.hk)
            player1 = maze.p1
            player2 = maze.p2
            health_kit = maze.hk
            i = 2
            j = 1
            rand_x = x_object
            rand_y = y_object
            
        if maze.game == 2:
            self.collision(maze.e2, maze.hk2)
            self.collision(maze.e3, maze.hk2)
            self.collision(maze.e4, maze.hk2)
            self.collision(maze.e5, maze.hk2)
            self.collision(maze.e6, maze.hk2)
            self.collision(maze.bomb, maze.hk2)
            player1 = maze.p1_l2
            player2 = maze.p2_l2
            health_kit = maze.hk2
            rand_x = x_object2
            rand_y = y_object2
            i = 1
            j = 0
        #checks distnace between both players if less than the diameter of one images, they collide
        if sqrt(((player1.x + CELLDIM//2 - player2.x + (j*CELLDIM//2))**2) + ((player1.y + CELLDIM//2 - player2.y + (j*CELLDIM//2))**2)) < i*CELLDIM:
            health_kit.cnt = 1
            player1.health -= 1
            player2.health -= 1
            rand_int = random.randint(0,len(rand_x)-1)
            player1.x = rand_x[rand_int]
            player1.y = rand_y[rand_int]
            rand_int = random.randint(0,len(rand_x)-1)
            player2.x = rand_x[rand_int]
            player2.y = rand_y[rand_int]
            
        #checks distnace between player and heath kit, if more than diameter, cnt increments they collide
        if health_kit.cnt == 1 and (sqrt(((self.x - health_kit.x)**2) + ((self.y - health_kit.y)**2)) >= CELLDIM or sqrt(((player1.x + (j*CELLDIM//2) - player2.x +(j*CELLDIM//2))**2) + ((player1.y + (j*CELLDIM//2) - player2.y + (j*CELLDIM//2)))**2) >= i*CELLDIM):
            health_kit.cnt += 1
            rand_int = random.randint(0,len(x_object)-1)
            health_kit.x = rand_x[rand_int]
            health_kit.y = rand_y[rand_int]
      #when player collides with health kit cnt ==. 1 and kit disappears
        if sqrt(((self.x - health_kit.x)**2) + ((self.y - health_kit.y)**2)) < CELLDIM:
            if self.health < 3:
                health_kit.cnt = 0 
                self.health +=1
                rand_int = random.randint(0,len(rand_x)-1)
                health_kit.x = 0 
                health_kit.y = 0
            else:
                health_kit.cnt +=1
     
        
                
       #method to detect colission with coins, increments score             
     def check_collision_coin(self, coin, i):

        if sqrt(((self.x + CELLDIM//2 - coin.x)**2) + ((self.y + CELLDIM//2 - coin.y)**2) ) < i*CELLDIM:
            return True
        else:
            return False    
     #display players so that their image changes to reflect the direction they are facing, increment score
     def display(self):
        
        if maze.game == 1:
            self.move()
            self.healthkit_appears()
            image(self.img, self.x - CELLDIM , self.y - CELLDIM, self.w, self.h, 0, self.d * 80, 80, self.d * 80 + 80)
            for coin in maze.coinlist:
                if self.check_collision_coin(coin, 2) == True:
                    self.score += 1
                    maze.coinlist.remove(coin)
                    
        if maze.game == 2:
            self.move()
            self.healthkit_appears()
            image(self.img, self.x  , self.y , self.w, self.h, 0, self.d * 80, 80, self.d * 80 + 80)
            for coin in maze.coinlist2:
                if self.check_collision_coin(coin, 1) == True:
                    self.score += 1
                    maze.coinlist2.remove(coin)
 #class for player 1 inhreits the character class since collison, score incrementing etc remains same for both players.                   
class PlayerOne(Characters):
    global maze_type
    def __init__(self, x, y, d, w, h):
        Characters.__init__(self, x, y, d, w, h)
        self.d = d
        self.x = x 
        self.y =  y 
        self.w = w
        self.h = h
        self.key_code = {LEFT: False, RIGHT: False, UP: False, DOWN: False} #initialize key codes
    #player one moves with arrow keys,  this function sees if movement is possible and if so, self.vy and self.vs increment based on direction and player moves
    def move(self):
            self.vx = 0
            self.vy = 0
    
            if self.key_code[LEFT] == True:
                if self.x - CELLDIM >= 0 and self.x <= WIDTH - CELLDIM and maze_type[self.y//CELLDIM][self.x//CELLDIM-1] == 0 :
                    self.vx = -30
                    self.vy = 0
                    self.d = 2
    
            elif self.key_code[RIGHT] == True:
                if self.x + CELLDIM <= WIDTH - CELLDIM and self.x  >= 0 and maze_type[self.y//CELLDIM][self.x//CELLDIM+1] == 0:
                    self.vx = 30
                    self.vy = 0
                    self.d = 3
        
            elif self.key_code[UP] == True:
                if self.y <= HEIGHT - CELLDIM and self.y - CELLDIM >= 0 and maze_type[self.y//CELLDIM - 1][self.x//CELLDIM] == 0  :
                    self.vx = 0
                    self.vy = -30
                    self.d = 1
                        
            elif self.key_code[DOWN] == True:
                if self.y + CELLDIM <= HEIGHT - CELLDIM and self.y >= 0  and maze_type[self.y//CELLDIM + 1][self.x//CELLDIM] == 0:
                    self.vx = 0
                    self.vy = 30
                    self.d = 0
            else:
                self.vx = 0
                self.vy = 0
    
            self.x += self.vx
            self.y += self.vy
        
# defines moevemts of player 2 and inherits methods from 
class PlayerTwo(Characters):
    global maze_type
    def __init__(self, x, y, d, w, h):
        Characters.__init__(self, x, y, d, w, h)
        self.d = d
        self.x = x 
        self.y =  y 
        self.w = w
        self.h = h
        self.key_code = {'A': False, 'D': False, 'W': False, 'S': False} #initialize key codes
    #player 2 moves with A,W,S,D keys, this function sees if movement is possible and if so, self.vy and self.vs increment based on direction and player moves
    def move(self):
            self.vx = 0
            self.vy = 0
    
            if self.key_code['A'] == True:
                if self.x - CELLDIM >= 0 and self.x <= WIDTH - CELLDIM and maze_type[self.y//CELLDIM][self.x//CELLDIM-1] == 0 :
                    self.vx = -30
                    self.vy = 0
                    self.d = 2
                
    
            elif self.key_code['D'] == True:
                if self.x + CELLDIM <= WIDTH - CELLDIM and self.x  >= 0 and maze_type[self.y//CELLDIM][self.x//CELLDIM+1] == 0:
                    self.vx = 30
                    self.vy = 0
                    self.d = 3
            
        
            elif self.key_code['W'] == True:
                if self.y <= HEIGHT - CELLDIM and self.y - CELLDIM >= 0 and maze_type[self.y//CELLDIM - 1][self.x//CELLDIM] == 0  :
                    self.vx = 0
                    self.vy = -30
                    self.d = 1
                        
            
            elif self.key_code['S'] == True:
                if self.y + CELLDIM <= HEIGHT - CELLDIM and self.y >= 0  and maze_type[self.y//CELLDIM + 1][self.x//CELLDIM] == 0:
                    self.vx = 0
                    self.vy = 30
                    self.d = 0
            
            else:
                self.vx = 0
                self.vy = 0
    
    
            self.x += self.vx
            self.y += self.vy
        
#main class, in which all objects are bought together
class Maze:
    def __init__(self):
        global MAZE, MAZE2, x_object, y_object, x_object2, y_object2

        self.game = 1
        
        self.coinlist = []
        self.coinlist2 = []
        
        self.add_coins_to_list()

        for x in range(12):
            rand_int = random.randint(0,len(x_object)-1)
            if x == 0:  
                self.p1 = PlayerOne(x_object[rand_int], y_object[rand_int], 0, 90, 90)
            elif x == 1:  
                self.p2 = PlayerTwo(x_object[rand_int], y_object[rand_int], 0, 90, 90)
            elif x == 2:  
                 self.e = Enemy(x_object[rand_int], y_object[rand_int])
            elif x == 3:  
                self.p1_l2 = PlayerOne(x_object2[rand_int], y_object2[rand_int], 0, 30, 30)
            elif x == 4:  
                self.p2_l2 = PlayerTwo(x_object2[rand_int], y_object2[rand_int], 0, 30, 30)
            elif x == 5:  
                self.e2 = Enemy(x_object2[rand_int], y_object2[rand_int])
            elif x == 6:  
                self.e3 = Enemy(x_object2[rand_int], y_object2[rand_int])
            elif x == 7:  
                self.e4 = Enemy(x_object2[rand_int], y_object2[rand_int])
            elif x == 8:  
                self.e5 = Enemy(x_object2[rand_int], y_object2[rand_int])
            elif x == 9:  
                self.e6 = Enemy(x_object2[rand_int], y_object2[rand_int])
            elif x == 10:  
                self.e6 = Enemy(x_object2[rand_int], y_object2[rand_int])
            elif x == 11:  
                self.bomb = Bomb(x_object2[rand_int], x_object2[rand_int], 3)
                
            del x_object[rand_int]
            del y_object[rand_int]

        self.hk = HealthKit()
        self.hk2 = HealthKit()

        self.gameover = False
        self. winner = ""
        
        self.player1 = self.p1
        self.player2 = self.p2

        self.music = player.loadFile(path + "/data/munni.mp3")
        self.music.loop()
    def add_coins_to_list(self):

        for i in range(3):
            rand_int = random.randint(0,len(x_object)-1)
            x = x_object[rand_int]
            y = y_object[rand_int]
            
            self.coinlist.append(Coins(x, y, 6, 30, 30))
            
    
            del x_object[rand_int]
            del y_object[rand_int]

        for i in range(30):
            rand_int = random.randint(0,len(x_object2)-1)
            x = x_object2[rand_int]
            y = y_object2[rand_int]
            
            self.coinlist2.append(Coins(x, y, 6, 15, 15))
            
    
            del x_object2[rand_int]
            del y_object2[rand_int]
        
        
    def choosewinner(self):
        
        if self.game == 1:
            if  self.p1.health == 0 or self.p2.health == 0:
                if self.p1.health > self.p2.health:
                    self.winner =  "1"
                if self.p2.health > self.p1.health:
                    self.winner = "2"
                    
        if self.game == 2:
            if   (self.coinlist2) == 0 :
            
                if self.p1_l2.score > self.p2_l2.score:
                    self.winner = "1"
                if self.p2_l2.score > self.p1_l2.score:
                    self.winner = "2"
           
            if  self.p1_l2.health == 0 or self.p2_l2.health == 0:
                 
                if self.p1_l2.health > self.p2_l2.health:
                    self.winner =  "1"    
                if self.p2_l2.health > self.p1_l2.health:
                    self.winner = "2"
            
            
    
    def gameovermenu(self):
        self.choosewinner()
        if self.gameover == True:
            background(12, 150, 228)
            fill(255)
            noStroke()
            textSize(500)
            textAlign(CENTER)
            font = loadFont("nj.vlw")
            textFont(font)
            textSize(60)
            text ("GAME OVER", 600, 125)
            textSize(40)
            text ("Player " + str(self.winner) + " wins!", 600, 225)
            textSize(30)
            text("PLayer 1: "+ str(maze.p1.score), 600, 315)
            text("Player 2: " + str(maze.p2.score), 600, 350)
            text("Click anywhere to restart the game", 600, 525)
    
    def ScoreBoard(self):
        
        if self.game == 1:
            player1 = self.p1
            player2 = self.p2
        
        if self.game == 2:                    
            player1 = self.p1_l2
            player2 = self.p2_l2
            
        textSize(20)
        fill(0)
        heart = loadImage(path + "/data/heart.png")
        dollar = loadImage(path + "/data/dollar.png")

        text('Player 1: ', 100, 20)
        image(dollar, 140,-3, 30,30)
        text(str(player1.score), 180, 20)
        for i in range(player1.health):
            image(heart, 200 + i*CELLDIM,-3, 30,30)

        
        text('Player 2: ', 1000, 20)
        image(dollar, 1040,-3, 30,30)
        text(str(player2.score), 1080, 20)
        for i in range(player2.health):
            image(heart, 1100 + i*CELLDIM,-3, 30,30)
                
    
    def update(self):
        if self.game == 1:
            if len(self.coinlist) == 0: 
       
                self.game = 2
                
                            
                self.p1_l2.health = self.p1.health
                self.p2_l2.health = self.p2.health
                self.p1_l2.score = self.p1.score
                self.p2_l2.score = self.p2.score  
            
            elif  self.p1.health == 0 or self.p2.health == 0:
                self.gameover = True
                self.gameovermenu()

            else:
                self.e.display()
                self.p1.display() 
                self.p2.display()
                for coin in self.coinlist:
                    coin.display(coin.x, coin.y)
    
                if self.hk.cnt > 1:
                    self.hk.display()
      
    
                self.ScoreBoard()
                
        if self.game == 2:
            if len(self.coinlist2) == 0 or self.p1_l2.health == 0 or self.p2_l2.health == 0:
                self.gameover = True
                self.gameovermenu()

            else:
                self.e2.display()
                self.e3.display()
                self.e4.display()
                self.e5.display()
                self.e6.display()
                self.p1_l2.display() 
                self.p2_l2.display()
                for coin in self.coinlist2:
                    coin.display(coin.x, coin.y + CELLDIM//2)
    
                if self.hk2.cnt > 1:
                    self.hk2.display()
                    
                self.bomb.update()
    
                self.ScoreBoard()
            

    def display(self):

            drawlines()
            self.update()

maze = Maze()
         
def setup():
    global bg
    size(WIDTH, HEIGHT)
    frameRate(60)

       
def draw():
    if (startgame == False and instructions == False):
        startmenu()
    elif(startgame == False and instructions == True):
        instmenu()
        
    elif(startgame == True and instructions == False):
    
        #slowdown the game by not displaying every frame
    
        if frameCount%10 == 0 or frameCount == 1:
            drawlines()
            maze.display()
                
def instmenu():
    global instructions, startgame
    if keyPressed:
        if key == ENTER:
            instructions = False
            startgame = True   
        
def startmenu():
    global startgame, bg, block, instructions
    if startgame == False:
        background(12, 150, 228)
        fill(255)
        noStroke()
        rect(475, 220, 200, 75)
        rect(475, 350, 200, 75)
        textSize(50)
        textAlign(CENTER)
        font = loadFont("nj.vlw")
        textFont(font)
        text ("GASHTI UNLIMITED", 600, 100)
        textSize(30)
        text ("Select the mode you want to play in:", 600, 160)
        textSize(26)
        text("Collect all coins you can but be aware for", 600, 500)
        textSize(26)
        text("Collect all coins you can but be aware for", 600, 500)
        text("you are not alone in the maze!", 600, 525)
        fill(0)
        textSize(22)
        text("Snow",570,265)
        text("Farm",570,400)
        img1 = loadImage(path + "/data/peng.png")
        image(img1, 410, 167, 160, 160)
        img2 = loadImage(path + "/data/strt.png")
        image(img2, 610, 325, 130, 130)

        if (mousePressed):
            if(mouseX>475 and mouseX<675 and mouseY>220 and mouseY<295):
                #load snow background
                strokeWeight(10)
                stroke(0)
                noFill()
                rect(475, 220, 200, 75)
                block = "block.jpg"
                bg = "ice_bg"
                instructions = True
                instruct = loadImage(path + "/data/menu_ice.jpg")
                image(instruct, 0, 0, WIDTH, HEIGHT)
                maze.e.img = loadImage(path + '/data/ice_enemy.png')
                maze.e2.img = loadImage(path + '/data/ice_enemy.png')
                maze.e3.img = loadImage(path + '/data/ice_enemy.png')
                maze.e4.img = loadImage(path + '/data/ice_enemy.png')
                maze.e5.img = loadImage(path + '/data/ice_enemy.png')
                maze.e6.img = loadImage(path + '/data/ice_enemy.png')
                maze.p1.img = loadImage(path + '/data/red_penguin.png')
                maze.p2.img = loadImage(path + '/data/blue_penguin.png')
                maze.p1_l2.img = loadImage(path + '/data/red_penguin.png')
                maze.p2_l2.img = loadImage(path + '/data/blue_penguin.png')
                
                
            if(mouseX>475 and mouseX<675 and mouseY>350 and mouseY<425):
                #load farm background
                strokeWeight(10)
                stroke(0)
                noFill()
                rect(475, 350, 200, 75)
                block = "grass.png"
                bg = "grass_bg"
                instructions = True
                instruct = loadImage(path + "/data/menu_farm.jpg")
                image(instruct, 0, 0, WIDTH, HEIGHT)
                maze.p1.img = loadImage(path + '/data/cow.png')
                maze.p2.img = loadImage(path + '/data/sheep.png')
                maze.p1_l2.img = loadImage(path + '/data/cow.png')
                maze.p2_l2.img = loadImage(path + '/data/sheep.png')
                maze.e.img = loadImage(path + '/data/farm_enemy.png')
                maze.e2.img = loadImage(path + '/data/farm_enemy.png')
                maze.e3.img = loadImage(path + '/data/farm_enemy.png')
                maze.e4.img = loadImage(path + '/data/farm_enemy.png')
                maze.e5.img = loadImage(path + '/data/farm_enemy.png')
                maze.e6.img = loadImage(path + '/data/farm_enemy.png')
        
        if instructions == True:     
            instmenu()

#draw the maze walls                             
def drawlines():
    global bg, block, maze_type, MAZE, MAZE2
    #load maze walls images
    img_bg = loadImage(path + "/data/" + bg +".jpg")
    background(img_bg)
    img_block = loadImage(path + "/data/" + block)
    #create walls in level 1
    if maze.game == 1:
        maze_type = MAZE
        for j in range(HEIGHT//CELLDIM):
            for i in range(WIDTH//CELLDIM):
                if MAZE[j][i] == 1:
                    image(img_block, i*CELLDIM, j*CELLDIM)
    #create walls in level 2
    if maze.game == 2:
        maze_type = MAZE2
        for j in range(HEIGHT//CELLDIM):
            for i in range(WIDTH//CELLDIM):
                if MAZE2[j][i] == 1:
                    image(img_block, i*CELLDIM, j*CELLDIM)
                    
                    
#define codes for when key os pressed for both players in both levels               
def keyPressed():
    if keyCode == LEFT:
        maze.p1.key_code[LEFT] = True
        maze.p1_l2.key_code[LEFT] = True
    if keyCode == RIGHT:
        maze.p1.key_code[RIGHT] = True
        maze.p1_l2.key_code[RIGHT] = True
    if keyCode == UP:
        maze.p1.key_code[UP] = True
        maze.p1_l2.key_code[UP] = True
    if keyCode == DOWN:
        maze.p1.key_code[DOWN] = True
        maze.p1_l2.key_code[DOWN] = True
    if key == 'A' or key == 'a':
        maze.p2.key_code['A'] = True
        maze.p2_l2.key_code['A'] = True
    if key == 'D' or key == 'd':
        maze.p2.key_code['D'] = True
        maze.p2_l2.key_code['D'] = True
    if key == 'W'or key == 'w':
        maze.p2.key_code['W'] = True
        maze.p2_l2.key_code['W'] = True
    if key == 'S' or key == 's':
        maze.p2.key_code['S'] = True
        maze.p2_l2.key_code['S'] = True
#define codes for when key os pressed for both players in both levels         
def keyReleased():
    if keyCode == LEFT:
        maze.p1.key_code[LEFT] = False
        maze.p1_l2.key_code[LEFT] = False
    if keyCode == RIGHT:
        maze.p1.key_code[RIGHT] = False
        maze.p1_l2.key_code[RIGHT] = False
    if keyCode == UP:
        maze.p1.key_code[UP] = False
        maze.p1_l2.key_code[UP] = False
    if keyCode == DOWN:
        maze.p1.key_code[DOWN] = False
        maze.p1_l2.key_code[DOWN] = False
    if key == 'A' or key == 'a':
        maze.p2.key_code['A'] = False
        maze.p2_l2.key_code['A'] = False
    if key == 'D' or key == 'd':
        maze.p2.key_code['D'] = False
        maze.p2_l2.key_code['D'] = False
    if key == 'W'or key == 'w':
        maze.p2.key_code['W'] = False
        maze.p2_l2.key_code['W'] = False
    if key == 'S' or key == 's':
        maze.p2.key_code['S'] = False
        maze.p2_l2.key_code['S'] = False
        
def mouseClicked():
    global maze
    global startgame
    if maze.gameover == True:
         #redefine starting conditions
        size(WIDTH, HEIGHT)
        x_object = []
        y_object = []

        x_object2 = []
        y_object2 = []
        
        startgame = False
        maze.gameover = False
        
        for j in range(HEIGHT//CELLDIM):
            for i in range(WIDTH//CELLDIM):
                if MAZE[j][i] == 0:
                    y_object.append(j*CELLDIM)
                    x_object.append(i*CELLDIM)

        for j in range(HEIGHT//CELLDIM):
            for i in range(WIDTH//CELLDIM):
                if MAZE2[j][i] == 0:
                    y_object2.append(j*CELLDIM)
                    x_object2.append(i*CELLDIM)
        
        neighbors = [[1,0], [0,1], [0,-1], [-1,0]]
        maze = Maze() #class for coins, ther will bw 21 coins in level 1 and 30 in level 2
