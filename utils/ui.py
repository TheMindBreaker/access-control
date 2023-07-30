from wiegand import Wiegand
import config

GREEN_LED = Pin(config.LED_WIEGAND)

def on_card(card_number, facility_code, cards_read):
	print(card_number)
	print(facility_code)
	print(card_number)
	
Wiegand(config.WIEGAND[0], config.WIEGAND[1], on_card)
