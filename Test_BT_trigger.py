#!/usr/bin/env python

import sys
import evdev

TRIGGER_DEVICE = 'AB Shutter3'

def get_BT_device_list():
    devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]

    # failure if devices list empty
    if len(devices) == 0:
        print("No devices found, try running with sudo")
        sys.exit(1)

    # iteratively check device list for BT device
    print('checking connected devices...')
    for device in devices:
        if device.name == TRIGGER_DEVICE: # look for trigger device
            print(device)
            device.grab() # other apps unable to receive events until device released
            for event in device.read_loop():
                if event.type == evdev.ecodes.EV_KEY: # look for pressed key events
                    print(evdev.categorize(event))

if __name__ == "__main__":
    get_BT_device_list();
