import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# 1. Define your pins
# The Hack Club macropad usually connects one side of the switch to a GPIO 
# and the other to Ground. Adjust these pins based on your specific wiring.
keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3) 
keyboard.row_pins = (board.GP4,) # If using a single row/direct pin setup
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 2. Define your Keymap
# Replace these with the shortcuts you actually want!
keyboard.keymap = [
    [
        KC.COPY,    # Key 1: Ctrl+C (Cmd+C on Mac)
        KC.PASTE,   # Key 2: Ctrl+V
        KC.MUTE,    # Key 3: Mute Audio
        KC.PLAY,    # Key 4: Play/Pause Media
    ]
]

if __name__ == '__main__':
    keyboard.go()