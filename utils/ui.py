import utils.cns_wiegand as wiegand
import config


def on_card(card_number, facility_code, cards_read):
	print(card_number)
	print(facility_code)
	print(card_number)
	
data = wiegand.read(config.WIEGAND[0], config.WIEGAND[1])
