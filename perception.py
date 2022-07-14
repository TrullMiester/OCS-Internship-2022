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

# Scans in a 90 degree window from the rear of the robot
def rear_scan(bot, distance_sensor): 
    current_rotation = 0
    minimum_distance = 3000
    best_degrees = 0
    STEP = 15
    END = 90
    DIAMETER = 190
    
    while current_rotation <= END:
        current_distance = distance_sensor.read_mm()
        current_distance += (DIAMETER * math.cos(math.radians(current_rotation)))

        if current_distance <= minimum_distance:
            best_degrees = current_rotation
            minimum_distance = current_distance
        
        if current_rotation < END:
            m.turn_cw(bot, STEP)
        
        current_rotation += STEP
    
    m.turn_ccw(bot, END-best_degrees)
    print(best_degrees)
            
def scan_two(bot, turned):
    forward_distance = bot.init_distance_sensor()
    rear_distance = bot.init_distance_sensor('AD2')

    rear = rear_distance.read_mm()
    forward = forward_distance.read_mm()

    # Take readings from distance sensors to determine future orientation
    # Case 1: Rear reading says close to wall, maybe like less than ~300-500 mm?
    #         No change in orientation, keep going forward 
    # Case 2: Forward distance sensor says very close to wall, less than ~150-300 mm.
    #         perform a scan using the rear distance sensor to keep following wall.
    # Case 3: Forward distance sensor says wall is in the distance, not 3000mm, 
    #         no change in orientation, keep going forward
    # Case 4: Rear distance sensor says wall is in the distance, not 3000 mm, 
    #         turn in direction of distance sensor
    # Case 5: Rear and forward distance sensor say nothing close, turn in direction
    #         of distance sensor, make sure not to turn twice until facing another wall 
    # Priority of cases to make sure no collisions take place is 2 -> 1 -> 3 -> 4 -> 5

    result = True
    if forward <= 150 or rear <= 150:
        rear_scan(bot, rear_distance)
    elif forward > 2000 and rear < 3000:
        m.turn_ccw(bot, 90)
    elif rear >= 3000 and forward >= 3000 and not turned:
        m.turn_cw(bot, 90)
        result = False
    
    return result  


def main():
    bot = easygopigo3.EasyGoPiGo3()
    servo = bot.init_servo()
    distance_sensor = bot.init_distance_sensor()

    servo.reset_servo()

    DURATION = 30  # seconds
    SPEED = 200    # degrees per iteration
    
    result = False

    end = time.time()  + DURATION 

    while time.time() < end:
        result = scan_two(bot, result)
        m.newfwd(bot, SPEED)

if __name__ == '__main__':
    main()
