import pyautogui as pg

from model import Pos, Move, Location, SunLocation, MoonLocation, Thing, WingLocation
from util import logcall

@logcall
def place_window(window_title):
    """Find the window, raise it, size it and move it"""
    browser_window: pg.Window
    [browser_window] = pg.getWindowsWithTitle(window_title)
    browser_window.moveTo(-8, -8)
    browser_window.resizeTo(newWidth=875, newHeight=710)
    browser_window.activate()

# Base position
center = Pos(410, 380)
pos_reload = Pos(87, 60)
pos_three = Pos(192, 122)
pos_four = Pos(264, 122)
pos_exclamation = Pos(336, 122)
pos_end = Pos(408, 122)
pos_trixie_square = Pos(415, 330)
pos_inventory = Pos(800, 119)
pos_next = Pos(728, 645)
pos_muffin = Pos(134, 482)
pos_agree = Pos(248, 661)
pos_accept = Pos(577, 661)
pos_inventory_yes = Pos(248, 630)
pos_inventory_no = Pos(577, 630)
pos_forward = Pos(412, 485)
back = Pos(413, 641)
low_left = Pos(56, 641)
low_right = Pos(765, 641)
high_left = Pos(211, 483)
high_right = Pos(614, 483)
high_high_center = Pos(408, 129)
pos_castel = Pos(211, 128)

# Move
left = Move(high_left, back)
right = Move(high_right, back)
up_castel = Move(pos_castel, back)
forward = Move(pos_forward, back)
rotate_left = Move(low_left, low_right)
rotate_right = Move(low_right, low_left)
inventory = Move(pos_inventory, pos_inventory)

# Location
home = Location("home", [])
field = Location("field", [rotate_right])
tree_house = SunLocation("tree_house", [forward] * 4)
cake_house = SunLocation("cake_house", [forward, left])
boulder = Location("boulder", [rotate_left, forward, forward])
vinyl_door = Location("vinyl_door", [forward, right])
apple_tree = SunLocation("apple_tree", [rotate_left] + [forward] * 6)
station_desk = Location("station_desk", [forward, forward, right, left])
fluttershy_hut = MoonLocation("fluttershy_hut", [rotate_right] * 2 + [forward] * 3)
luna_viewpoint = WingLocation("luna_viewpoint", [rotate_right, up_castel, right])

# Object positions
scarecrow = Thing("scarecrow", field, Pos(491, 333))
obj_balloon = Thing("obj_balloon", field, Pos(250, 520))
bottle = Thing("bottle", station_desk, Pos(79, 509))
vinyl_disk = Thing("vinyl_disk", vinyl_door, Pos(518, 326))
transformation_book = Thing("transformation_book", home, Pos(45, 457))
twilight_book = Thing("twilight_book", tree_house, Pos(768, 334))
fluttershy_lamp = Thing("fluttershy_lamp", fluttershy_hut, Pos(293, 89))
fluttershy_window = Thing("fluttershy_window", fluttershy_hut, Pos(628, 340))

# Ponies positions
trixie = Thing("trixie", home, Pos(640, 510))
mrs_cake = Thing("mrs_cake", cake_house, Pos(240, 310))
applejack = Thing("applejack", apple_tree, Pos(221, 499))
station_desk_pony = Thing("station_desk_pony", station_desk, Pos(552, 341))