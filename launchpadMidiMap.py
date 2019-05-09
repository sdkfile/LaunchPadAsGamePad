def launchpadmidimap(msg):
    midihex = msg.hex().split(" ")
    if len(midihex) == 3:
        midinum = int(midihex[1])
        x = midinum % 10
        y = midinum / 10

        onoff = midihex[2] != '00'
        return (x, y, onoff)
