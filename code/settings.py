#game setup
WIDTH    = 1280	#could be adjusted
HEIGTH   = 720
FPS      = 60 #recomend not to change
TILESIZE = 64

#ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

#colors
UI_BG_COLOR = '#222222'
UI_BG_COLOR_ACTIVE = '#450C0C'
UI_BORDER_COLOR = '#FF9E14' #F59F27'
UI_BORDER_COLOR_ACTIVE = 'white'
TEXT_COLOR = '#EEEEEE'
WATER_COLOR = '#71ddee'
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'

HEALH_T_DECREASE_AMOUNT = 0.2

#weapons
weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15,'graphic':'../graphics/weapons/sword/full.png'},
	'lance': {'cooldown': 400, 'damage': 30,'graphic':'../graphics/weapons/lance/full.png'},
	'axe': {'cooldown': 300, 'damage': 20, 'graphic':'../graphics/weapons/axe/full.png'},
	'rapier':{'cooldown': 50, 'damage': 8, 'graphic':'../graphics/weapons/rapier/full.png'},
	'sai':{'cooldown': 80, 'damage': 10, 'graphic':'../graphics/weapons/sai/full.png'}}