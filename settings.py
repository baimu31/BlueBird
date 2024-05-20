# general set up
TILE_SIZE=64
WINDOW_WIDTH =1280
WINDOW_HEIGHT=720
ANIMATION_SPEED=6
#colors
SKY_COLOR='#95ACA6'
HORIZON_TOP_COLOR = '#A2BCAF'
HORIZON_COLOR = '#323226'
LINE_COLOR='black'
BUTTON_BG_COLOR = '#33323d'
BUTTON_LINE_COLOR = '#f5f1de'
EDITOR_DATA ={
    0: {'style': 'player', 'type': 'object', 'menu': None, 'menu_surf': None, 'preview': None,
        'graphics': '../pythonProject/graphics/player/idle_right'},
    1: {'style': 'sky', 'type': 'object', 'menu': None, 'menu_surf': None, 'preview': None, 'graphics': None},

    2: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'menu_surf': '../pythonProject/graphics/menu/land.png',
        'preview': '../pythonProject/graphics/preview/land.png', 'graphics': None},
    3: {'style': 'water', 'type': 'tile', 'menu': 'terrain', 'menu_surf': '../pythonProject/graphics/menu/water.png',
        'preview': '../pythonProject/graphics/preview/water.png', 'graphics': '../pythonProject/graphics/terrain/water/animation'},

    4: {'style': 'coin', 'type': 'tile', 'menu': 'coin', 'menu_surf': '../pythonProject/graphics/menu/gold.png',
        'preview': '../pythonProject/graphics/preview/gold.png', 'graphics': '../pythonProject/graphics/items/gold'},
    5: {'style': 'coin', 'type': 'tile', 'menu': 'coin', 'menu_surf': '../pythonProject/graphics/menu/silver.png',
        'preview': '../pythonProject/graphics/preview/silver.png', 'graphics': '../pythonProject/graphics/items/silver'},
    6: {'style': 'coin', 'type': 'tile', 'menu': 'coin', 'menu_surf': '../pythonProject/graphics/menu/diamond.png',
        'preview': '../pythonProject/graphics/preview/diamond.png', 'graphics': '../pythonProject/graphics/items/diamond'},

    7: {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': '../pythonProject/graphics/menu/spikes.png',
        'preview': '../pythonProject/graphics/preview/spikes.png', 'graphics': '../pythonProject/graphics/enemies/spikes'},
    8: {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': '../pythonProject/graphics/menu/slim.png',
        'preview': '../pythonProject/graphics/preview/slim.png', 'graphics': '../pythonProject/graphics/enemies/slim/idle'},
    9: {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': '../pythonProject/graphics/menu/shell_left.png',
        'preview': '../pythonProject/graphics/preview/shell_left.png', 'graphics': '../pythonProject/graphics/enemies/shell_left/idle'},
    10: {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': '../pythonProject/graphics/menu/shell_right.png',
         'preview': '../pythonProject/graphics/preview/shell_right.png', 'graphics': '../pythonProject/graphics/enemies/shell_right/idle'},

    11: {'style': 'others_fg', 'type': 'object', 'menu': 'others fg', 'menu_surf': '../pythonProject/graphics/menu/tree2_fg.png',
         'preview': '../pythonProject/graphics/preview/tree2_fg.png', 'graphics': '../pythonProject/graphics/terrain/other/tree2_fg'},
    12: {'style': 'others_fg', 'type': 'object', 'menu': 'others fg', 'menu_surf': '../pythonProject/graphics/menu/tree1_fg.png',
         'preview': '../pythonProject/graphics/preview/tree1_fg.png', 'graphics': '../pythonProject/graphics/terrain/other/tree1_fg'},
    13: {'style': 'others_fg', 'type': 'object', 'menu': 'others fg', 'menu_surf': '../pythonProject/graphics/menu/lamb_fg.png',
         'preview': '../pythonProject/graphics/preview/lamb_fg.png', 'graphics': '../pythonProject/graphics/terrain/other/lamb_fg'},
    14: {'style': 'others_fg', 'type': 'object', 'menu': 'others fg', 'menu_surf': '../pythonProject/graphics/menu/pillar_fg.png',
         'preview': '../pythonProject/graphics/preview/pillar_fg.png', 'graphics': '../pythonProject/graphics/terrain/other/pillar_fg'},

    15: {'style': 'others_bg', 'type': 'object', 'menu': 'others bg', 'menu_surf': '../pythonProject/graphics/menu/tree2_bg.png',
         'preview': '../pythonProject/graphics/preview/tree2_bg.png', 'graphics': '../pythonProject/graphics/terrain/other/tree2_bg'},
    16: {'style': 'others_bg', 'type': 'object', 'menu': 'others bg', 'menu_surf': '../pythonProject/graphics/menu/tree1_bg.png',
         'preview': '../pythonProject/graphics/preview/tree1_bg.png', 'graphics': '../pythonProject/graphics/terrain/other/tree1_bg'},
    17: {'style': 'others_bg', 'type': 'object', 'menu': 'others bg', 'menu_surf': '../pythonProject/graphics/menu/lamb_bg.png',
         'preview': '../pythonProject/graphics/preview/lamb_bg.png', 'graphics': '../pythonProject/graphics/terrain/other/lamb_bg'},
    18: {'style': 'others_bg', 'type': 'object', 'menu': 'others bg', 'menu_surf': '../pythonProject/graphics/menu/pillar_bg.png',
         'preview': '../pythonProject/graphics/preview/pillar_bg.png', 'graphics': '../pythonProject/graphics/terrain/other/pillar_bg'},
}

NEIGHBOR_DIRECTIONS = {
    'A': (0,-1),
    'B': (1,-1),
	'C': (1,0),
	'D': (1,1),
	'E': (0,1),
	'F': (-1,1),
	'G': (-1,0),
	'H': (-1,-1)
}
LEVEL_LAYERS ={
    'clouds':1,
    'ocean':2,
    'bg':3,
    'water':4,
    'main':5
}