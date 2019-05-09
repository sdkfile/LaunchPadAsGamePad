import sys
import mido
import math
import time
from launchpadMidiMap import launchpadMidiMap
from pynput.mouse import Button, Controller

# For Window
# from win32api import GetSystemMetrics

# print("Width =", GetSystemMetrics(0))
# print("Height =", GetSystemMetrics(1))

from Quartz import CGDisplayBounds
from Quartz import CGMainDisplayID


def screen_size():
    mainMonitor = CGDisplayBounds(CGMainDisplayID())
    return (mainMonitor.size.width, mainMonitor.size.height)


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


def buttonpush():
    mouse.push(Button.left)
    mouse.push(Button.right)


def miditovector(msg):
    output = launchpadMidiMap(msg)
    x = output[0]
    y = output[1]
    onoff = output[2]
    if onoff:
        logic = 1
    else:
        logic = 0
    vector_x = (x - 3.5) * logic
    vector_y = (y - 3.5) * logic
    return (vector_x, vector_y)


def run():
    inport = mido.open_input()
    outport = mido.open_output()
    # direction = [0, 0]
    org = (0, 0)
    for msg in inport:
        # print(msg.hex())
        # mousemovement(mousemapping(msg, direction))
        outport.send(msg)
        if launchpadMidiMap(msg)[0] == 8 and launchpadMidiMap(msg)[1] == 0 and not launchpadMidiMap(msg)[2]:
            sys.exit()
        print(miditovector(msg))
        if miditovector(msg) != (0, 0):
            org = mousemoving(miditovector(msg)[0], miditovector(msg)[1], screen_size(), org)


def mousemoving(x, y, size, org):
    if x != 0 and y != 0:
        width = size[0]
        height = size[1]
        x += 3.5
        y += 3.5
        x /= 3.5
        y /= 3.5
        rel_x = width * x / 2
        rel_y = height * y / 2
        a = org[0]
        b = org[1]
        smoothmove(a, b, rel_x, rel_y)
        # mouse.position = (rel_x, rel_y)
    else:
        rel_x = 0
        rel_y = 0
    return rel_x, rel_y


def smoothmove(x, y, x1, y1):
    dist_x = (x1 - x)
    dist_y = (y1 - y)
    distance = math.sqrt(math.pow(dist_x, 2) + math.pow(dist_y, 2))
    num = round(distance)
    for i in range(num):
        x += dist_x / num
        y += dist_y / num
        mouse.position = (x, y)
        time.sleep(0.00015)
    mouse.position = (x1, y1)


def mousemovement(way):
    mouse.move(way[0], way[1])
    mousemovement(way)


run()
