from lime import limeServo

servo = limeServo(0)
servo2 = limeServo(1)

while True:
            # Move the servo back and forth
            for angle in range(0, 180, 10):
                servo.set_angle(angle)
                servo2.set_angle(angle)
                time.sleep(0.5)

            for angle in range(180, 0, -10):
                servo.set_angle(angle)
                servo2.set_angle(angle)
                time.sleep(0.5)