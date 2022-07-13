import easygopigo3
import time, math
import motion as m

# scan area in front of robot, find the closest "wall"
# then precisely turn to be perpindicular, then turn 90
# degreees to be parallel to the wall and continue on

def scan(bot, distance_sensor):
    START = 30
    END = 180 - START
    STEP = 10
    min_distance = 3000 # max distance sensor reading
    min_degrees = 0

    m.turn_ccw(bot, 90-START) 
    current_deg = 0
    final_deg = 0

    while current_deg <= END:
        current_distance = distance_sensor.read_mm() 
        
        if current_distance <= min_distance:
            min_degrees  = current_deg
            min_distance = current_distance
        
        if current_deg < END: 
            m.turn_cw(bot, STEP)
            
        final_deg = current_deg
        current_deg += STEP 
    
    m.turn_ccw(bot, final_deg-min_degrees-90)

    print(min_degrees)

def scan_two(bot):
    forward_distance = bot.init_distance_sensor()
    rear_distance = bot.init_distance_sensor('AD2')

    servo = bot.init_servo()
    servo.rotate_servo(0)

    rear = rear_distance.read_mm()
    forward = forward_distance.read_mm()

    if rear < 300:
        m.turn_cw(bot, 0)
    elif forward < 150:
        if rear > 600:
            m.turn_cw(bot, 90)
        else:
            scan(bot, forward_distance)

def main():
    bot = easygopigo3.EasyGoPiGo3()
    servo = bot.init_servo()
    distance_sensor = bot.init_distance_sensor()

    servo.reset_servo()

    DURATION = 30  # seconds
    SPEED = 200    # degrees per iteration

    end = time.time()  + DURATION 

    while time.time() < end:
        scan_two(bot)
        m.newfwd(bot, SPEED)

if __name__ == '__main__':
    main()
