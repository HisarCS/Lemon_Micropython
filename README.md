# Lemon_Micropython
This is the library for controlling Lemon Robots with micropython via the RaspberryPi Pico

Firstly to use this library you must clone the repository
```
git clone https://github.com/HisarCS/Lemon_Micropython.git)https://github.com/HisarCS/Lemon_Micropython.git
```
After clonnig the repository you must connect your hardware. Firstly, you must connect your Pico to your computer with the pico cable. Then you must connect the PCA9685 to your Pico. Firstly you must connectthe SCL, SDA, VCC and Ground pins of the PCA9685 to your picos General Purpose(GP) pins. You should connect SDA to pin zero, SCL to pin one, VCC to pin 40 and Ground to pin 38 as seen in the image below
