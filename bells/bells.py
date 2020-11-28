#!/usr/bin/python

######
### The read only file system might be turned on.  run raspi-config to turn off
######

# Project using a Relat PiPlate and a raspberry pi zero w
#
# The purpose of the project is to automate relays which will control christmas lights

#
# References
# https://www.raspberrypi.org/documentation/linux/software/python.md
# https://pi-plates.com/relayplate-users-guide/
# https://pi-plates.com/examples/#Controlling_aRELAYplate_Remotely_with_Your_Web_Browser
# https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/#systemd
#
#

import piplates.RELAYplate as RELAY
import time

## The address of the relay plate
ppADDR = 0

RELAY.RESET(ppADDR)

while True:
    RELAY.relayON(ppADDR, 1)
    time.sleep(0.5)
    RELAY.relayOFF(ppADDR, 1)
    RELAY.relayON(ppADDR, 2)
    time.sleep(0.5)
    RELAY.relayOFF(ppADDR, 2)
    RELAY.relayON(ppADDR, 3)
    time.sleep(1)
    RELAY.relayOFF(ppADDR, 3)
    RELAY.relayON(ppADDR, 2)
    time.sleep(0.5)
    RELAY.relayOFF(ppADDR,2)
    RELAY.relayON(ppADDR, 1)
    time.sleep(0.5)
