import time

import pyautogui as pg
from model import Pair
from sequence import *
from util import logcall

pg.FAILSAFE = True

# Banned from Equestria (Daily) v1.5
# WINDOW_TITLE = 'Banned from Equestria (Daily)'
WINDOW_TITLE = 'BFEQ'


# Misc
@logcall
def reload():
    """Reload the page and click through the introduction"""
    pos_reload.click()
    pg.hotkey("ctrl", "pagedown")
    fast(5.9, "intro") # A bit brutal, could use more refinements (using `sleep`)


# Scenario
def meet_luna(st: State):
    """Meet luna"""
    become(st, PonyKind.HORN)
    bring_balloon(st)
    learn_spell(st)
    get_vinyl(st)
    get_trixie1(st)
    become(st, PonyKind.WING)
    get_pinkie_pie(st)
    get_fluttershy(st)
    get_derpy(st)
    luna_viewpoint.go(st)


def apple_road(st: State):
    """Get money and use it"""
    learn_spell(st)
    get_money(st, 1)
    quest_muffin(st)
    bottle.touch(st); skip()
    quest_ticket(st)
    become(st, PonyKind.HORN)


def twibook(st: State):
    """Get twilight's book and give it back"""
    bring_balloon(st)
    learn_spell(st)
    become(st, PonyKind.HORN)
    dance_with_scarecrow(st)
    get_transformation_book(st)
    get_trixie1(st)
    become(st, PonyKind.WING)
    tree_house.go(st)


def trixie2(st: State):
    """Get Trixie Twice"""
    learn_spell(st)
    become(st, PonyKind.HORN)
    dance_with_scarecrow(st)
    get_trixie1(st)
    get_money(st, 1)
    eat_muffin(st)
    dance_with_scarecrow(st)
    get_trixie2(st)


###
sleep(0.5)
st = State(home, PonyKind.EARTH, 0, dict(), set())
beginning = time.time()
try:
    print(f"{beginning=}")
    place_window(window_title=WINDOW_TITLE)
    reload()

    trixie2(st)
except Exception:
    end = time.time()
    print(f"{end - beginning=}")
    raise
    # import traceback, pdb
    # traceback.print_exc()
    # pdb.post_mortem()
else:
    end = time.time()
    print(f"{end - beginning=}")
# finally:
#     breakpoint()