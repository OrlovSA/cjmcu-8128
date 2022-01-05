from time import sleep


class HDC1000(object):
    
    def __init__(self, i2c=None, addr=64):
        self.i2c = i2c
        self.addr = addr  
        self.humidity = 0
        self.c_temperature = 0
        self.f_temperature = 0   
        # Select configuration register, 0x02(02)
        # 0x30(48)	Temperature, Humidity enabled, Resolultion = 14-bits, Heater on
        self.i2c.writeto_mem(self.addr, 0x02, bytearray([0x30]))
        
        
    # Read data back, 2 bytes
    # temp MSB, temp LSB
    def data_ready(self):
        # Send temp measurement command, 0x00(00)
        self.i2c.writeto(self.addr, bytearray([0x00]))
        sleep(0.5)

        data = self.i2c.readfrom(self.addr, 0x40, 2)
        data0 = data[0]
        data1 = data[1]

        # Convert the data
        temp = (data0 * 256) + data1
        self.c_temperature = (temp / 65536.0) * 165.0 - 40
        self.f_temperature = self.c_temperature * 1.8 + 32


        # Send humidity measurement command, 0x01(01)
        self.i2c.writeto(self.addr, bytearray([0x01]))
        sleep(0.5)

        # Read data back, 2 bytes
        # humidity MSB, humidity LSB
        data = self.i2c.readfrom(self.addr, 0x40, 2)
        data0 = data[0]
        data1 = data[1]

        # Convert the data
        humidity = (data0 * 256) + data1
        self.humidity = (humidity / 65536.0) * 100.0
        return True


# def main():
#     from machine import Pin, I2C
#     import time
#     i2c = I2C(1, scl=Pin(18), sda=Pin(19), freq=9600)
#     hdc1000 = HDC1000(i2c)
#     time.sleep(1)
#     while True:
#         if hdc1000.data_ready():  
#             print(f'temperature: {hdc1000.c_temperature}, humidity: {hdc1000.humidity}')
#             time.sleep(1)

# main()