import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

R_1 = 82 # kohms
R_2 = 12 # kohms, vout to ADC 
R_ratio = (R_1 + R_2) / R_2

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2c)

chan = AnalogIn(ads, ADS.P0)

print("{:>5}\t{:>5}".format('raw', 'v'))

while True:
  print("{:>5}\t\t{:>5.3f}".format(chan.value, chan.voltage))
  print("Voltage:\t{:>5.3f}".format(R_ratio * chan.voltage))
  time.sleep(0.5)


