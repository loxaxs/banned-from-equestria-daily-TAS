from dataclasses import dataclass

from fast import sleep, skip, fast, smash, agree, accept
from info import *
from model import State, PonyKind
from util import logboth


# Macro
@logboth
def become(st: State, kind: PonyKind):
    """
    Become an earth pony, a pegasus or a unicorn
    Requirements:
    - time: day
    """
    if st.kind == kind:
        return
    st.assert_sun()
    trixie.touch(st)
    encounter_trixie(st)
    skip(2)
    sleep(.4)
    if kind == PonyKind.HORN or (kind == PonyKind.EARTH and st.kind == PonyKind.HORN):
        accept()
    elif kind == PonyKind.WING or (kind == PonyKind.EARTH and st.kind == PonyKind.WING):
        agree()
    sleep(1.6)
    st.kind = kind


# Sequence
class Sequence:
    def check(self, st: State):
        pass
    def interact(self, st: State):
        raise NotImplementedError()
    def change(self, st: State):
        pass

    def run(self, st: State):
        self.check(st)
        self.interact(st)
        self.change(st)

    def simulate(self, st: State):
        self.check(st)
        self.change(st)


@dataclass
class Goto(Sequence):
    location: Location
    def interact(self, st: State):
        self.location.go(st)


@dataclass
class Become(Sequence):
    kind: PonyKind
    def check(self, st: State):
        st.assert_sun()
    def interact(self, st: State):
        become(st, self.kind)
    def change(self, st: State):
        st.kind = self.kind


class Breakpoint(Sequence):
    def interact(self, st: State):
        breakpoint()


class Set(Sequence):
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    def interact(self, st):
        pass
    def change(self, st):
        for key, value in self.kwargs.items():
            setattr(st, key, value)


class DanceWithScarecrow(Sequence):
    """
    Dance with the scarecrow, either at day or at night
    Requirements: NONE
    """
    def interact(self, st: State):
        scarecrow.touch(st)
        skip(3)
        agree()
        sleep(8.4)
    def change(self, st):
        st.day += 1


class BringBalloon(Sequence):
    """
    Fetch and bring balloon to Mrs.Cake, then put the gift in Pinkie's room
    Requirements:
    - time: day
    - balloon has not yet been touched
    """
    def check(self, st: State):
        st.assert_sun()
    def interact(self, st: State):
        balloon.touch(st, wait=0.2)
        skip()
        mrs_cake.touch(st, wait=0.2)
        skip(5)
        with forward:
            center.click()
    def change(self, st):
        st.status["balloon"] = True


class BringWineBottle(Sequence):
    def interact(self, st: State):
        wine_bottle.touch(st, wait=0.2)
        skip()
        berry_punch_doorstep.touch(st, wait=0.2)
        agree()
        skip(2)


class BuyMuffin(Sequence):
    """
    Go buy a muffing
    Requirements:
    - time: day
    - money: 3+ bucks
    - have no muffin in inventory
    """
    def check(self, st: State):
        assert st.status.get("muffin", 0) == 0
        assert st.money >= 3
    def interact(self, st: State):
        mrs_cake.touch(st)
        skip()
        agree()
        st.money -= 3
        skip()
    def change(self, st: State):
        st.status["muffin"] = 1


class EatMuffin(Sequence):
    """
    Go to Mrs Cake and buy a muffin.
    - The inventory must be clear of balloon
    - Time must be day
    - The player has enough money to buy the muffin
    """
    def check(self, st: State):
        assert st.status.get("muffin", 0) > 0
    def interact(self, st: State):
        with inventory:
            sleep(.2)
            pos_muffin.click()
            sleep(.2)
            pos_inventory_yes.click()
            skip()
    def change(self, st: State):
        st.status["muffin"] = 0
        st.status["shield_breaker_B"] = True


class HelpSpike(Sequence):
    """
    Buy one ticket and bring it to Spike
    Requirements:
    - time: day
    - money: 30+ bucks
    - Twilight has already been encountered and Spike seen escaping
    - The ticket has not yet been bought
    """
    def check(self, st: State):
        assert st.money >= 50
        assert "magic_attack_A" in st.status # i.e. we met Twilight
        st.assert_sun()
    def interact(self, st: State):
        station_desk_pony.touch(st)
        skip(2)
        sleep(0.6)
        st.money -= 50
        agree(); skip()
        become(st, PonyKind.WING)
        tree_house_park.go(st)
        high_high_center.click()
        fast(1.7)
        agree()
        sleep(3.7)
        skip(5)
        back.click()
    def change(self, st: State):
        st.status["spike_service"] = True
        st.kind = PonyKind.WING


class VinylRemixingTime(Sequence):
    def check(self, st: State):
        assert "Vinyl" in st.gotten
    def interact(self, st: State):
        vinyl_window.touch(st)
        skip(2)


class FluttershySoManyWonders(Sequence):
    def check(self, st):
        assert "fluttershy_asleep" not in st.status
        st.assert_moon()
    def interact(self, st):
        from pony_up import Fluttershy
        Fluttershy.start(st)
        accept() # Forget her
        skip(6)
        sleep(4.5)
        fluttershy_window.touch(st)
        skip(4)
        fluttershy_window.touch(st)
        skip(3)
        fluttershy_window.touch(st)
        skip(5)
    def change(self, st: State):
        st.status["fluttershy_asleep"] = True


class BringTransformationBook(Sequence):
    def check(self, st: State):
        assert st.status.get("transformation_book", 0) > 0
        st.assert_sun()
    def interact(self, st: State):
        tree_house.go(st)
        center.click()
        skip(3)
        sleep(9)
        skip(6)
        st.location = tree_house_park


