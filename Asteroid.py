import pygame
import random
# Imports pygame, which is the gui, and the random function
pygame.init()

win = pygame.display.set_mode((500, 500))
timer = pygame.time.Clock()
pygame.display.set_caption("My Game")
myFont = pygame.font.SysFont('Arial', 30)
x = 20
y = 250
width = 20
height = 20
thickness = 0
vel = 1
run = True
gameOver = True
color = (255, 255, 255)
shape = "Player"
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#dir = "U"
key = False
frame_count = 0
frame_rate = 60
start_time = 90
timeCounter= 0
HighScore = 0
win.fill(WHITE)

# --- Timer going up ---
# Calculate total seconds
total_seconds = frame_count // frame_rate

# Divide by 60 to get total minutes
minutes = total_seconds // 60

# Use modulus (remainder) to get seconds
seconds = total_seconds % 60

# Use python string formatting to format in leading zeros
output_string = " {0:02}:{1:02}".format(minutes, seconds)

# Blit to the screen
text = myFont.render(output_string, True, BLACK)
win.blit(text, [250, 250])

# --- Timer going up ---
frame_count = frame_count + 1

# Limit frames per second
timer.tick(frame_rate)
pygame.display.flip()

class Player(object):
    #Class that defines the player and its hitbox

   def __init__(self, x, y , width, height, color):
       self.x = x
       self.y = y
       self.width = width
       self.height = height
       self.color = color
       self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        # Players physical features defined

   def draw(self):
       pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
       pygame.draw.rect(win, (0, 0, 0), (self.hitbox.x, self.hitbox.y, 20, 20), 1)

   def updateHitBox(self):
       self.hitbox.x = self.x
       self.hitbox.y = self.y
#Players hitbox defined

   def checkCollision(self, otherRect):
       return self.hitbox.colliderect(otherRect)
#Players collision defined

class Wall(object):
#Class that defines the wall, which is what the Asteroid is made of
   def __init__(self, x, y, width, height, color,):
       self.x = x
       self.y = y
       self.width = width
       self.height = height
       self.color = color
       self.dir = "U"
       self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
#Defines the physical features for the wall (Asteroid)
   def hitbox(self):
       pygame.draw.rect(win, (0, 0, 0), (self.hitbox.x, self.hitbox.y, 20, 20), 1)
   def draw(self):
       pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
       pygame.draw.rect(win, (255, 255, 255), (self.hitbox.x, self.hitbox.y, self.hitbox.width, self.hitbox.height), 1)
#
   def undraw(self):
       pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), 0)

   def updateHitBox(self):
       self.hitbox.x = self.x
       self.hitbox.y = self.y

#Function that allows the user to control the players movement
def userInput():
   global vel
   keys = pygame.key.get_pressed()
   if keys[pygame.K_LEFT]: #and x > vel:
       player.x -= 60 * (0.06)
       player.hitbox.x = player.x
   if keys[pygame.K_RIGHT]:#and x < 500:
       player.x += 60 * (0.06)
       player.hitbox.x = player.x
   if keys[pygame.K_UP]:  # and y > vel:
       player.y -= 60 * (0.06)
       player.hitbox.y = player.y
   if keys[pygame.K_DOWN]:  # and y < 500 - thickness - vel:
       player.y += 60 * (0.06)
       player.hitbox.y = player.y

player = Player(235, 420, 20, 20, (45, 45, 255))
Asteroid = [] #List for the first asteroid, second asteroid, etc....
Asteroid2 = []
Asteroid3 = []
Asteroid4 = []
Asteroid5 = []
RandomX = random.randint(10,500) #Random position for first asteroid, second asteroid, etc....
RandomX2 = random.randint(10,500)
RandomX3 = random.randint(10,500)
RandomX4 = random.randint(10,500)
RandomX5 = random.randint(10,500)
Asteroid.append(Wall(RandomX, 60, 13, 13, RED))#Draws the asteroid and its dimensions....
Asteroid2.append(Wall(RandomX2, 60, 22, 22, RED))
Asteroid3.append(Wall(RandomX3, 60, 10, 10, RED))
Asteroid4.append(Wall(RandomX4, 60, 17, 17, RED))
Asteroid5.append(Wall(RandomX5, 60, 12,12, RED))

