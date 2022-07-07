import easygopigo3
import time 

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

    right_error *= 1.375
    right_speed += kP * right_error

    return (left_speed, right_speed)


if __name__ == '__main__':
    print('No default test')
