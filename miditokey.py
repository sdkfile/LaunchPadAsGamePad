import mido
import keyboard

def keymapping(msg):
    if msg.hex() == '90 0C 7F':
        keyboard.press('z')
    elif msg.hex() == '90 0C 00':
        keyboard.release('z')
    elif msg.hex() == '90 0D 7F':
        keyboard.press('x')
    elif msg.hex() == '90 0D 00':
        keyboard.release('x')
    elif msg.hex() == '90 0E 7F':
        keyboard.press('c')
    elif msg.hex() == '90 0E 00':
        keyboard.release('c')
    elif msg.hex() == '90 0F 7F':
        keyboard.press('v')
    elif msg.hex() == '90 0F 00':
        keyboard.release('v')
def run():
    with mido.open_input() as inport:
        choice = input()
        if choice == 'q':
            return True
        else:
            for msg in inport:
                print(msg)
                keymapping(msg)


run()
