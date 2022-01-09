# cjmcu-8128, BMP280, CCS811, HDC1000 sensors for MicroPython
Tested on ESP32, Default pin scl-18, sda-19, gnd-wak-gnd, vcc-3.3v

It is necessary to close contacts: WAK-GND
```python
from CCS811 import CCS811
from HDC1000 import HDC1000
from BMP280 import BMP280
from time import sleep
from machine import Pin, I2C


def main():
    """
    hdc1000_c_temperature: 33.04352
    hdc1000_f_temperature: 91.47834
    hdc1000_humidity: 38.04321
    ccs811_eCO2: 426
    ccs811_tVOC: 3
    bmp280_c_temperature: 32.87
    bmp280_pressure: 99783
    bmp280_mm_pressure: 748.4338
    bmp280_altitude: 129.0936 
    """
    i2c = I2C(scl=Pin(18), sda=Pin(19), freq=100000)
    cjmcu_8128 = CJMCU_8128(i2c)

    while True:
        if cjmcu_8128.data_ready():
            print(f'hdc1000_c_temperature: {cjmcu_8128.hdc1000_c_temperature}')
            print(f'hdc1000_f_temperature: {cjmcu_8128.hdc1000_f_temperature}')
            print(f'hdc1000_humidity: {cjmcu_8128.hdc1000_humidity}')
            print(f'ccs811_eCO2: {cjmcu_8128.ccs811_eCO2}')
            print(f'ccs811_tVOC: {cjmcu_8128.ccs811_tVOC}')
            print(f'bmp280_c_temperature: {cjmcu_8128.bmp280_c_temperature}')
            print(f'bmp280_pressure: {cjmcu_8128.bmp280_pressure}')
            print(f'bmp280_mm_pressure: {cjmcu_8128.bmp280_mm_pressure}')
            print(f'bmp280_altitude: {cjmcu_8128.bmp280_altitude}')
            print('*'*100)
        sleep(1)


main()
 ```
 ![](https://github.com/OrlovSA/cjmcu-8128/blob/main/CCS811-HDC1080-BMP280.jpg)
    
    
    

