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

meet_luna_alt = [
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
    DanceWithScarecrow(),
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
    DanceWithScarecrow(),
    Trixie(),
    DanceWithScarecrow(),
    TrixieAgain(),
]

more_bullshit = [
    # time 0
    BringBalloon(),
    BringWineBottle(), ##
    LearnSpell(),
    Become(PonyKind.HORN),
    Vinyl(), # time 1
    VinylRemixingTime(), ##
    FluttershySoManyWonders(), ##
    GetTransformationBook(),
    DanceWithScarecrow(), # time 2
    BringTransformationBook(), ##
    PinkiePie(), # time 3
    DanceWithScarecrow(), # time 4
    PinkiePieGoodbyeEquestria(), ##
    BreakBoulder(),
    CutieMarkCrusaders(), ##
    Chrysalis(), # early end
]

main_six = [
    Become(PonyKind.WING),
    Breakpoint(), # get Rainbow Dash
    Set(day=1, location=home),
    Fluttershy(),
    BringBalloon(),
    LearnSpell(),
    BreakBoulder(),
    GetMoney(3),
    HelpSpike(),
    Applejack(),
    Twilight(),
    RarityService(),
    PinkiePie(),
    Rarity(),
]


main_six_with_more_bullshit = [
    BringBalloon(),
    BringWineBottle(), ##
    LearnSpell(),
    BreakBoulder(),
    CutieMarkCrusaders(), ##
    GetMoney(3),
    HelpSpike(),
    Become(PonyKind.WING),
    Breakpoint(), # get Rainbow Dash
    Set(day=1, location=home),
    Twilight(),
    Become(PonyKind.HORN),
    PinkiePie(),
    GetTransformationBook(),
    Fluttershy(),
    PinkiePieGoodbyeEquestria(), ##
    BringTransformationBook(), ##
    RarityService(),
    Applejack(),
    Rarity(),
    ###
    # VinylRemixingTime and FluttershySoManyWonders cannot be obtained
    # simultaneously to the main six ending
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
    plan_and_run(*main_six_with_more_bullshit)
except (KeyboardInterrupt, pg.FailSafeException):
    print("interrupted")
except Exception:
    raise
    # import traceback, pdb
    # traceback.print_exc()
    # pdb.post_mortem()
# finally:
#     breakpoint()