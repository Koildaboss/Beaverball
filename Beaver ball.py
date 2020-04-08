import pygame
pygame.init()
print("Welcome to Beaver Ball")
win = pygame.display.set_mode((500, 480))#, pygame.FULLSCREEN)

pygame.display.set_caption("Beaver Ball")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

class player (object):
    def __init__(self, x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isjump = False
        self.jumpcount = 10
        self.left = False
        self.right = False
        self.walkcount = 0
        self.standing = True
        
    def draw(self,win):
            if self.walkcount + 1 >= 27:
                self.walkcount = 0

            if not(self.standing):
                
                if self.left:
                    win.blit(walkLeft[self.walkcount//3], (self.x,self.y))
                    self.walkcount += 1
                    
                elif self.right:
                    win.blit(walkRight[self.walkcount//3],(self.x,self.y))
                    self.walkcount += 1
                
            else:
                if self.right:
                    win.blit(walkRight[0],(self.x, self.y))    
                else:
                    win.blit(walkLeft[0],(self.x,self.y))

class projectile (object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color,(self.x,self.y),self.radius)
        


def redrawgamewindow():
    global walkcount
    win.blit(bg,(0,0))
    beaverbill.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()



#mainloop
beaverbill = player (300,410,64,64)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            run = False
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    

    if keys[pygame.K_SPACE]:

        if beaverbill.left:
            facing = -1

        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(projectile(round (beaverbill.x + beaverbill.width //2), round(beaverbill.y + beaverbill.height//2), 6, (0,255,255), facing))
                

    if keys[pygame.K_LEFT] and beaverbill.x > beaverbill.vel:
        beaverbill.x -= beaverbill.vel
        beaverbill.left = True
        beaverbill.right = False
        beaverbill.standing = False
    
    elif keys[pygame.K_RIGHT] and beaverbill.x < 500 - beaverbill.width - beaverbill.vel:
        beaverbill.x += beaverbill.vel
        beaverbill.right = True
        beaverbill.left = False
        beaverbill.standing = False

    else:
        beaverbill.standing = True
        beaverbill.walkcount = 0


    if not (beaverbill.isjump):

        if keys[pygame.K_UP]:
            beaverbill.isjump = True
            beaverbill.right = False
            beaverbill.left = False
            beaverbill.walkcount = 0
    else:
        if beaverbill.jumpcount >= -10:
            neg = 1
            if beaverbill.jumpcount < 0:
                neg = -1
            beaverbill.y -= (beaverbill.jumpcount** 2) * 0.5 * neg
            beaverbill.jumpcount -= 1

        else:
            beaverbill.isjump = False
            beaverbill.jumpcount = 10
    redrawgamewindow()



pygame.quit()

