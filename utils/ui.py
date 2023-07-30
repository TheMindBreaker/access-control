import cns_wiegand as wiegand


WIEGAND_ZERO = 4
WIEGAND_ONE = 17

def on_card(facility_code, card_code):
    print('Facility Code: ', facility_code)
    print('Card Code: ', card_code)

wg = wiegand(3, 4, on_card)
wg.listen()
