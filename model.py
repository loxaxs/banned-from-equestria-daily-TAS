import pyautogui as pg

from collections import namedtuple
from dataclasses import dataclass
from enum import Enum
from typing import List

from util import remove_common_prefix

Pair = namedtuple("Pair", ("x", "y"))


# # Classes
class PonyKind(Enum):
    EARTH = "EARTH"
    WING = "WING"
    HORN = "HORN"


@dataclass
class State:
    """
    The state is created at the beginning and passed throughout the program.
    It allows each component to know in what state the game is, to:
    - Decide how to go somewhere
    - Check that the state allow performing the action the component does
    Each component is responsible to update the state when it changes anything
    in the game that is mentioned in the state.

    The properties to maintain are:
    - location - the scene/location where Big Brian is. This is mostly managed by the Location object
    - pony - what kind of pony Big Brian is: Earth Pony, Pegasus or Unicorn
    - day - the number of elapsed half-days since the beginning of the game (starts at 0)
    """
    location: "Location"
    kind: PonyKind
    day: int
    money: int
    status: dict
    gotten: set

    def sun(self):
        return self.day % 2 == 0

    def moon(self):
        return not self.sun()

    def assert_sun(self):
        assert self.sun()

    def assert_moon(self):
        assert self.moon()

    def assert_horn(self):
        assert self.kind == PonyKind.HORN

    def assert_wing(self):
        assert self.kind == PonyKind.WING


class Pos(Pair):
    """
    A pos is a pair of coordinates that can be clicked (and hovered).
    """
    size_factor = 2
    y_offset = 80
    base_window_height = 700
    def hover(self):
        pg.moveTo(
            int(self.x * self.size_factor),
            int((self.y - self.y_offset) * self.size_factor + self.y_offset),
        )

    def click(self):
        pg.click(
            int(self.x * self.size_factor),
            int((self.y - self.y_offset) * self.size_factor + self.y_offset),
        )

@dataclass
class Move:
    """
    A move is an action that can be undone.
    """
    forward: Pos
    backward: Pos

    def do(self):
        self.forward.click()

    def undo(self):
        self.backward.click()

    def __enter__(self):
        self.do()

    def __exit__(self, _et, _ev, _tb):
        self.undo()


@dataclass
class Location:
    name: str
    path: List[Move]

    def go(self, st: State):
        undo_list, do_list = remove_common_prefix(st.location.path, self.path)
        print(f"go to {self.name} (-{len(undo_list)} +{len(do_list)})")
        for move in reversed(undo_list):
            move.undo()
        for move in do_list:
            move.do()
        st.location = self

    def __repr__(self):
        return f"<Loc:{self.name}>"


class SunLocation(Location):
    def go(self, st: State):
        st.assert_sun()
        super().go(st)


class MoonLocation(Location):
    def go(self, st: State):
        st.assert_moon()
        super().go(st)


class WingLocation(Location):
    def go(self, st: State):
        assert st.kind == PonyKind.WING
        super().go(st)


@dataclass
class Thing:
    name: str
    location: Location
    position: Pos

    def touch(self, st: State, wait: float = 0.4):
        self.location.go(st)
        self.position.click()
        pg.sleep(wait)

    def __repr__(self):
        return f"<Thing:{self.name}>"