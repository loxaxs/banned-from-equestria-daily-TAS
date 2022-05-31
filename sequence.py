from encounter import encounter_trixie
from fast import smash
from pony_up import *
from util import logboth


# Macro
@logboth
def become(st: State, pony: Pony):
    """
    Become an earth pony, a pegasus or a unicorn
    Requirements:
    - time: day
    """
    if st.pony == pony:
        return
    st.assert_sun()
    trixie.touch(st)
    encounter_trixie(st, 'trixie')
    skip(2)
    sleep(.4)
    if pony == Pony.HORN or (pony == Pony.EARTH and st.pony == Pony.HORN):
        accept()
    elif pony == Pony.WING or (pony == Pony.EARTH and st.pony == Pony.WING):
        agree()
    sleep(1.6)
    st.pony = pony


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
    sleep(8.8)
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


@logboth
def buy_muffin(st: State, count=2):
    """
    Go buy a muffing. /!\\ potentially buggy
    Requirements:
    - time: day
    - money: 3+ bucks
    - have no muffin in inventory
    """
    mrs_cake.touch(st); skip(count)
    agree(); skip(2)


@logboth
def quest_muffin(st: State):
    """
    Buy one muffing, eat it, then buy one more.
    TODO fix it! (I accept PRs)
    Requirements:
    - time: day
    - money: 6+ bucks
    - have no muffin in inventory
    """
    # fails for unknown reason - but at least it buys the muffin
    buy_muffin(st, 4)
    with inventory:
        pos_muffin.click()
        agree(); skip()
    buy_muffin(st)


@logboth
def quest_ticket(st: State):
    """
    Buy one ticket and bring it to Spike
    Requirements:
    - time: day
    - money: 30+ bucks
    - Twilight has already been encountered and Spike seen escaping
    - The ticket has not yet been bought
    """
    station_desk_pony.touch(st)
    skip(2)
    sleep(0.6)
    agree(); skip()
    become(st, Pony.WING)
    Location([forward] * 3).go(st)
    high_high_center.click()
    skip(7)
    sleep(2)
    skip(3)
    sleep(1)
    agree()
    sleep(3.3)
    skip(4)
    back.click()


@logboth
def learn_spell(st: State):
    """Go meet Twilight and learn the two spells
    Requirements:
    - day
    - Twilight has not been met yet
    """
    tree_house.go(st)
    center.click()
    fast(1.8)
    agree()
    skip(12)
    encounter_trixie(st, 'twilight')
    for k in range(2):
        twilight_book.touch(st, 0)
        skip(2)


@logboth
def get_money(st: State, target_count):
    """
    Go break the boulder and buck the tree.
    Requirements:
    - know magic attack A
    - day
    - boulder has not been broken yet
    """
    become(st, Pony.HORN)
    boulder.go(st)
    center.click() # break boulder
    sleep(3); skip(12) # wait during scene then skip dialog
    apple_tree.go(st)
    applejack.touch(st) # talk to AJ
    sleep(0.5); skip(6) # talk...
    print("bucking!")
    smash(43, 3.8) # Send 43 clicks to buck the tree
    center.click(); skip(2) # Talk to AJ
    if target_count <= 1:
        accept(); skip(2)
        return
    agree() # Continue bucking
    print("bucking again!")
    smash(44, 3.8); skip(3) # Smash the click button to buck the tree
    if target_count <= 2:
        accept(); skip(2)
        return
    agree() # Continue bucking
    print("bucking a third time!")
    smash(45, 3.8); skip(4) # Smash the click button to buck the tree
    accept(); skip(2) # Wanna go to the barn? -> No
    if target_count <= 3:
        accept(); skip(2)
        return
    count = 3
    while count < target_count:
        agree()
        print(f"bucking a {count}th time")
        smash(45, 3.8); skip(4)
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
    assert(st.pony == Pony.HORN) # assert we have a horn
    st.assert_moon() # assert we are at night
    trixie.touch(st)
    break_shield_trixie(st)
    transformation_book.touch(st)
    skip()
    back.click()


@logboth
def eat_muffin(st: State):
    """
    Go to Mrs Cake and buy a muffin.
    - The inventory must be clear of balloon
    - Time must be day
    - The player has enough money to buy the muffin
    """
    mrs_cake.touch(st)
    skip()
    agree()
    skip()
    pos_inventory.click()
    sleep(.2)
    pos_muffin.click()
    sleep(.2)
    pos_inventory_yes.click()
    skip()
    pos_inventory.click()
