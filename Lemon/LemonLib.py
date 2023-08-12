from time import sleep
from machine import I2C, Pin

class PCA9685:
    #initalizer of the class
    def __init__(self, i2c, address=0x40):
        self.i2c = i2c
        self.address = address
        self.reset()


    def reset(self):
        #send the reset command to PCA9685 0x06 = reset value of PCA
        self.i2c.writeto_mem(self.address, 0x00, bytes([0x06]))

    
    def set_pwm_freq(self, freq: float):
        #internal oscilator(stable clock signal which serves a timing refrence) value
        prescale_val = 25000000.0  # 25MHz
        #converts this value to 12 bit which the PCA9685 uses
        prescale_val /= 4096.0  # 12-bit
        #divivded by freq to send signals at requried freq
        prescale_val /= freq
        #one is subtract to ensure it fals into the 12 bit range(0-4095)
        prescale_val -= 1.0
        #round up to the nearest int
        prescale = int(prescale_val + 0.5)
        #reads the info from the sleep register
        #0x00 first register controlles if the PCA9685 is on
        old_mode = self.i2c.readfrom_mem(self.address, 0x00, 1)[0]
        #0111 = 0x07 0001 0000 = 0x10
        new_mode = (old_mode & 0x7F) | 0x10 #updates the on/off of sleep mode through binary operation
        
        self.i2c.writeto_mem(self.address, 0x00, bytes([new_mode])) #ensures the PCA 9685 is in sleep mode because PCA must be asleep before configuring it such as setting the prescale val.
        #the adress which sets the prescale to the internal oscilator
        self.i2c.writeto_mem(self.address, 0xFE, bytes([prescale]))  # set the prescaler val which is important essantial things such as for PWM frequency control
        self.i2c.writeto_mem(self.address, 0x00, bytes([old_mode]))  # restore original base configs(basically factory settings) of the PCA9685

    def __set_pwm__(self, channel, on, off): #on and off are the parameters for the on and off time
        #calculate channel offset(in pca9685 every channel equires 4 registers so channel offset must be calculated via channel*4
        #the time setting is for the time of pwm signal on and off
        channel_offset = 4 * channel
        #note that 0xFF is equvilant to one in binary
        self.i2c.writeto_mem(self.address, 0x06 + channel_offset, bytes([on & 0xFF]))#(0x06 = ON_L)writes the lower 8 bits of the on register sets the timimng of the beginingg for the active period
        self.i2c.writeto_mem(self.address, 0x07 + channel_offset, bytes([(on >> 8) & 0xFF]))#(OxO7 = ON_H) writes the upper 4 bits completes the setting of time (remaining bits)
        self.i2c.writeto_mem(self.address, 0x08 + channel_offset, bytes([off & 0xFF]))#(0x08 = OFF_L)writes the lower 8 bits of the off register sets the timimng of the beginnig for the off period
        self.i2c.writeto_mem(self.address, 0x09 + channel_offset, bytes([(off >> 8) & 0xFF]))#)#(OxO9 = OFF_H) writes the upper 4 bits completes the setting of time (remaining bits)


    def set_angle(self, channel, angle):
        angle = max(0, min(180, angle))  # Limit angle between 0 and 180 degrees
        pulse = int(102.4 + (angle * 4.6)) #(4.6 = conversion factor, 102.4 pulse width in microseconds which corresponds to neutral/start position(for servos)conversion factor converts the angle to the corresponidng width in microseconds. Microseconds were chosen because they provide a good level of precision for controlling devices with PWM(pulse width modulation)
        self.__set_pwm__(channel, 0, pulse)#sets pwm value for angle setting on to 0 means that the pins automatically start at HIGH and setting off to pulse means the pwm goes to LOW until the next PWM cycle. So to conclude the servo goes to the desired position at the start because on is set to 0 and setting pulse for the off registers ensure the PWM remaining on low until the start of the next cycle.

def createI2C(id, scl, sda, freq=400000, timeout=50000):
    return I2C(id, scl=Pin(scl), sda=Pin(sda), freq=freq, timeout=timeout)

    

        

      
