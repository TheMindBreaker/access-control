import time
import RPi.GPIO as GPIO

class Wiegand:
    def __init__(self, data0_pin, data1_pin, callback):
        self.data_bits = []
        self.bit_count = 0
        self.facility_code = 0
        self.card_code = 0
        self.callback = callback

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(data0_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(data1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(data0_pin, GPIO.FALLING, callback=self.data0, bouncetime=300)
        GPIO.add_event_detect(data1_pin, GPIO.FALLING, callback=self.data1, bouncetime=300)

    def data0(self, channel):
        self.data_bits.append(0)
        if 1 <= self.bit_count <= 8:
            self.facility_code = (self.facility_code << 1) | 0
        if 9 <= self.bit_count <= 26:
            self.card_code = (self.card_code << 1) | 0
        self.bit_count += 1

    def data1(self, channel):
        self.data_bits.append(1)
        if 1 <= self.bit_count <= 8:
            self.facility_code = (self.facility_code << 1) | 1
        if 9 <= self.bit_count <= 26:
            self.card_code = (self.card_code << 1) | 1
        self.bit_count += 1

    def listen(self):
        try:
            while True:
                if self.bit_count >= 26:
                    self.callback(self.facility_code, self.card_code)
                    self.bit_count = 0
                    self.data_bits = []
                    self.facility_code = 0
                    self.card_code = 0
                time.sleep(0.1)
        finally:
            GPIO.cleanup()
