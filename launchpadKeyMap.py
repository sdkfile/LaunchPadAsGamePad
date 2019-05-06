import mido
import keyboard


def keymapping(msg):
    if msg.hex() == '90 70 7F':
        keyboard.press('z')
    elif msg.hex() == '90 70 00':
        keyboard.release('z')
    elif msg.hex() == '90 71 7F':
        keyboard.press('x')
    elif msg.hex() == '90 71 00':
        keyboard.release('x')
    elif msg.hex() == '90 72 7F':
        keyboard.press('c')
    elif msg.hex() == '90 72 00':
        keyboard.release('c')
    elif msg.hex() == '90 73 7F':
        keyboard.press('v')
    elif msg.hex() == '90 73 00':
        keyboard.release('v')
    elif msg.hex() == '90 66 7F':
        keyboard.press('up')
    elif msg.hex() == '90 66 00':
        keyboard.release('up')
    elif msg.hex() == '90 76 7F':
        keyboard.press('down')
    elif msg.hex() == '90 76 00':
        keyboard.release('down')
    elif msg.hex() == '90 75 7F':
        keyboard.press('left')
    elif msg.hex() == '90 75 00':
        keyboard.release('left')
    elif msg.hex() == '90 77 7F':
        keyboard.press('right')
    elif msg.hex() == '90 77 00':
        keyboard.release('right')


def run():
    with mido.open_input() as inport:
        for msg in inport:
            print(msg.hex())
            keymapping(msg)


run()