#While loop that allows the timer to work
while run:
   pygame.time.delay(10)
   timeCounter+=0.01
   for event in pygame.event.get():  # this gets a list of all the events in pygame
       if event.type == pygame.QUIT: # this checks if you hit the big red button on the game window
           run = False
   userInput()
   win.fill((0, 0, 0))
   player.draw()
   player.updateHitBox()
# For loops that define the speed of each asteroid
   for w in Asteroid:
       w.y+=40*(0.04)
       w.draw()
       w.updateHitBox()
   if w.y >= 450:
       w.y = 60
       w.x = random.randint(10, 500)
   for w2 in Asteroid2:
       w2.y += 30 * (0.03)
       w2.draw()
       w2.updateHitBox()
   if w2.y >= 450:
       w2.y = 60
       w2.x = random.randint(10, 500)
   for w3 in Asteroid3:
       w3.y += 90 * (0.09)
       w3.draw()
       w3.updateHitBox()
   if w3.y >= 450:
       w3.y = 60
       w3.x = random.randint(10, 500)
   for w4 in Asteroid4:
       w4.y += 60 * (0.06)
       w4.draw()
       w4.updateHitBox()
   if w4.y >= 450:
       w4.y = 60
       w4.x = random.randint(10, 500)
   for w5 in Asteroid5:
       w5.y += 25 * (0.25)
       w5.draw()
       w5.updateHitBox()
   if w5.y >= 450:
       w5.y = 60
       w5.x = random.randint(10, 500)
    #If statements that define the boundaries of the game
   if player.x >= 500:
        player.x = 235
        player.y = 420
   if player.x <= 0:
        player.x = 235
        player.y = 420
   if player.y >= 465:
        player.x = 235
        player.y = 420
   if player.y <= 125:
       player.x = 235
       player.y = 420

   # For loops that define the High Score
   for w in Asteroid:
       hit = player.checkCollision(w.hitbox)
       if hit:
           player.x = 235
           player.y = 420
           if HighScore < timeCounter:
               HighScore = timeCounter
           else:
               HighScore != timeCounter
           timeCounter = timeCounter - timeCounter

   for w2 in Asteroid2:
       hit = player.checkCollision(w2.hitbox)
       if hit:
           player.x = 235
           player.y = 420
           if HighScore < timeCounter:
               HighScore = timeCounter
           else:
               HighScore != timeCounter
           timeCounter = timeCounter - timeCounter

   for w3 in Asteroid3:
       hit = player.checkCollision(w3.hitbox)
       if hit:
           player.x = 235
           player.y = 420
           if HighScore < timeCounter:
               HighScore = timeCounter
           else:
               HighScore != timeCounter
           timeCounter = timeCounter - timeCounter

   for w4 in Asteroid4:
       hit = player.checkCollision(w4.hitbox)
       if hit:
           player.x = 235
           player.y = 420
           if HighScore < timeCounter:
               HighScore = timeCounter
           else:
               HighScore != timeCounter
           timeCounter = timeCounter - timeCounter

   for w5 in Asteroid5:
       hit = player.checkCollision(w5.hitbox)
       if hit:
           player.x = 235
           player.y = 420
           if HighScore < timeCounter:
               HighScore = timeCounter
           else:
               HighScore != timeCounter
           timeCounter = timeCounter - timeCounter






# Add the texts on the top left of the screen
   textSurface1 = myFont.render("Score:", False, (255, 255, 255))
   textSurface2 = myFont.render("High Score: ", False, (255, 255, 255))
   textSurface4 = myFont.render(str(((HighScore * 100) // 1) / 100), False, (255, 255, 255))
   textSurface3 = myFont.render(str(((timeCounter*100)//1)/100), False, (255, 255, 255))
   win.blit(textSurface1, (40, 20))
   win.blit(textSurface2, (40, 60))
   win.blit(textSurface3, (130, 20))
   win.blit(textSurface4, (210, 60))
   #if player.x >= 200:
       #cheatWall.undraw()
   #else:
       #cheatWall.draw()

   pygame.display.flip()