from wiegand import Wiegand
import config


def on_card(card_number, facility_code, cards_read):
	print(card_number)
	print(facility_code)
	print(card_number)
	
Wiegand(pin0=config.WIEGAND[0], pin1=config.WIEGAND[1], callback=on_card)
