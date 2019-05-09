import mido
import mido.backends.rtmidi
import keyboard
import sys

from launchpadMidiMap import launchpadMidiMap


def keymapping(msg):
    if len(msg.hex().split(" ")) == 3:
        if launchpadMidiMap(msg) == (0, 7, True):
            keyboard.press('z')
        elif launchpadMidiMap(msg) == (0, 7, False):
            keyboard.release('z')
        elif launchpadMidiMap(msg) == (1, 7, True):
            keyboard.press('x')
        elif launchpadMidiMap(msg) == (1, 7, False):
            keyboard.release('x')
        elif launchpadMidiMap(msg) == (2, 7, True):
            keyboard.press('c')
        elif launchpadMidiMap(msg) == (2, 7, False):
            keyboard.release('c')
        elif launchpadMidiMap(msg) == (3, 7, True):
            keyboard.press('v')
        elif launchpadMidiMap(msg) == (3, 7, False):
            keyboard.release('v')
        elif launchpadMidiMap(msg) == (6, 6, True):
            keyboard.press('up')
        elif launchpadMidiMap(msg) == (6, 6, False):
            keyboard.release('up')
        elif launchpadMidiMap(msg) == (6, 7, True):
            keyboard.press('down')
        elif launchpadMidiMap(msg) == (6, 7, False):
            keyboard.release('down')
        elif launchpadMidiMap(msg) == (5, 7, True):
            keyboard.press('left')
        elif launchpadMidiMap(msg) == (5, 7, False):
            keyboard.release('left')
        elif launchpadMidiMap(msg) == (7, 7, True):
            keyboard.press('right')
        elif launchpadMidiMap(msg) == (7, 7, False):
            keyboard.release('right')
        elif launchpadMidiMap(msg)[0] == 8 and launchpadMidiMap(msg)[1] == 0:
            sys.exit()


def run():
    with mido.open_input() as inport:
        for msg in inport:
            print(msg.hex())
            keymapping(msg)
    sys.stdin.readlin()


run()
