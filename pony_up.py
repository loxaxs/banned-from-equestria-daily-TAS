from sequence import break_shield_trixie, break_second_shield_trixie
from fast import sleep, skip, accept, agree, fast
from info import *
from model import State, Pos
from util import logboth

# See README.md for description of the role of this file

class Pony:
    square: Pos = pos_four
    wait = 0.8
    waitload = 6.6
    click = 0
    def get(self, st: State):
        pony_name = type(self).__name__
        assert pony_name not in st.gotten
        st.gotten.add(pony_name)
        print(f"getting {pony_name}")
        self._getting(st)

        # /\ intercourse
        self.square.click() # square is usually pos_three or pos_four
        sleep(self.waitload) # wait for the bar to load, (it is slow for applejack)
        pos_exclamation.click() # final
        sleep(self.wait)
        skip(self.click) # skip dialogs
        sleep(.4)
        pos_end.click() # end square
        sleep(4.6) # "ya got ~" screen
        pos_next.click()
        sleep(2.4) # the screen fades to black
        # \/ intercourse
        st.location = home
        st.day += 1


class Twilight(Pony):
    click = 4
    wait = 8
    def _getting(self, st: State):
        assert "spike_service" in st.status
        st.assert_wing()
        st.assert_moon()
        tree_house_park.go(st)
        high_high_center.click()
        skip(2)
        sleep(1)
        skip(4)
        sleep(3.5)
        skip(2)


class Vinyl(Pony):
    def _getting(self, st: State):
        vinyl_disk.touch(st)
        sleep(2.9)
        skip(2)
        forward.do()
        center.click()
        sleep(18.5)


class Trixie(Pony):
    wait = 3.2
    click = 5
    def _getting(self, st: State):
        st.assert_horn()
        st.assert_moon()
        trixie.touch(st) # Zoom
        break_shield_trixie(st)
        skip()
        pos_trixie_square.click(); sleep(1)
        skip(5); sleep(3)
        skip(5); sleep(2.8)


class TrixieAgain(Pony):
    wait = 4
    click = 2
    def _getting(self, st: State):
        st.assert_horn()
        st.assert_moon()
        trixie.touch(st) # Zoom
        break_second_shield_trixie(st)
        skip()
        pos_trixie_square.click()
        fast(4.2)


class PinkiePie(Pony):
    wait = 2
    def _getting(self, st: State):
        assert "balloon" in st.status
        st.assert_sun()
        cake_house.go(st)
        forward.do()
        sleep(10)


class Applejack(Pony):
    wait = 16
    waitload = 19
    def _getting(self, st: State):
        assert "broken_boulder" in st.status
        st.assert_sun()
        applejack.touch(st)
        skip(4)
        sleep(.5)
        agree()
        fast(7)


class Fluttershy(Pony):
    def _getting(self, st: State):
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


class Derpy(Pony):
    wait = 13.2
    click = 0
    def _getting(self, st: State):
        derpy_letter_box.go(st)
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


class Zecora(Pony):
    def _getting(self, st: State):
        water_stream.touch(st)
        skip(3)
        everfree_forest.go(st)
        forward.do()
        skip()
        agree()
        sleep(3.7)
        for direction in [left, left, right] * 3:
            direction.do()
        forward.do()
        fast(5)
        pos_zecora_closet.click()
        sleep(2.5)
        skip(7)
        sleep(1)