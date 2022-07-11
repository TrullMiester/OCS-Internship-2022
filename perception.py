import easygopigo3
import time, math
import motion as m

# scan area in front of robot, find the closest "wall"
# then precisely turn to be perpindicular, then turn 90
# degreees to be parallel to the wall and continue on

def scan(bot):
    min_distance = 3000     # max distance sensor reading
    min_degrees  = 0        # position of robot with closest distance  

def main():
    bot = easygopigo3.EasyGoPiGo3()
    servo = bot.init_servo()
    distance_sensor = bot.init_distance_sensor()

    servo.reset_servo()

    DURATION = 60  # seconds
    SPEED = 200    # degrees per iteration

    end = time.time()  + DURATION 

    while time.time() < end:
        distance = distance_sensor.read_mm() 

        if distance < 300: 
            scan(bot)
        else:
            m.fwd(bot, SPEED) 


if __name__ == '__main__':
    main()