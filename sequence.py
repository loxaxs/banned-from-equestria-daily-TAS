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
@logboth
def dance_with_scarecrow(st: State):
    """
    Dance with the scarecrow, either at day or at night
    Requirements: NONE
    """
    scarecrow.touch(st)
    skip(3)
    agree()
    sleep(8.4)
    st.day += 1


@logboth
def bring_balloon(st: State):
    """
    Fetch and bring balloon to Mrs.Cake, then put the gift in Pinkie's room
    Requirements:
    - time: day
    - balloon has not yet been touched
    """
    obj_balloon.touch(st, wait=0.2)
    skip()
    mrs_cake.touch(st, wait=0.2)
    skip(5)
    with forward:
        center.click()
        st.status["balloon"] = True


@logboth
def buy_muffin(st: State):
    """
    Go buy a muffing
    Requirements:
    - time: day
    - money: 3+ bucks
    - have no muffin in inventory
    """
    mrs_cake.touch(st)
    assert "muffin" not in st.status
    skip()
    agree()
    st.money -= 3
    assert st.money >= 0
    st.status["muffin"] = 1
    skip()


@logboth
def eat_muffin(st: State):
    """
    Go to Mrs Cake and buy a muffin.
    - The inventory must be clear of balloon
    - Time must be day
    - The player has enough money to buy the muffin
    """
    assert st.status.get("muffin", 0) > 0
    with inventory:
        sleep(.2)
        pos_muffin.click()
        sleep(.2)
        pos_inventory_yes.click()
        st.status["muffin"] = 0
        skip()
    st.status["shield_breaker_B"] = True


@logboth
def help_spike(st: State):
    """
    Buy one ticket and bring it to Spike
    Requirements:
    - time: day
    - money: 30+ bucks
    - Twilight has already been encountered and Spike seen escaping
    - The ticket has not yet been bought
    """
    assert "magic_attack_A" in st.status
    st.assert_sun()
    station_desk_pony.touch(st)
    skip(2)
    sleep(0.6)
    st.money -= 50
    assert st.money >= 0
    agree(); skip()
    become(st, PonyKind.WING)
    tree_house_park.go(st)
    high_high_center.click()
    fast(1.7)
    agree()
    sleep(3.7)
    skip(5)
    st.status["spike_service"] = True
    back.click()


@logboth
def learn_spell(st: State):
    """Go meet Twilight and learn the two spells
    Requirements:
    - Twilight has not been met yet
    """
    st.assert_sun()
    tree_house.go(st)
    center.click()
    fast(1.8)
    agree()
    skip(12)
    encounter_twilight(st)
    for k in range(2):
        twilight_book.touch(st, 0)
        skip(2)
    st.status["magic_attack_A"] = True
    st.status["shield_breaker_A"] = True


@logboth
def break_boulder(st: State):
    """
    Go break the boulder.
    Requirements:
    - know magic attack A
    - boulder has not been broken yet
    """
    assert "magic_attack_A" in st.status
    assert "broken_boulder" not in st.status
    become(st, PonyKind.HORN)
    boulder.go(st)
    center.click() # break boulder
    sleep(3); skip(12) # wait during scene then skip dialog



@logboth
def get_money(st: State, target_count):
    """
    Go buck the tree.
    Requirements:
    - day
    - boulder has been broken
    """
    st.assert_sun()
    assert "broken_boulder" not in st.status
    applejack.touch(st) # talk to AJ
    sleep(0.5); skip(6) # talk...
    print("bucking!")
    smash(43, 3.3) # Send 43 clicks to buck the tree
    center.click(); skip(2) # Talk to AJ
    st.money += 40
    if target_count <= 1:
        accept(); skip(2)
        return
    agree() # Continue bucking
    print("bucking again!")
    smash(44, 3.3); skip(3) # Smash the click button to buck the tree
    st.money += 40
    if target_count <= 2:
        accept(); skip(2)
        return
    agree() # Continue bucking
    print("bucking a third time!")
    smash(45, 3.3); skip(4) # Smash the click button to buck the tree
    accept(); skip(2) # Wanna go to the barn? -> No
    st.money += 40
    if target_count <= 3:
        accept(); skip(2)
        return
    count = 3
    while count < target_count:
        agree()
        print(f"bucking a {count}th time")
        smash(45, 3.8); skip(4)
        st.money += 40
        count += 1
    accept(); skip(2)


@logboth
def get_transformation_book(st: State):
    """
    Go to trixie and get the spell book
    Requirements:
    - Be a unicorn
    - Time is night
    - The book has not yet been taken
    """
    assert(st.kind == PonyKind.HORN) # assert we have a horn
    st.assert_moon() # assert we are at night
    trixie.touch(st)
    break_shield_trixie(st)
    transformation_book.touch(st)
    skip()
    back.click()


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