class PinkiePieGoodbyeEquestria(Sequence):
    def check(self, st: State):
        assert "PinkiePie" in st.gotten
        st.assert_sun()
    def interact(self, st):
        cake_house.go(st)
        with forward:
            center.click()
            skip(2)


class CutieMarkCrusaders(Sequence):
    def check(self, st: State):
        assert "broken_boulder" in st.status
        st.assert_sun()
    def interact(self, st):
        cutie_mark_crusaders_tree.go(st)
        center.click()
        skip(17)
        sleep(1.2)
        center.click()
        skip(2)


class LearnSpell(Sequence):
    """Go meet Twilight and learn the two spells
    Requirements:
    - Twilight has not been met yet
    """
    def check(self, st: State):
        st.assert_sun()
    def interact(self, st: State):
        tree_house.go(st)
        center.click()
        fast(1.8)
        agree()
        skip(12)
        for k in range(2):
            twilight_book.touch(st, 0)
            skip(2)
    def change(self, st: State):
        encounter_twilight(st)
        st.status["magic_attack_A"] = True
        st.status["shield_breaker_A"] = True


class BreakBoulder(Sequence):
    """
    Go break the boulder.
    Requirements:
    - know magic attack A
    - boulder has not been broken yet
    """
    def check(self, st: State):
        assert "magic_attack_A" in st.status
        assert "broken_boulder" not in st.status
        assert st.sun() or st.kind == PonyKind.HORN
    def interact(self, st: State):
        become(st, PonyKind.HORN)
        boulder.go(st)
        center.click() # break boulder
        sleep(3); skip(12) # wait during scene then skip dialog
    def change(self, st: State):
        st.status["broken_boulder"] = True
        st.kind = PonyKind.HORN


class RarityService(Sequence):
    """Slice the fabric and ask for a kinded reward"""
    def check(self, st: State):
        st.assert_sun()
    def interact(self, st: State):
        become(st, PonyKind.HORN)
        rarity_house.go(st)
        center.click()
        sleep(1)
        skip(4)
        agree()
        skip(2)
        high_left.click()
        sleep(1)
        skip(4)
        agree()
        skip(10)
        back.click()
        pos_chalkboard.click()
        skip(2)
        high_right.click() # go to the fabric
        center.click() # slice it
        skip()
        back.click()
        center.click() # talk to Rarity
        skip(12)
    def change(self, st: State):
        st.status["magic_attack_B"] = True
        st.status["rarity_service"] = True



@dataclass
class GetMoney(Sequence):
    target_count: int
    """
    Go buck the tree.
    Requirements:
    - day
    - boulder has been broken
    """
    def check(self, st: State):
        assert "broken_boulder" in st.status
        assert "bucking" not in st.status
        st.assert_sun()
    def interact(self, st: State):
        applejack.touch(st) # talk to AJ
        sleep(0.5); skip(6) # talk...
        print("bucking!")
        center.click()
        smash(41, 3.3) # Send 43 clicks to buck the tree
        center.click(); skip(2) # Talk to AJ
        st.money += 40
        if self.target_count <= 1:
            accept(); skip(2)
            return
        agree() # Continue bucking
        print("bucking again!")
        center.click()
        smash(42, 3.3); skip(3) # Smash the click button to buck the tree
        st.money += 40
        if self.target_count <= 2:
            accept(); skip(2)
            return
        agree() # Continue bucking
        print("bucking a third time!")
        center.click()
        smash(43, 3.3); skip(4) # Smash the click button to buck the tree
        accept(); skip(2) # Wanna go to the barn? -> No
        st.money += 40
        if self.target_count <= 3:
            accept(); skip(2)
            return
        count = 3
        while count < self.target_count:
            agree()
            print(f"bucking a {count}th time")
            center.click()
            smash(41 + count, 3.8); skip(4)
            st.money += 40
            count += 1
        accept(); skip(2)
    def change(self, st: State):
        st.status["bucking"] = self.target_count
        st.money += 40 * self.target_count


class GetTransformationBook(Sequence):
    """
    Go to Trixie and get the spell book
    Requirements:
    - Be a unicorn
    - Time is night
    - The book has not yet been taken
    """
    def check(self, st: State):
        st.assert_horn()
        st.assert_moon()
    def interact(self, st: State):
        trixie.touch(st)
        break_shield_trixie(st)
        transformation_book.touch(st)
        skip()
        back.click()
    def change(self, st: State):
        st.status["transformation_book"] = 1


# /\ Helper sequences
@logboth
def encounter_twilight(st: State):
    if 'trixie2' not in st.status:
        st.status['trixie2'] = 'twilight'
    else:
        pass


@logboth
def encounter_trixie(st: State):
    if 'trixie1' not in st.status:
        skip(8)
        st.status['trixie1'] = True
    elif 'trixie2' not in st.status:
        pass
    elif st.status['trixie2'] == 'trixie':
        pass
    else:
        st.status['trixie2'] = 'trixie'
        sleep(.5)
        skip(6)
        sleep(2)
        skip()


@logboth
def break_shield_trixie(st: State):
    st.assert_horn()
    assert "shield_breaker_A" in st.status
    if 'trixie_shield' not in st.status:
        center.click()
        sleep(.8)
        skip(1)
        st.status['trixie_shield'] = True


@logboth
def break_second_shield_trixie(st: State):
    st.assert_horn()
    assert "shield_breaker_B" in st.status
    if 'second_trixie_shield' not in st.status:
        center.click()
        sleep(.8)
        skip(1)
        st.status['second_trixie_shield'] = True


@logboth
def go_to_zecora_hut(st: State):
    everfree_forest.go(st)
    forward.do()
    skip()
    agree()
    sleep(3.7)
    for direction in [left, left, right] * 3:
        direction.do()
    forward.do()
# \/ helper sequences
