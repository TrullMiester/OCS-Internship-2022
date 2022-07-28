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
    minimum_distance = 3000 # Max distance sensor reading
    best_degrees = 0
    STEP = 15
    END = 90
    DIAMETER = 190
    
    while current_rotation <= END:
        current_distance = distance_sensor.read_mm()
        
        #compensation for the movement of the distance sensor
        current_distance += (DIAMETER / 2 * math.cos(math.radians(current_rotation)))

        if current_distance <= minimum_distance:
            best_degrees = current_rotation
            minimum_distance = current_distance
        
        if current_rotation < END:
            m.turn_cw(bot, STEP)
        
        current_rotation += STEP
    
    m.turn_ccw(bot, END-best_degrees)
    
    print(best_degrees)
    return minimum_distance

# Returns the distance left motor and right motor are supposed to turn
def scan_two(bot, fwdsensor, rearsensor, speed, dist):
    # Take readings from front and rear distance sensor to determine 
    # movement of robot. Ideal distance is 200-400mm and will be linear
    # compensation.
    # Case 1: Front sensor says very close to wall, perform scan
    # Case 2: Rear sensor says very close to wall , left motor turn more
    # Case 3: Rear sensor says very far from wall, right motor turn more
    # Case 4: Rear sensor says wall very far away (maybe 1500+ mm?), move  
    #         1 bot length forward, then turn in direction of sensor
    # This should allow for better movement than previous commits
    
    forward = fwdsensor.read_mm()
    rear = rearsensor.read_mm()

    print(forward, rear)

    left = speed
    right = speed

    newdist = dist

    if forward <= 150:
        newdist = rear_scan(bot, rearsensor) 
        left = 0
        right = 0
    elif rear < dist:
        left += (speed * ((dist - rear) / (dist * 3 / 2))) 
    elif rear > dist and rear < 3 * dist:
        right += (speed * ((rear - dist) / (dist * 3 / 2)))
    elif dist > 3 * dist:
        m.newfwd(bot, 350)
        m.turn_ccw(bot, 90)
        while rear_distance.read_mm() > 3 * dist:
            m.newfwd(bot, 100)
    else:
        pass 

    return (left, right, newdist)

def main():
    bot = easygopigo3.EasyGoPiGo3()
    servo = bot.init_servo()

    fwd_sensor = bot.init_distance_sensor()
    rear_sensor = bot.init_distance_sensor('AD2')

    servo.reset_servo()

    DURATION = 60  # seconds
    SPEED = 100    # degrees per iteration
    distance = rear_sensor.read_mm() # # of mm away from wall
    
    result = False

    end = time.time()  + DURATION 


    while time.time() < end:
        left, right, distance = scan_two(bot, fwd_sensor, rear_sensor, SPEED, distance)

        print(left, right, distance)

        m.fwdfwd(bot, left, right)

if __name__ == '__main__':
    main()
