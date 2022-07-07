import easygopigo3
import time, math

# Proportional motor control, extra compensation for right motor
# Robot naturally veers to the right
# I will use the orbit function and not turn_degrees

def fwd(bot, goal=200, left_speed=200, right_speed=200):
    TICKS = 4
    LOOP_GOAL = goal / TICKS

    kP = 1 
    kI = 0
    kD = 0

    bot.reset_encoders(True)
    bot.set_motor_dps(bot.MOTOR_LEFT, left_speed)
    bot.set_motor_dps(bot.MOTOR_RIGHT, right_speed)

    time.sleep(0.25)

    left_position, right_position = bot.read_encoders()

    left_error = LOOP_GOAL - left_position
    left_speed += kP * left_error

    right_error = LOOP_GOAL - right_position
    if right_error > 0:
        right_error *= 1.05

    right_error *= (2.75 * (goal / 400))
    right_speed += kP * right_error

    print(left_speed, left_position)
    print(right_speed, right_position)

    return (left_speed, right_speed)

def turn(bot, deg): 
    ORBIT_DIAMETER = 115 #in mm 
    WHEEL_DIAMETER = 65  #in mm 

    mm_needed = (ORBIT_DIAMETER * math.pi) * (deg / 360)
    degrees_needed = (mm_needed / (WHEEL_DIAMETER * math.pi)) * 360 

    bot.reset_encoders()

    bot.set_motor_position(bot.MOTOR_LEFT, -degrees_needed)
    bot.set_motor_position(bot.MOTOR_RIGHT, degrees_needed)

if __name__ == '__main__':
    bot = easygopigo3.EasyGoPiGo3()
    turn(bot,90)
