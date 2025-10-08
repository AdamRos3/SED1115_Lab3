from machine import Pin, PWM, ADC
import time

adcA = ADC(Pin(26))
led1 = PWM(Pin(6))
led2 = PWM(Pin(7))
led3 = PWM(Pin(8))
led4 = PWM(Pin(9))

led1.freq(1000)
led2.freq(1000)
led3.freq(1000)
led4.freq(1000)

led1.duty_u16(0)
led2.duty_u16(0)
led3.duty_u16(0)
led4.duty_u16(0)

leds = [led1, led2, led3, led4]

threshold = int(65535/len(leds))

while True:
	valeur = adcA.read_u16()
	print(valeur)

	progress_full = int(valeur / threshold)
	progress_remainder = int(valeur % threshold)

	for i in range(0, progress_full):
		leds[i].duty_u16(65535)

	if (progress_full < len(leds) - 1):
		leds[progress_full + 1].duty_u16(progress_remainder)