import pygame
import random
import math,time

# 初始化界面
pygame.init()
screen = pygame.display.set_mode((800,600 ),flags=pygame.FULLSCREEN)  #800 * 600
pygame.display.set_caption("打飞机")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
bgImg = pygame.image.load("bg.png")

#添加背景音效
pygame.mixer_music.load('bg.wav')
pygame.mixer_music.play(-1)  #单曲循环

#添加射中音效
bao_sound = pygame.mixer.Sound('exp.wav')

# 飞机
playerImg = pygame.image.load("player.png" )
playerX = 400  #飞机X坐标
playerY = 550  # 飞机Y坐标
playerStep = 0  #玩家移动的速度

#分数
score = 0
Running = True

font = pygame.font.Font('mytest.ttf',32)
def show_score():
    text = f"分数：{score}"
    score_render = font.render(text,True,(0,255,0))
    screen.blit(score_render,(10,10))

time_font = pygame.font.Font('mytest.ttf',32)
def show_time():
    text = f"时间：{time.strftime('%H:%M:%S')}"
    score_render = time_font.render(text,True,(255,255,255))
    screen.blit(score_render,(500,550))



# 游戏结束
is_over = False
over_font = pygame.font.Font('mytest.ttf',64)
over1_font = pygame.font.Font('mytest.ttf',32)
over2_font = pygame.font.Font('mytest.ttf',32)
def check_is_score():
    if is_over:
        if score>=50:
            win_text = f"您赢了，真厉害"
            score1_render = over1_font.render(win_text, True, (255, 0, 0))
            screen.blit(score1_render, (300, 150))
        else:
            lose_text = f"您输了，请继续努力"
            score2_render = over2_font.render(lose_text, True, (255, 0, 0))
            screen.blit(score2_render, (300, 150))
        text = f"Game Over"
        score_render = over_font.render(text,True,(255,0,0))
        screen.blit(score_render,(300,250))


#敌人类
number_of_enemies = 10
class Enemy():
    def __init__(self):
        self.img = pygame.image.load("1.png")
        self.x = random.randint(200,600)
        self.y = random.randint(50,250)
        self.step = random.randint(2,4)
    #当被射中时 恢复位置
    def reset(self):
        global score
        score += 1
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 150)
enemies = []  #保存所有的敌人
for i in range(number_of_enemies):
    enemies.append(Enemy())

#两个点之间的距离
def distance(bx,by,ex,ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a*a+b*b)


# 子弹类
class Bullet():
    def __init__(self):
        self.img = pygame.image.load("2.png")
        self.x = playerX + 16 #(64-32)/2
        self.y = playerY + 10
        self.step = 10
    #击中
    def hit(self):
        for e in enemies:
            if(distance(self.x,self.y,e.x,e.y)<30):
                bao_sound.play()
                #射中敌人
                try:
                    bullets.remove(self)
                except:
                    pass
                e.reset()

bullets = [] #保存现有子弹

def show_bullets():
    for b in bullets:
        screen.blit(b.img,(b.x,b.y))
        b.hit() #是否击中敌人
        b.y -= b.step  #移动子弹
        if b.y <0:
            bullets.remove(b)
#显示敌人，实现敌人的移动
def show_enemy():
    global is_over
    for e in enemies:
        screen.blit(e.img,(e.x,e.y))
        e.x += e.step
        if(e.x > 736 or e.x <0):
            e.step *= -1
            e.y +=  40
            if e.y >500 or score>49:
                is_over = True
                enemies.clear()


def process_events():
    global playerStep,Running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        #通过键盘事件控制飞机的移动
        if event.type == pygame.KEYDOWN:  #按下就移动
            if event.key == pygame.K_RIGHT:
                playerStep = 5
            elif event.key == pygame.K_LEFT:
                playerStep = -5
            elif event.key == pygame.K_SPACE:
                bullets.append(Bullet())
            if event.type == pygame.KEYUP: #抬起来就不
                playerStep = 0



def move_player():
    global playerX
    playerX += playerStep
    if playerX > 736:
        playerX = 736
    if playerX < 0:
        playerX = 0

#游戏主循环
while Running:
    screen.blit(bgImg,(0,0))
    show_score() #显示分数
    process_events()  #处理事件
    screen.blit(playerImg, (playerX, playerY))
    move_player() #移动玩家
    show_enemy()  #显示敌人
    show_bullets() #显示子弹
    check_is_score()# 显示分数
    show_time() #显示时间

    pygame.display.update()