from Lemon import PCA9685, createI2C
from time import sleep

i2c = createI2C(0, scl=1, sda=0)
pca = PCA9685(i2c)
pca.set_pwm_freq(50)

while True:
     for angle in range(0, 180, 5):
          pca.set_angle(0, angle)
          pca.set_angle(1, angle)
          sleep(0.05)

     for angle in range(180, 0, -5):
          pca.set_angle(0, angle)
          pca.set_angle(1, angle)
          sleep(0.05)