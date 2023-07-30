import time
import RPi.GPIO as GPIO


def read(pin0, pi1):
    # Set up RPi.GPIO
    GPIO.setmode(GPIO.BCM)

    DATA0_PIN = 4
    DATA1_PIN = 17

    GPIO.setup(DATA0_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(DATA1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # This will store our Wiegand data
    data = []

    # These functions are called when a falling edge is detected on DATA0 or DATA1
    def data0_falling(channel):
        data.append(0)

    def data1_falling(channel):
        data.append(1)

    # Register the callbacks
    GPIO.add_event_detect(DATA0_PIN, GPIO.FALLING, callback=data0_falling, bouncetime=300)
    GPIO.add_event_detect(DATA1_PIN, GPIO.FALLING, callback=data1_falling, bouncetime=300)

    # Loop forever, printing the Wiegand data whenever it becomes 26 bits long
    try:
        while True:
            if len(data) >= 26:
                print("Read Wiegand data:", ''.join(map(str, data)))
                return map(str, data)
                data.clear()
            time.sleep(0.1)
    finally:
        GPIO.cleanup()