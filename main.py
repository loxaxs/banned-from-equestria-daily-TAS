import time

import pyautogui as pg

from model import Pair
from sequence import *
from util import logcall

pg.FAILSAFE = True

# Banned from Equestria (Daily) v1.5
WINDOW_TITLE = 'Banned from Equestria (Daily)'
WINDOW_POS_OFFSET = Pair(0, 0)
EXTRA_POS_OFFSET = Pair(-8, -8)


# Misc
@logcall
def place_window():
    """Find the window, raise it, size it and move it"""
    browser_window: pg.Window
    [browser_window] = pg.getWindowsWithTitle(WINDOW_TITLE)
    x, y = WINDOW_POS_OFFSET
    cx, cy = EXTRA_POS_OFFSET
    browser_window.moveTo(x + cx, y + cy)
    browser_window.resizeTo(newWidth=835, newHeight=820)
    browser_window.activate()


@logcall
def reload():
    """Reload the page and click through the introduction"""
    pos_reload.click()
    fast(6.2, "intro") # A bit brutal, could use more refinements (using `sleep`)


# Scenario
def meet_luna(st: State):
    """Meet luna"""
    place_window()
    reload()
    become(st, Pony.HORN)
    learn_spell(st)
    bring_balloon(st)
    get_vinyl(st)
    get_trixie1(st)
    become(st, Pony.WING)
    get_pinkie_pie(st)
    get_fluttershy(st)
    get_derpy(st)
    luna_viewpoint.go(st)


def apple_road(st: State):
    """Get money and use it"""
    place_window()
    reload()
    learn_spell(st)
    get_money(st)
    quest_muffin(st)
    bottle.touch(st); skip()
    quest_ticket(st)
    become(st, Pony.HORN)


def twibook(st: State):
    """Get twilight's book and give it back"""
    place_window()
    reload()
    bring_balloon(st)
    learn_spell(st)
    become(st, Pony.HORN)
    dance_with_scarecrow(st)
    get_transformation_book(st)
    get_trixie1(st)
    become(st, Pony.WING)
    tree_house.go(st)
    # get_pinkie_pie(st)
    Location(tree_house.path[:-1]).go(st)


try:
    sleep(0.5)
    st = State(home, Pony.EARTH, 0, dict())
    beginning = time.time()
    print(f"{beginning=}")
    twibook(st)
    end = time.time()
    print(f"{end - beginning=}")
except Exception:
    import traceback, pdb
    traceback.print_exc()
    pdb.post_mortem()
finally:
    breakpoint()