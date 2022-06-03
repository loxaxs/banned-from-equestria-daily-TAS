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
meet_luna = [
    Become(PonyKind.HORN),
    BringBalloon(),
    LearnSpell(),
    Vinyl(),
    Trixie(),
    Become(PonyKind.WING),
    PinkiePie(),
    Fluttershy(),
    Derpy(),
    Goto(luna_viewpoint),
]


# Get money and use it
apple_road = [
    LearnSpell(),
    BreakBoulder(),
    GetMoney(2),
    BuyMuffin(),
    EatMuffin(),
    HelpSpike(),
]


# Get twilight's book and give it back
twibook = [
    BringBalloon(),
    LearnSpell(),
    Become(PonyKind.HORN),
    DanceWithScareCrow(),
    GetTransformationBook(),
    Trixie(),
    Goto(tree_house),
]


# Get Trixie twice
trixie_twice = [
    LearnSpell(),
    BreakBoulder(),
    GetMoney(1),
    BringBalloon(),
    BuyMuffin(),
    EatMuffin(),
    DanceWithScareCrow(),
    Trixie(),
    DanceWithScareCrow(),
    TrixieAgain(),
]


def plan_and_run(*args):
    # planning
    st = State(home, PonyKind.EARTH, 0, 0, dict(), set())
    for sequence in args:
        sequence.simulate(st)

    # running
    sleep(0.5)
    place_window(window_title=WINDOW_TITLE)
    reload()
    beginning = time.time()
    st = State(home, PonyKind.EARTH, 0, 0, dict(), set())
    for sequence in args:
        assert "end" not in st.status
        sequence.run(st)
    end = time.time()
    print(f"time: {end - beginning}")

###
try:
    plan_and_run(
        LearnSpell(),
        BreakBoulder(),
        GetMoney(2),
        BringBalloon(),
        BuyMuffin(),
        EatMuffin(),
        HelpSpike(),
        Zecora(),
        Twilight(),
        PinkiePie(),
        Fluttershy(),
        Vinyl(),
        Goto(luna_viewpoint),
    )
except (KeyboardInterrupt, pg.FailSafeException):
    print("interrupted")
except Exception:
    raise
    # import traceback, pdb
    # traceback.print_exc()
    # pdb.post_mortem()
# finally:
#     breakpoint()