import sys
import pygame
from pygame.math import Vector2 as vector

from settings import *
from support import *

from sprites import Generic,Block,Animated,Particle,Coin,Player,Spikes,Slim,Shell,Cloud

from random import choice,randint
class Level:
    def __init__(self,grid,switch,asset_dict,audio):
        self.display_surface = pygame.display.get_surface()
        self.switch =switch

        #groups
        self.all_sprites = CameraGroup()
        self.coin_sprites = pygame.sprite.Group()
        self.damage_sprites = pygame.sprite.Group()
        self.collision_sprites =pygame.sprite.Group()
        self.shell_sprites = pygame.sprite.Group()

        self.build_level(grid,asset_dict,audio['jump'])

        #关卡 限制
        self.level_limits={
            'left' :-WINDOW_WIDTH,
            'right':sorted(list(grid['terrain'].keys()), key = lambda pos:pos[0])[-1][0]+500
        }

        #附加粒子
        self.particle_surfs = asset_dict['particle']

        self.cloud_surfs = asset_dict['clouds']
        self.cloud_timer = pygame.USEREVENT+2
        pygame.time.set_timer(self.cloud_timer,2000)
        self.startup_clouds()

        #声音
        self.bg_music = audio['music']
        self.bg_music.set_volume(0.2)
        self.bg_music.play(loops=-1)

        self.coin_sound = audio['coin']
        self.coin_sound.set_volume(0.3)

        self.hit_sound = audio['hit']
        self.hit_sound.set_volume(0.3)

    def build_level(self,grid,assets_dict,jump_sound):
        for layer_name,layer in grid.items():
            for pos,data in layer.items():
                if layer_name == 'terrain':
                    Generic(pos,assets_dict['land'][data],[self.all_sprites,self.collision_sprites])
                if layer_name == 'water':
                    if data =='top':
                        #animated sprite
                        Animated(assets_dict['water top'],pos,self.all_sprites,LEVEL_LAYERS['water'])
                    else:
                        Generic(pos,assets_dict['water bottom'],self.all_sprites,LEVEL_LAYERS['water'])

                print(f"Layer: {layer_name}, Position: {pos}, Data: {data}")
                match data:
                    # 玩家
                    case 0:self.player = Player(pos,assets_dict['player'],self.all_sprites,self.collision_sprites,jump_sound)
                    case 1:
                        self.horizon_y=pos[1]
                        self.all_sprites.horizon_y=pos[1]
                    #硬币
                    case 4:Coin('gold',assets_dict['gold'],pos,[self.all_sprites,self.coin_sprites])
                    case 5:Coin('silver',assets_dict['silver'],pos,[self.all_sprites,self.coin_sprites])
                    case 6:Coin('diamond',assets_dict['diamond'],pos,[self.all_sprites,self.coin_sprites])
                    #敌人
                    case 7:Spikes(assets_dict['spikes'],pos,[self.all_sprites,self.damage_sprites])
                    case 8:Slim(assets_dict['slim'],pos,[self.all_sprites,self.damage_sprites],self.collision_sprites)
                    case 9:Shell(orientation='left',
                                 assets=assets_dict['shell'],
                                 pos=pos,
                                 group=[self.all_sprites,self.collision_sprites,self.shell_sprites],
                                 bullet_surf=assets_dict['bullet'],
                                 damage_sprites=self.damage_sprites)
                    case 10:Shell(orientation='right',
                                  assets=assets_dict['shell'],
                                  pos=pos,
                                  group=[self.all_sprites,self.collision_sprites,self.shell_sprites],
                                  bullet_surf=assets_dict['bullet'],
                                  damage_sprites=self.damage_sprites)

                    # others
                    case 11:Animated(assets_dict['others']['tree2_fg'], pos, self.all_sprites,LEVEL_LAYERS['bg'])
                    case 12:Animated(assets_dict['others']['tree1_fg'], pos, self.all_sprites,LEVEL_LAYERS['bg'])
                    case 13:Animated(assets_dict['others']['lamb_fg'], pos, self.all_sprites,LEVEL_LAYERS['bg'])
                    case 14:Animated(assets_dict['others']['pillar_fg'], pos, self.all_sprites,LEVEL_LAYERS['bg'])
                    case 15:Animated(assets_dict['others']['tree2_bg'], pos, self.all_sprites,LEVEL_LAYERS['bg'])
                    case 16:Animated(assets_dict['others']['tree1_bg'], pos, self.all_sprites,LEVEL_LAYERS['bg'])
                    case 17:Animated(assets_dict['others']['lamb_bg'], pos, self.all_sprites,LEVEL_LAYERS['bg'])
                    case 18:Animated(assets_dict['others']['pillar_bg'], pos, self.all_sprites,LEVEL_LAYERS['bg'])
            #获取瞄准player位置
        for sprite in self.shell_sprites:
            sprite.player = self.player
    def get_coins(self):
        collided_coins = pygame.sprite.spritecollide(self.player,self.coin_sprites,True)
        for sprite in collided_coins:
            self.coin_sound.play()
            Particle(self.particle_surfs,sprite.rect.center,self.all_sprites)

    def get_damage(self):
        collection_sprites = pygame.sprite.spritecollide(self.player,self.damage_sprites,False,pygame.sprite.collide_mask)
        if collection_sprites:
            self.hit_sound.play()
            self.player.damage()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #按下Esc键退回编辑器
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.switch()
                self.bg_music.stop()

                if event.type == self.cloud_timer:
                    surf = choice(self.cloud_surfs)
                    surf = pygame.transform.scale2x(surf) if randint(0,5)>3 else surf
                    x = self.level_limits['right'] + randint(100,300)
                    y = self.horizon_y-randint(100, 500)
                    Cloud((x,y),surf,self.all_sprites)

    def startup_clouds(self):
        for i in range(40):
            surf = choice(self.cloud_surfs)
            surf = pygame.transform.scale2x(surf) if randint(0, 5) > 3 else surf
            x = randint(self.level_limits['left'], self.level_limits['right'])
            y = self.horizon_y - randint(-50, 600)
            Cloud((x, y), surf, self.all_sprites, self.level_limits['left'])

    def run(self,dt):
        #update
        self.event_loop()
        self.all_sprites.update(dt)
        self.get_coins()
        self.get_damage()

        #drawing

        self.display_surface.fill(SKY_COLOR)
        #self.all_sprites.draw(self.display_surface)
        self.all_sprites.custom_draw(self.player)
        #pygame.draw.rect(self.display_surface,'yellow',self.player.hitbox)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = vector()
        self.horizon_image = pygame.image.load('../pythonProject/cursor/背景.jpg').convert()
        self.horizon_image_rect = self.horizon_image.get_rect()

    def draw_horizon(self):
        horizon_pos = self.horizon_y - self.offset.y

        if horizon_pos < WINDOW_HEIGHT:
            sea_rect = pygame.Rect(0, horizon_pos, WINDOW_WIDTH, WINDOW_HEIGHT - horizon_pos)
            # 裁剪图像以适应绘制区域
            cropped_horizon_image = self.horizon_image.subsurface(sea_rect)
            self.display_surface.blit(cropped_horizon_image, (0, horizon_pos))

            #地平线
            horizon_rect1 = pygame.Rect(0, horizon_pos - 10, WINDOW_WIDTH, 10)
            horizon_rect2 = pygame.Rect(0, horizon_pos - 16, WINDOW_WIDTH, 4)
            horizon_rect3 = pygame.Rect(0, horizon_pos - 20, WINDOW_WIDTH, 2)
            pygame.draw.rect(self.display_surface, HORIZON_TOP_COLOR, horizon_rect1)
            pygame.draw.rect(self.display_surface, HORIZON_TOP_COLOR, horizon_rect2)
            pygame.draw.rect(self.display_surface, HORIZON_TOP_COLOR, horizon_rect3)
            pygame.draw.line(self.display_surface,HORIZON_COLOR,(0,horizon_pos),(WINDOW_WIDTH,horizon_pos),3)


    def custom_draw(self,player):
        self.offset.x = player.rect.centerx-WINDOW_WIDTH/2
        self.offset.y = player.rect.centery-WINDOW_HEIGHT/2

        for sprite in self:
            if sprite.z == LEVEL_LAYERS['clouds']:
                offset_rect = sprite.rect.copy()
                offset_rect.center -= self.offset
                self.display_surface.blit(sprite.image, offset_rect)

        self.draw_horizon()
        for sprite in self:
            for layer in LEVEL_LAYERS.values():
                if sprite.z == layer and sprite.z != LEVEL_LAYERS['clouds']:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image,offset_rect)