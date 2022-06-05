# Banned from Equestria (Daily) TAS

-- Tool Assisted Speedrun for Banned from Equestria

A bunch of functions and classes to play through Banned from Equestria (Daily) without touching your mouse & keyboard.

- time starts at page reload
- runs with Chrome / Canary Chrome / Chromium

Supports getting ponies:

- Twilight
- Rarity
- PinkiePie
- Applejack
- Fluttershy
- Rainbow Dash

- Vinyl
- Trixie
- Trixie, the second time
- Derpy
- Zecora
- Chrysalis, with the bad end

Also supports sequences for:

- Trixie
  - Changing between Earth pony, Pegasus and Unicorn
  - Her talking longer the first time we chat with her
  - Her talking longer when she sees we want her transformation book
- Switching between day and night by dancing with Mr. Scarecrow
- Getting money
- Buying a cupcake, eating a cupcake
- Keeping track of the location, and moving efficiently
- Going to luna's viewpoint

Does not support:

- Trixie
    - Talking to trixie after having taken the book from her
- Getting:
    - Celestia
    - Luna
    - Big Macintosh
    - More ponies (who???)
- Buying at the spa

## Requirements

This project was written using Python 3.8 and PyAutoGUI (`pip3 install pyautogui`).

## Trying it out

In a browser window, open two Banned from Equestria tabs and have no other tabs open in that window, then run `python main.py`

## Important note

PyAutoGUI's `FAILSAFE` mode is enabled. This enables you to stop a macro by moving the mouse to the top left corner of the screen. This will only work while the script is sending an input, not if the script is sleeping. In the latter case you can select the terminal windows and type Ctrl+C to interrupt the script.

## Getting luna

First, you need to get five ponies during the first half days, and make sure to have wings on the last.
During the last night, go to Celestia's castle and go to the platform to the right, it will be lit and you'll be able to join luna.

The fight against luna is easy if you can click fast enough and see each time your shield breaks. The strategy is simple:

- Keep your shield up by clicking 6 times on it (3-6 clicks are necessary to bring it up)
- Once your shield is up, you can attack Luna
  - Don't attack Luna when your shield is down
- Luna breaks your shield as soon as you attack her, so you shouldn't hit her more than once or twice at a time.

## License

This repository is available under CC0 copyleft. It is part of the public domain.

## Project structure

Concept ladder (`model.py`):

```txt
Scenario (main.py) A full story to play from the beginning [
    def meet_luna(),
    # ^ play in a way which allows to meet luna
  ] 
| (they are made of)
Sequence (sequence.py and pony_up.py) [
    def learn_spell(),
    # ^ go to the tree house, talk to twilight and learn the spells
    def get_derpy()
    # ^ save derpy, and ... get her 
  ]
| (which are made of)
- Move (Location.go: `cake_house.go()`)
- Object touch (Thing.touch: `wine_bottle.touch()`)
- Pony touch (Thing.touch: `trixie.touch()`)
- Clicking through dialogs (`skip` and `fast`, in fast.py)
- Waiting during cutscenes (`sleep` and `fast`, in fast.py)
| (these things rely on)
- State [st = State()]
- Thing [
    wine_bottle = Thing(station_desk, Pos(79, 509)),
    twilight_book = Thing(tree_house, Pos(768, 334)),
    trixie = Thing(home, Pos(640, 510)),
  ]
| which contain
Location [
    home = Location([]),
    tree_house = SunLocation([forward] * 4),
  ]
| which is made of a list of
Move (a move that can be undone) [
    forward = Move(pos_forward, back),
  ]
| which is made of a pair of
Pos (X, Y coordinates of a point to click) [
    pos_forward = Pos(412, 485),
    back = Pos(413, 641),
  ]
```

All of the concrete data which hydrates these models is in `info.py`.  

Here's what each file contains or does:

- `encounter.py` - Dealing with ponies (just Trixie)'s changing behaviour from one encounter to another
- `fast.py` - Utility functions used to deal with times and number of clicks while writing sequences of actions
- `info.py` - All data about the game: UI element positions, arrow positions, map of the locations and positions of things and ponies both in that map and on the screen
- `main.py` - Contains some scenarios. You can change them and write your owns.
- `model.py` - Contains the classes containing the location management logic, and other state management logic.
- `pony_up.py` - Code to manage intercourse time with ponies
- `sequence.py` - Sequence of actions that are combined in `main.py` to create scenarios
- `util.py` - Logging decorators and list manipulation function(s).
