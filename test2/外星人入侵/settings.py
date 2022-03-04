class Settings():
    #存储游戏所有设置的类
    def __init__(self):
        #初始化游戏设置
        #屏幕设置
        self.screen_width=900
        self.screen_height=700
        self.bg_color=(193,210,240)
        #飞船的设置
        self.ship_speed_factor=1.5

        #子弹设置
        self.bullet_speed_factor=1
        self.bullet_width=15
        self.bullet_height=35
        self.bullet_color=60,60,60
        self.bullets_allowed=3