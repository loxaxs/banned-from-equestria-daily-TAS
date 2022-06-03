import time

import pyautogui as pg

from fast import fast
from model import Pair
from sequence import *
from pony_up import *
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
    Vinyl().get(st)
    Trixie().get(st)
    become(st, PonyKind.WING)
    PinkiePie().get(st)
    Fluttershy().get(st)
    Derpy().get(st)
    luna_viewpoint.go(st)


def apple_road(st: State):
    """Get money and use it"""
    learn_spell(st)
    break_boulder(st)
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
    Trixie().get(st)
    become(st, PonyKind.WING)
    tree_house.go(st)


def trixieTwice(st: State):
    """Get Trixie Twice"""
    learn_spell(st)
    break_boulder(st)
    get_money(st, 1)
    bring_balloon(st)
    buy_muffin(st)
    eat_muffin(st)
    dance_with_scarecrow(st)
    Trixie().get(st)
    dance_with_scarecrow(st)
    TrixieAgain().get(st)


###
sleep(0.5)
st = State(home, PonyKind.EARTH, 0, 0, dict(), set())
beginning = time.time()
try:
    print(f"{beginning=}")
    place_window(window_title=WINDOW_TITLE)
    reload()

    learn_spell(st)
    break_boulder(st)
    get_money(st, 2)
    bring_balloon(st)
    buy_muffin(st)
    eat_muffin(st)
    help_spike(st)
    Zecora().get(st)
    Twilight().get(st)
    PinkiePie().get(st)
    Fluttershy().get(st)
    Vinyl().get(st)
    luna_viewpoint.go()

except (KeyboardInterrupt, pg.FailSafeException):
    print("interrupted")
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