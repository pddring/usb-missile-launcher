"""
USB Missile launcher scratch interface.
Written by P. Dring
https://github.com/pddring/usb-missile-launcher

"""
from launcher import Launcher
import scratch

# connect to rocket launcher
r = Launcher()

# connect to scratch
s = scratch.Scratch()
time = 200

# Loop continuously to wait for messages from scratch
while True:
    # get a message broadcast from scratch
	msg = s.receive()
    cmd = msg[1]
    
    # process the message
	"""
	This code will process the following broadcast messages from scratch:
	MOVE_LEFT: aims the missile launcher slightly to the left
	MOVE_RIGHT: aims the missile launcher slightly to the right
	MOVE_UP: hopefully you've got the idea by now...
	"""
	if cmd == "MOVE_LEFT":
        r.move(r.MOVE_LEFT, time)
    elif cmd == "MOVE_RIGHT":
        r.move(r.MOVE_RIGHT, time)
    elif cmd == "MOVE_UP":
        r.move(r.MOVE_UP, time)
    elif cmd == "MOVE_DOWN":
        r.move(r.MOVE_DOWN, time)
    elif cmd == "FIRE":
        r.fire()
    elif cmd == "LED_ON":
        r.set_led(True)
    elif cmd == "LED_OFF":
        r.set_led(False)