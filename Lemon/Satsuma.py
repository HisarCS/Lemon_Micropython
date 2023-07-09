import LemonLib

i2c = I2C(0, scl=Pin(1), sda=Pin(0))  
pca = PCA9685(i2c)
pca.set_pwm_freq(50)

while True:
        pca.set_angle(0, 40)
        pca.set_angle(1, 90)
        pca.set_angle(2, 40)
        pca.set_angle(3, 50)
        pca.set_angle(4, 90)

        time.sleep(0.5)

        pca.set_angle(0, 20)
        pca.set_angle(1, 110)
        pca.set_angle(2, 20)
        pca.set_angle(3, 90)
        pca.set_angle(4, 50)
      

