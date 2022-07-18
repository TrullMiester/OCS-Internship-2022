import easygopigo3
import time, math

# Proportional motor control, extra compensation for right motor
# Robot naturally veers to the right

# Turning functions are essentially the same as given functions 
# only difference when I implemented was that I played around with 
# numbers until turning got more accurate 

def fwd(bot, goal=200, left_speed=200, right_speed=200):
    TICKS = 2
    LOOP_GOAL = goal / TICKS

    kP = 1 
    kI = 0
    kD = 0

    bot.reset_encoders(True)
    bot.set_motor_dps(bot.MOTOR_LEFT, left_speed)
    bot.set_motor_dps(bot.MOTOR_RIGHT, right_speed)

    time.sleep(0.5)

    left_position, right_position = bot.read_encoders()

    left_error = LOOP_GOAL - left_position
    left_speed += kP * left_error

    right_error = LOOP_GOAL - right_position
    right_speed += kP * right_error

    print(left_speed, left_position)
    print(right_speed, right_position)

    return (left_speed, right_speed, left_position, right_position)

def newfwd(bot, dps):
    bot.reset_encoders(True)

    bot.set_motor_position(bot.MOTOR_LEFT + bot.MOTOR_RIGHT , dps)

    left = False
    right = False
    while not (left and right):
        left_pos, right_pos = bot.read_encoders()
        if left_pos >= dps:
            bot.set_motor_dps(bot.MOTOR_LEFT, 0)
            left = True
        if right_pos >= dps:
            bot.set_motor_dps(bot.MOTOR_RIGHT, 0)
            right = True
    
    print(bot.read_encoders())

def fwdfwd(bot, leftdps, rightdps):
    bot.reset_encoders(True)
    
    bot.set_motor_position(bot.MOTOR_LEFT, leftdps)
    time.sleep(0.01)
    bot.set_motor_position(bot.MOTOR_RIGHT, rightdps)
    time.sleep(0.01)
    
    left, right = False, False
    while not (left and right):
        left_pos, right_pos = bot.read_encoders()
        if left_pos >= leftdps:
            bot.set_motor_dps(bot.MOTOR_LEFT, 0)
            left = True
        if right_pos >= rightdps:
            bot.set_motor_dps(bot.MOTOR_RIGHT, 0)
            right = True
            
    print(bot.read_encoders(), leftdps, rightdps)

def turn_ccw(bot, deg): 
    ORBIT_DIAMETER = 115 #in mm 
    WHEEL_DIAMETER = 65  #in mm 

    mm_needed = (ORBIT_DIAMETER * math.pi) * (deg / 360)
    degrees_needed = (mm_needed / (WHEEL_DIAMETER * math.pi)) * 360 

    bot.reset_encoders()

    left_position, right_position = -degrees_needed, degrees_needed
    
    bot.set_motor_position(bot.MOTOR_LEFT, left_position)
    bot.set_motor_position(bot.MOTOR_RIGHT, right_position)

    while not bot.target_reached(left_position, right_position):
        time.sleep(0.05)

def turn_cw(bot, deg): 
    ORBIT_DIAMETER = 115  #in mm 
    WHEEL_DIAMETER = 65  #in mm 

    mm_needed = (ORBIT_DIAMETER * math.pi) * (deg / 360)
    degrees_needed = (mm_needed / (WHEEL_DIAMETER * math.pi)) * 360 

    bot.reset_encoders()

    left_position, right_position = degrees_needed, -degrees_needed
    
    bot.set_motor_position(bot.MOTOR_LEFT, left_position)
    bot.set_motor_position(bot.MOTOR_RIGHT, right_position)

    while not bot.target_reached(left_position, right_position):
        time.sleep(0.05)

if __name__ == '__main__':
    bot = easygopigo3.EasyGoPiGo3()

    turn_cw(bot, 360)
