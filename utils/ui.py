from cns_wiegand import Wiegand
import RPi.GPIO as GPIO

WIEGAND_ZERO = 4
WIEGAND_ONE = 17

def on_card(facility_code, card_code):
    print("HOLA")
    print('Facility Code: ', facility_code)
    print('Card Code: ', card_code)

while True:
    try:
        wg = Wiegand(17, 27, on_card)
        # Other code
    finally:
        GPIO.cleanup()

