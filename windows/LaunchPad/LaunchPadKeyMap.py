import mido
import mido.backends.rtmidi
import keyboard
import sys


def keymapping(msg):
    if len(msg.hex().split(" ")) == 3:

        if msg.hex().split(" ")[1] == '70' \
                and msg.hex().split(" ")[2] != '00':
            keyboard.press('z')
        elif msg.hex().split(" ")[1] == '70' \
                and msg.hex().split(" ")[2] == '00':
            keyboard.release('z')
        elif msg.hex().split(" ")[1] == '71' \
                and msg.hex().split(" ")[2] != '00':
            keyboard.press('x')
        elif msg.hex().split(" ")[1] == '71' \
                and msg.hex().split(" ")[2] == '00':
            keyboard.release('x')
        elif msg.hex().split(" ")[1] == '72' \
                and msg.hex().split(" ")[2] != '00':
            keyboard.press('c')
        elif msg.hex().split(" ")[1] == '72' \
                and msg.hex().split(" ")[2] == '00':
            keyboard.release('c')
        elif msg.hex().split(" ")[1] == '73' \
                and msg.hex().split(" ")[2] != '00':
            keyboard.press('v')
        elif msg.hex().split(" ")[1] == '73' \
                and msg.hex().split(" ")[2] == '00':
            keyboard.release('v')
        elif msg.hex().split(" ")[1] == '66' \
                and msg.hex().split(" ")[2] != '00':
            keyboard.press('up')
        elif msg.hex().split(" ")[1] == '66' \
                and msg.hex().split(" ")[2] == '00':
            keyboard.release('up')
        elif msg.hex().split(" ")[1] == '76' \
                and msg.hex().split(" ")[2] != '00':
            keyboard.press('down')
        elif msg.hex().split(" ")[1] == '76' \
                and msg.hex().split(" ")[2] == '00':
            keyboard.release('down')
        elif msg.hex().split(" ")[1] == '75' \
                and msg.hex().split(" ")[2] != '00':
            keyboard.press('left')
        elif msg.hex().split(" ")[1] == '75' \
                and msg.hex().split(" ")[2] == '00':
            keyboard.release('left')
        elif msg.hex().split(" ")[1] == '77' \
                and msg.hex().split(" ")[2] != '00':
            keyboard.press('right')
        elif msg.hex().split(" ")[1] == '77' \
                and msg.hex().split(" ")[2] == '00':
            keyboard.release('right')
        elif msg.hex().split(" ")[1] == '08':
            sys.exit()


def run():
    with mido.open_input() as inport:
        for msg in inport:
            print(msg.hex())
            keymapping(msg)
    sys.stdin.readlin()


run()
