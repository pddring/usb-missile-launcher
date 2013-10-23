"""
USB Missile Launcher API
Written by P. Dring
Based on some code from https://github.com/codedance/Retaliation
See https://github.com/pddring/usb-missile-launcher for more info

Usage:

# import the rocket launcher module
from launcher import Launcher

# connect to the usb rocket launcher
rocket = Launcher()

# turn led on
rocket.set_led(True)

# moves the launcher up for 500ms
rocket.move(rocket.MOVE_UP, 500)

# fire one rocket
rocket.fire()

# turn led off
rocket.set_led(False)
"""
import usb.core
import time
   
class Launcher:
    """
    USB Missile launcher class
    """
    MOVE_DOWN = 0x1
    MOVE_UP = 0x2
    MOVE_LEFT = 0x4
    MOVE_RIGHT = 0x8
    FIRE = 0x10
    STOP = 0x20
    
    
    dev = None
    
    def connect(self):
        """
        Connects to the missile launcher. This is called automatically - 
        you don't need to call this function in your code. 
        """
        self.dev = usb.core.find(idVendor=0x2123, idProduct=0x1010)
        if self.dev == None:
            raise ValueError("Could not connect to missile launcher")
        self.dev.set_configuration()
    
    def check_connection(self):
        """
        Establishes a usb connection to the missile launcher if
        one hasn't already been established 
        """
        if self.dev == None:
            self.connect()
    
    def set_led(self, light_status):
        """
        Turns the LED on or off
        @param light_status: Boolean. True to turn the LED on
        """
        self.check_connection()
        if light_status:
            self.dev.ctrl_transfer(0x21, 0x09, 0, 0, [0x03, 1, 0x00,0x00,0x00,0x00,0x00,0x00])
        else:
            self.dev.ctrl_transfer(0x21, 0x09, 0, 0, [0x03, 0, 0x00,0x00,0x00,0x00,0x00,0x00])
        
    def move(self, movement, time_ms):
        """
        Moves the missile launcher
        @param movement: one of Launcher.MOVE_UP, Launcher.MOVE_DOWN
            Launcher.MOVE_LEFT or Launcher.MOVE_RIGHT
        @param time_ms: time for which to move the missile launcher (in milliseconds)
        """
        self.check_connection()
        self.dev.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, movement, 0x00,0x00,0x00,0x00,0x00,0x00])
        time.sleep(time_ms / 1000.0)
        self.stop()
    
    def stop(self):
        """
        Stops moving the missile launcher
        """
        self.check_connection()
        self.dev.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, self.STOP, 0x00,0x00,0x00,0x00,0x00,0x00])
        
    def fire(self):
        """
        Fires one missile
        """
        self.check_connection()
        self.dev.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, self.FIRE, 0x00,0x00,0x00,0x00,0x00,0x00])    
