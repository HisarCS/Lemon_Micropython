# Lemon_Micropython
This is the library for controlling Lemon Robots with micropython via the RaspberryPi Pico


Firstly, you must connect your Pico to your computer with the pico cable. Then you must connect the PCA9685 to your Pico. Firstly you must connect the SCL, SDA, VCC and Ground pins of the PCA9685 to your picos General Purpose Input Output(GPIO) pins. You should connect SDA to pin zero, SCL to pin one, VCC to pin 40 and Ground to pin 38 as seen in the image below. Then you must connect a power source(preferably 4.5-5V) to the power pins located on the side of the PCA9685 because the pico only powers the logic gates of the PCA9685.

Secondly, you must prepare the LemonLib library to perform the necessary functions needed to control your robot. First, you must create a folder named Lemon then you must open your computer’s terminal and write cd Lemon. Then, you must write git clone (library link). After completing this process you will have installed the library. Next, you must install the IDE Mu Editor. (Mu editor için gereken adımları ekle). 

This library works for the Lime and Satsuma robots. To control your Lime robot, you must perform the following steps. Firstly, you must import the Lemon library with the following line :

```python

import LemonLib

```

Then you must initialize your I2C 
channel:

‘’’
i2c = I2C(0, scl=Pin(1), sda=Pin(0))’’’

The following function from the I2C class in the machine library takes three arguments. The second and the third one initialize the set pins for the I2C channel. And the first argument sets which I2C channel the PCA9685 is. After that, you must set the I2C channel you have just created for your PCA9685 and also set your PWM frequency.
‘’’python
pca = PCA9685(i2c)
pca.set_pwm_freq(50)
‘’’
You must create a while loop in order to move the fish.
‘’’while True:
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
‘’’

The angle in range functions make the Lime fish move from 0 to 180 and then from 180 to 0 5 degrees at a time. Whilst the pca.set_angle function sets the current angle value created in the loops to the servos on the PCA9685’s first and second channels, the print(angle) function shows you the current angle value which is created by the for loops. Also the time.sleep(0.05) smooths out the movement of the fish by creating a small time interval between each iteration of the loop.

Secondly, to control the Satsuma robot. [Satsuma instructionlarini micropython ultrasonik kodu yazildiktan sonra ekle]
