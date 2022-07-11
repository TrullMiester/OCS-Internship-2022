import easygopigo3
import time, math
import motion as m

# scan area in front of robot, find the closest "wall"
# then precisely turn to be perpindicular, then turn 90
# degreees to be parallel to the wall and continue on

def scan(bot, distance_sensor):
    min_distance = 3000 # max distance sensor reading
    min_degrees = 0

    m.turn_ccw(bot, 90) 
    current_deg = 0

    while current_deg <= 180:
        current_distance = distance_sensor.read_mm() 
        
        if current_distance <= min_distance:
            min_degrees  = current_deg
            min_distance = current_distance
        
        if current_deg < 180: 
            m.turn_cw(bot, 10)
        
        current_deg += 10
    
    m.turn_ccw(bot, 90-min_degrees)




def main():
    bot = easygopigo3.EasyGoPiGo3()
    servo = bot.init_servo()
    distance_sensor = bot.init_distance_sensor()

    servo.reset_servo()

    DURATION = 30  # seconds
    SPEED = 200    # degrees per iteration

    end = time.time()  + DURATION 

    while time.time() < end:
        distance = distance_sensor.read_mm() 

        if distance < 300: 
            scan(bot, distance_sensor)
        else:
            m.fwd(bot, SPEED) 


if __name__ == '__main__':
    main()
