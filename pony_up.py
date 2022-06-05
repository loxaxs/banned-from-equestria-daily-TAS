from fast import sleep, skip, accept, agree, fast, clicker
from info import *
from model import State, Pos, PonyKind
from sequence import (
    Sequence,
    break_shield_trixie,
    break_second_shield_trixie,
    go_to_zecora_hut,
    become,
)
from util import logboth

# See README.md for description of the role of this file


class Pony(Sequence):
    square: Pos = pos_four
    wait = 0.8
    waitload = 6.6
    click = 0

    def check(self, st: State):
        self.pony_check(st)

    def change(self, st: State):
        self.pony_change(st)

    def pony_check(self, st: State):
        assert type(self).__name__ not in st.gotten

    def pony_change(self, st: State):
        st.gotten.add(type(self).__name__)
        st.location = home
        st.day += 1

    def interact(self, st):
        print(f"getting {type(self).__name__}")
        self._getting(st)

        # /\ sex scene
        self.square.click()  # square is usually pos_three or pos_four
        sleep(self.waitload)  # wait for the bar to load, (it is slow for applejack)
        pos_exclamation.click()  # final
        sleep(self.wait)
        skip(self.click)  # skip dialogs
        sleep(0.4)
        pos_end.click()  # end square
        sleep(4.6)  # "ya got ~" screen
        pos_next.click()
        sleep(2.4)  # the screen fades to black
        # \/


class Twilight(Pony):
    click = 4
    wait = 8
    waitload = 9

    def check(self, st: State):
        self.pony_check(st)
        assert "spike_service" in st.status
        st.assert_wing()
        st.assert_moon()

    def _getting(self, st: State):
        tree_house_park.go(st)
        high_high_center.click()
        skip(2)
        sleep(1)
        skip(4)
        sleep(4)
        skip(2)
        sleep(1)


class Rarity(Pony):
    wait = 3

    def check(self, st: State):
        self.pony_check(st)
        assert "Twilight" in st.gotten
        assert "rarity_service" in st.status
        assert "magic_attack_B" in st.status
        st.assert_horn()
        st.assert_moon()

    def _getting(self, st: State):
        spike_box.touch(st)
        skip(5)
        accept()
        skip(2)
        sleep(4)
        skip(6)
        rarity_window.touch(st)
        sleep(2)
        skip(7)
        rarity_window.touch(st)
        pos_center_square.click()
        sleep(3)


class Vinyl(Pony):
    def _getting(self, st: State):
        vinyl_disk.touch(st)
        sleep(2.9)
        skip(2)
        forward.do()
        center.click()
        sleep(17.5)


class Trixie(Pony):
    wait = 3.2
    click = 5

    def check(self, st):
        self.pony_check(st)
        st.assert_horn()
        st.assert_moon()

    def _getting(self, st: State):
        trixie.touch(st)  # Zoom
        break_shield_trixie(st)
        skip()
        pos_center_square.click()
        sleep(1)
        skip(5)
        sleep(3)
        skip(5)
        sleep(2.8)


class TrixieAgain(Pony):
    wait = 4
    click = 2

    def check(self, st):
        self.pony_check(st)
        assert "Trixie" in st.gotten
        st.assert_horn()
        st.assert_moon()

    def _getting(self, st: State):
        trixie.touch(st)  # Zoom
        break_second_shield_trixie(st)
        skip()
        pos_center_square.click()
        fast(4.2)


class PinkiePie(Pony):
    wait = 2

    def check(self, st):
        self.pony_check(st)
        assert "balloon" in st.status
        st.assert_sun()

    def _getting(self, st: State):
        cake_house.go(st)
        forward.do()
        sleep(10)


class Applejack(Pony):
    wait = 13.5
    waitload = 19

    def check(self, st):
        self.pony_check(st)
        assert "broken_boulder" in st.status
        assert st.status.get("bucking", 0) >= 3
        st.assert_sun()

    def _getting(self, st: State):
        applejack.touch(st)
        skip(4)
        sleep(0.5)
        agree()
        fast(7)


class Fluttershy(Pony):
    wait = 3
    click = 4

    def check(self, st):
        assert "fluttershy_asleep" not in st.status
        self.pony_check(st)
        st.assert_moon()

    @classmethod
    def start(cls, st):
        fluttershy_window.touch(st)
        skip(7)
        sleep(3.4)
        skip()
        fluttershy_lamp.touch(st)
        sleep(2.6)
        skip(2)
        sleep(0.6)
        accept()  # Why?
        skip(8)
        sleep(0.6)
        accept()  # Cheer up
        skip(2)
        sleep(0.6)

    def _getting(self, st: State):
        Fluttershy.start(st)
        agree()  # Let's fuck
        skip(4)
        sleep(0.6)
        accept()  # Want it?
        skip(4)
        sleep(3)

    def change(self, st: State):
        self.pony_change(st)
        st.status["fluttershy_asleep"] = True


class RainbowDash(Pony):
    wait = 5

    def check(self, st: State):
        st.assert_sun()

    def _getting(self, st: State):
        home.go(st)
        become(st, PonyKind.WING)
        high_high_center.click()
        center.click()
        sleep(2)
        skip(2)
        sleep(1)
        agree() # race you!
        skip(5)
        agree() # yes!
        skip(3)
        clicker(
            center,
            7.29, 3.01, 1.36, 1.94, 1.66, 1.87, 1.45, 1.05, 0.96, 1.48, 3.06, 0.96,
            0.69, 1.72, 0.79, 1.07, 0.71, 0.82, 1.20, 0.64, 0.58, 0.95, 0.58, 0.58,
            0.43, 0.93, 0.97, 0.61, 0.47, 0.94, 0.48, 0.49, 0.87, 0.93, 0.54, 0.50,
            0.86, 0.66, 0.49, 0.74, 0.36, 0.49, 0.41, 0.55, 0.38, 0.96, 0.34, 0.52,
            0.42, 0.42, 0.72, 0.43, 0.34, 0.70, 0.57, 0.57, 0.30, 0.54, 0.33, 0.47,
            0.33, 0.53, 0.32, 0.54, 0.31, 0.43, 0.46,
        )
        skip()
        sleep(.8)
        skip(2)
        sleep(.8)
        skip(2)
        sleep(.8)
        agree()
        skip(2)
        sleep(.8)
        skip(2)
        sleep(.8)
        agree()
        skip(5)
        sleep(.8)
        skip(2)
        sleep(.8)
        skip(2)
        sleep(.8)
        pos_center_square.click()
        sleep(4)

    def change(self, st: State):
        st.kind = PonyKind.WING


class Derpy(Pony):
    wait = 13.2
    click = 0

    def _getting(self, st: State):
        derpy_letter_box.go(st)
        center.click()
        skip(2)
        center.click()
        skip()
        sleep(4)  # hearing
        center.click()
        skip(2)
        agree()
        skip()
        sleep(29)  # saving derpy & intro


class Zecora(Pony):
    square = pos_three

    def _getting(self, st: State):
        water_stream.touch(st)
        skip(3)
        go_to_zecora_hut(st)
        fast(5)
        pos_zecora_closet.click()
        sleep(2.5)
        skip(7)
        sleep(1)


class Chrysalis(Pony):
    wait = 4
    click = 7

    def check(self, st):
        self.pony_check(st)
        assert "Zecora" not in st.gotten

    def _getting(self, st: State):
        go_to_zecora_hut(st)
        fast(6)

    def change(self, st):
        self.pony_change(st)
        st.status["end"] = True
