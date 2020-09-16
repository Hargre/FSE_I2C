import RPi_I2C_driver
import smbus2
import bme280

from time import sleep

lcd = RPi_I2C_driver.lcd()

i2c = 1
address = 0x76
bus = smbus2.SMBus(i2c)

calibration_params = bme280.load_calibration_params(bus, address)

while(1):
    data = bme280.sample(bus, address, calibration_params)

    temp = data.temperature
    humid = data.humidity
    press = data.pressure

    print("T: %.2f H: %.2f P: %.2f" % (temp, humid, press))

    lcd.lcd_display_string("T: %.2f H: %.2f" % (temp, humid), 1)
    lcd.lcd_display_string("P: %.2f" % (press), 2)

    sleep(1)