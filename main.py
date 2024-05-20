import pygame
from pygame.math import Vector2 as vector
from settings import *
from support import*

from pygame.image import load

from editor import Editor
from level import Level

from os import walk

class Main:
    def __init__(self):
        pygame.init()
        #创建显示表面
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        #创建时钟,控制游戏循环帧率
        self.clock = pygame.time.Clock()
        #导入游戏模块资源
        self.imports()
        #创建编辑器活动
        self.editor_active= True
        self.transition = Transition(self.toggle)
        self.editor = Editor(self.land_tiles,self.switch)

        #光标
        surf = load('../pythonProject/cursor/鼠标.png').convert_alpha()
        cursor = pygame.cursors.Cursor((0,0),surf)
        pygame.mouse.set_cursor(cursor)

    def imports(self):
        #地形
        self.land_tiles = import_folder_dict('../pythonProject/graphics/terrain/land')
        #导入一个water tile
        self.water_bottom = load('../pythonProject/graphics/terrain/water/water_bottom.png').convert_alpha()
        self.water_top_animation = import_folder('../pythonProject/graphics/terrain/water/animation')
        #硬币
        self.gold = import_folder('../pythonProject/graphics/items/gold')
        self.silver = import_folder('../pythonProject/graphics/items/silver')
        self.diamond = import_folder('../pythonProject/graphics/items/diamond')
        self.particle = import_folder('../pythonProject/graphics/items/particle')

        #others
        self.others = {folder: import_folder(f'../pythonProject/graphics/terrain/other/{folder}')for folder in list(walk('../pythonProject/graphics/terrain/other'))[0][1]}
        print(self.others)

        # 敌人
        self.spikes = load('../pythonProject/graphics/enemies/spikes/spikes.png').convert_alpha()
        self.slim = {folder: import_folder(f'../pythonProject/graphics/enemies/slim/{folder}')for folder in list(walk('../pythonProject/graphics/enemies/slim'))[0][1]}
        self.shell = {folder: import_folder(f'../pythonProject/graphics/enemies/shell_right/{folder}')for folder in list(walk('../pythonProject/graphics/enemies/shell_right'))[0][1]}
        self.bullet = load('../pythonProject/graphics/enemies/pearl/pearl.png').convert_alpha()

        #玩家
        self.player_graphics = {folder: import_folder(f'../pythonProject/graphics/player/{folder}')for folder in list(walk('../pythonProject/graphics/player'))[0][1]}
        print(self.player_graphics)

        #云朵
        self.clouds = import_folder('../pythonProject/graphics/clouds')

        # 游戏音乐
        self.level_sounds = {
            'coin': pygame.mixer.Sound('../pythonProject/audio/coin.wav'),
            'hit': pygame.mixer.Sound('../pythonProject/audio/hit.wav'),
            'jump': pygame.mixer.Sound('../pythonProject/audio/jump.wav'),
            'music': pygame.mixer.Sound('../pythonProject/audio/SuperHero.ogg'),
        }

    #切换编辑器状态
    def toggle(self):
        self.editor_active = not self.editor_active
        if self.editor_active:
            self.editor.editor_music.play()

    #关卡切换
    def switch(self,grid = None):
        self.transition.active=True
        if grid:
            self.level = Level(grid,self.switch,{
                'land':self.land_tiles,
                'water bottom':self.water_bottom,
                'water top':self.water_top_animation,
                'gold':self.gold,
                'silver':self.silver,
                'diamond':self.diamond,
                'particle':self.particle,
                'others':self.others,
                'spikes':self.spikes,
                'slim':self.slim,
                'shell':self.shell,
                'player':self.player_graphics,
                'bullet':self.bullet,
                'clouds':self.clouds},
            self.level_sounds
                               )

    def run(self):
        while True:
                dt = self.clock.tick() / 1000

                #实现编辑器和关卡切换
                if self.editor_active:
                    self.editor.run(dt)
                else:
                    self.level.run(dt)
                self.transition.display(dt)
                #画坐标系
                pygame.display.update()
#过渡动画
class Transition():
    def __init__(self,toggle):
        self.display_surface =pygame.display.get_surface()
        self.toggle = toggle
        self.active = False

        self.border_width = 0
        self.direction =1
        self.center =(WINDOW_WIDTH/2,WINDOW_HEIGHT/2)
        self.radius = vector(self.center).magnitude()
        self.threshold = self.radius+100

    def display(self,dt):
        if self.active:
            self.border_width += 1000 *dt *self.direction
            #反方向动画
            if self.border_width>=self.threshold:
                self.direction = -1
                self.toggle()
            if self.border_width<0:
                self.active =False
                self.border_width=0
                self.direction =1
            pygame.draw.circle(self.display_surface,'black',self.center,self.radius,int(self.border_width))

if __name__ == '__main__':
    main =Main()
    main.run()