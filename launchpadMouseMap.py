import mido
from pynput.mouse import Button, Controller

mouse = Controller()


def mousemapping(msg, direction):
    intensity = 1
    if msg.hex() == '90 66 7F':
        direction[1] = -intensity
    elif msg.hex() == '90 76 7F':
        direction[1] = intensity
    elif msg.hex() == '90 75 7F':
        direction[0] = -intensity
    elif msg.hex() == '90 77 7F':
        direction[0] = intensity
    elif msg.hex() == '90 66 00':
        direction[1] = 0
    elif msg.hex() == '90 76 00':
        direction[1] = 0
    elif msg.hex() == '90 75 00':
        direction[0] = 0
    elif msg.hex() == '90 77 00':
        direction[0] = 0
    return direction


def run():
    with mido.open_input() as inport:
        print(inport)
        print(inport.msg)
        direction = [0, 0]
        for msg in inport:
            # print(msg.hex())
            # mousemovement(mousemapping(msg, direction))
            print("hello")


def mousemovement(way):
    mouse.move(way[0], way[1])
    mousemovement(way)


class MouseMover:
    MouseDirection = [0, 0]

    @classmethod
    def MouseMoving(cls):
        while self.MouseDirection != [0, 0]:
            mouse.move(self.MouseDirection[0], self.MouseDirection[1])


run()
