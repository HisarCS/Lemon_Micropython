import LemonLib

i2c = I2C(0, scl=Pin(1), sda=Pin(0))  
pca = PCA9685(i2c)
pca.set_pwm_freq(50)


while True:
      for angle in range:(0, 180, 5):
          pca.set_angle(0, angle)
          pca.set_angle(1, angle)
          print(angle)
          time.sleep(0.05)

     for angle in range(180, 0, -5):
          pca.set_angle(0, angle)
          pca.set_angle(1, angle)
          print(angle)
          time.sleep(0.05)