import time

import pyautogui as pg

from info import center, pos_agree, pos_accept
from util import logcall, repeat

TIME_RELAXATION = 0

# Click macro
@logcall
def agree():
    pos_agree.click()

@logcall
def accept():
    pos_accept.click()


@logcall
def fast(duration: float, comment: str = ""):
    """Fast-forward-click throughout some scene"""
    def click():
        center.click()
    repeat(click, pg.sleep, duration, "done")


@logcall
def skip(count: int = 1, comment: str = ""):
    def click():
        center.click()
    repeat(click, pg.sleep, count / 10, "done")


@logcall
def smash(count: int, duration: float, comment: str = ""):
    pg.click(*center, count, 0.001)
    pg.sleep(duration)


@logcall
def sleep(duration: float, comment: str = ""):
    def nop(): pass
    print("sleep", end=" ")
    repeat(nop, pg.sleep, duration + TIME_RELAXATION, "done")

def clicker(pos, *sleepList):
    goal = time.time()
    goal -= 0.30 # pg.sleep is usually late
    for sleepTime in sleepList:
        goal += sleepTime
        pg.sleep(goal - time.time())
        pos.click()