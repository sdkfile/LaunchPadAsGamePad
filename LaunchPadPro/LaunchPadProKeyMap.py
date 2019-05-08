import mido
import mido.backends.rtmidi
import keyboard
import io
import sys


def keymapping(msg):
    if len(msg.hex().split(" ")) == 3:

        if msg.hex().split(" ")[1] == '0B' \
                and msg.hex().split(" ")[2] != '00':
            keyboard.press('z')
        elif msg.hex().split(" ")[1] == '0B' \
                and msg.hex().split(" ")[2] == '00':
            keyboard.release('z')
        elif msg.hex().split(" ")[1] == '0C' \
                and msg.hex().split(" ")[2] != '00':
            keyboard.press('x')
        elif msg.hex().split(" ")[1] == '0C' \
                and msg.hex().split(" ")[2] == '00':
            keyboard.release('x')
        elif msg.hex().split(" ")[1] == '0D' \
                and msg.hex().split(" ")[2] != '00':
            keyboard.press('c')
        elif msg.hex().split(" ")[1] == '0D' \
                and msg.hex().split(" ")[2] == '00':
            keyboard.release('c')
        elif msg.hex().split(" ")[1] == '0E' \
                and msg.hex().split(" ")[2] != '00':
            keyboard.press('v')
        elif msg.hex().split(" ")[1] == '0E' \
                and msg.hex().split(" ")[2] == '00':
            keyboard.release('v')
        elif msg.hex().split(" ")[1] == '1B' \
                and msg.hex().split(" ")[2] != '00':
            keyboard.press('up')
        elif msg.hex().split(" ")[1] == '1B' \
                and msg.hex().split(" ")[2] == '00':
            keyboard.release('up')
        elif msg.hex().split(" ")[1] == '11' \
                and msg.hex().split(" ")[2] != '00':
            keyboard.press('down')
        elif msg.hex().split(" ")[1] == '11' \
                and msg.hex().split(" ")[2] == '00':
            keyboard.release('down')
        elif msg.hex().split(" ")[1] == '10' \
                and msg.hex().split(" ")[2] != '00':
            keyboard.press('left')
        elif msg.hex().split(" ")[1] == '10' \
                and msg.hex().split(" ")[2] == '00':
            keyboard.release('left')
        elif msg.hex().split(" ")[1] == '12' \
                and msg.hex().split(" ")[2] != '00':
            keyboard.press('right')
        elif msg.hex().split(" ")[1] == '12' \
                and msg.hex().split(" ")[2] == '00':
            keyboard.release('right')
        elif msg.hex().split(" ")[1] == '08':
            sys.quit()


def run():
    with mido.open_input() as inport:
        for msg in inport:
            print(msg.hex())
            keymapping(msg)
    sys.stdin.readlin()


run()
