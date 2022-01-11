from CCS811 import CCS811
from HDC1000 import HDC1000
from BMP280 import BMP280
from time import sleep


class CJMCU_8128(object):
    #[64, 90, 118] 64 - HDC1000, 90 - CCS811, 118 - BMP280
    def __init__(self, I2C):
        self.ccs811 = CCS811(I2C, 90)  
        self.hdc1000 = HDC1000(I2C, 64)  
        self.bmp280 = BMP280(I2C, 118)
        self.old_t = 0
        self.old_h = 0
        self.range_correction = 2
        self.hdc1000_c_temperature = 0
        self.hdc1000_f_temperature = 0
        self.hdc1000_humidity = 0
        self.ccs811_eCO2 = 0
        self.ccs811_tVOC = 0
        self.bmp280_c_temperature = 0
        self.bmp280_pressure = 0
        self.bmp280_mm_pressure = 0
        self.bmp280_altitude = 0
        sleep(1)
        
    def data_ready(self):

        if self.hdc1000.data_ready():
            self.hdc1000_c_temperature = self.hdc1000.c_temperature
            self.hdc1000_f_temperature = self.hdc1000.f_temperature
            self.hdc1000_humidity = self.hdc1000.humidity

        if self.ccs811.data_ready():
            if abs(int(self.hdc1000_c_temperature) - self.old_t) >= self.range_correction or abs(int(self.hdc1000_humidity) - self.old_h) >= self.range_correction:
                self.old_t = self.hdc1000_c_temperature
                self.old_h = self.hdc1000_humidity
                self.ccs811.put_envdata(int(self.hdc1000_humidity), int(self.hdc1000_c_temperature))
                sleep(0.5)
                
            self.ccs811_eCO2 = self.ccs811.eCO2
            self.ccs811_tVOC = self.ccs811.tVOC

        self.bmp280_c_temperature = self.bmp280.getTemp()
        self.bmp280_pressure = self.bmp280.getPress()
        self.bmp280_mm_pressure = self.bmp280_pressure / 133.3224
        self.bmp280_altitude = self.bmp280.getAltitude()

        return True


# def main():
#     from machine import Pin, I2C
#     """
#     hdc1000_c_temperature: 33.04352
#     hdc1000_f_temperature: 91.47834
#     hdc1000_humidity: 38.04321
#     ccs811_eCO2: 426
#     ccs811_tVOC: 3
#     bmp280_c_temperature: 32.87
#     bmp280_pressure: 99783
#     bmp280_mm_pressure: 748.4338
#     bmp280_altitude: 129.0936
#     ****************************************************************************************************
#     """
#     i2c = I2C(scl=Pin(18), sda=Pin(19), freq=100000)
#     cjmcu_8128 = CJMCU_8128(i2c)

#     while True:
#         if cjmcu_8128.data_ready():
#             print(f'hdc1000_c_temperature: {cjmcu_8128.hdc1000_c_temperature}')
#             print(f'hdc1000_f_temperature: {cjmcu_8128.hdc1000_f_temperature}')
#             print(f'hdc1000_humidity: {cjmcu_8128.hdc1000_humidity}')
#             print(f'ccs811_eCO2: {cjmcu_8128.ccs811_eCO2}')
#             print(f'ccs811_tVOC: {cjmcu_8128.ccs811_tVOC}')
#             print(f'bmp280_c_temperature: {cjmcu_8128.bmp280_c_temperature}')
#             print(f'bmp280_pressure: {cjmcu_8128.bmp280_pressure}')
#             print(f'bmp280_mm_pressure: {cjmcu_8128.bmp280_mm_pressure}')
#             print(f'bmp280_altitude: {cjmcu_8128.bmp280_altitude}')
#             print('*'*100)
#         sleep(1)


# main()
