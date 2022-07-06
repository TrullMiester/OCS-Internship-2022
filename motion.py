import easygopigo3
import time 

#

def fwd(bot):
  GOAL = 250 
  TICKS = 1
  LOOP_GOAL = GOAL / TICKS
  sum_error = 0
  
  kP = 1 
  kI = 0
  kD = 0

  left_speed = 250 
  right_speed = 250

  bot.reset_encoders(True)
  bot.set_motor_dps(bot.MOTOR_LEFT, left_speed)
  bot.set_motor_dps(bot.MOTOR_RIGHT, right_speed)

  end = time.time()+25
  while time.time() < end:
    time.sleep(1)
    left_position, right_position = bot.read_encoders()
    print(left_position, right_position)
    bot.reset_encoders(True)
    
    left_error = LOOP_GOAL - left_position
    right_error = LOOP_GOAL - right_position
    
    left_speed += kP * left_error
    right_speed += kP * right_error * 2

    print(left_speed, right_speed)
    
    bot.set_motor_dps(bot.MOTOR_LEFT, left_speed)
    bot.set_motor_dps(bot.MOTOR_RIGHT, right_speed)

  
  bot.stop()
    
    
