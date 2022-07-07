import motion
import easygopigo3

def main():
    bot = easygopigo3.EasyGoPiGo3()
    
    servo = bot.init_servo()
    servo.reset_servo()

    distance_sensor = bot.init_distance_sensor()

    left_speed, right_speed = 200, 200 #starting speed
    while distance_sensor.read_mm() > 300:
        left_speed, right_speed = motion.fwd(bot, 200, left_speed, right_speed)
    
    bot.stop()

if __name__ == '__main__':
    main()


