from encounter import break_shield_trixie, break_second_shield_trixie
from fast import sleep, skip, accept, agree, fast
from info import *
from model import State, Pos
from util import logboth

# See README.md for description of the role of this file

@logboth
def intercourse(st: State, square: Pos, wait=0.8, waitload=6.6, click=0):
    """
    Manage clicking at the right time and places during the intercourse scene(s).
    Also update the state as needed.
    """
    square.click() # square is usually pos_three or pos_four
    sleep(waitload) # wait for the bar to load, (it is slow for applejack)
    pos_exclamation.click() # final
    sleep(wait)
    skip(click) # skip dialogs
    sleep(.4)
    pos_end.click() # end square
    sleep(4.8) # "ya got ~" screen
    pos_next.click()
    sleep(2.6) # the screen fades to black
    st.location = home
    st.day += 1


@logboth
def get_vinyl(st: State):
    st.getting("Vinyl")
    vinyl_disk.touch(st); sleep(2.9)
    skip(2)
    forward.do()
    center.click(); sleep(18.5)
    intercourse(st, square=pos_four)


@logboth
def get_trixie1(st: State):
    st.getting("Trixie")
    st.assert_horn()
    st.assert_moon()
    trixie.touch(st) # Zoom
    break_shield_trixie(st)
    skip()
    pos_trixie_square.click(); sleep(1)
    skip(5); sleep(3)
    skip(5); sleep(3)
    intercourse(st, square=pos_four, wait=3.2, click=5)


@logboth
def get_trixie2(st: State):
    st.getting("Trixie again")
    st.assert_horn()
    st.assert_moon()
    trixie.touch(st) # Zoom
    break_second_shield_trixie(st)
    skip()
    pos_trixie_square.click()
    fast(5)
    intercourse(st, square=pos_four, wait=4, click=2)


@logboth
def get_pinkie_pie(st: State):
    st.getting("Pinkie Pie")
    st.assert_sun()
    cake_house.go(st)
    forward.do()
    sleep(10)
    intercourse(st, square=pos_four, wait=2)


@logboth
def get_applejack(st: State):
    st.getting("Applejack")
    st.assert_sun()
    applejack.touch(st)
    skip(4)
    sleep(.5)
    agree()
    fast(7)
    intercourse(st, square=pos_four, wait=16, waitload=19)


@logboth
def get_fluttershy(st: State):
    st.getting("Fluttershy")
    st.assert_moon()
    fluttershy_window.touch(st)
    skip(7); sleep(3.4)
    skip()
    fluttershy_lamp.touch(st); sleep(2.6)
    skip(2); sleep(.6)
    accept() # Why?
    skip(8); sleep(.6)
    accept() # Cheer up
    skip(2); sleep(.6)
    agree() # Let's fuck
    skip(4); sleep(.6)
    accept() # Want it?
    skip(4); sleep(3)
    intercourse(st, square=pos_four, wait=2.4, click=4)


@logboth
def get_derpy(st: State):
    st.getting("Derpy")
    Location([forward, rotate_left]).go(st)
    center.click()
    skip(2)
    center.click()
    skip()
    sleep(4) # hearing
    center.click()
    skip(2)
    agree()
    skip()
    sleep(29) # saving derpy & intro
    intercourse(st, square=pos_three, wait=13.2, click=0)