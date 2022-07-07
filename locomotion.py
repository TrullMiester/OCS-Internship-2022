import motion
import easygopigo3

def main():
    bot = easygopigo3.EasyGoPiGo3()
    
    servo = bot.init_servo()
    servo.reset_servo()

    distance_sensor = bot.init_distance_sensor()

    goal, left_speed, right_speed = 1000, 1000, 1000 #starting speed
    while distance_sensor.read_mm() > 300:
        left_speed, right_speed = motion.fwd(bot, goal, left_speed, right_speed)
    
    bot.stop()

if __name__ == '__main__':
    main()


