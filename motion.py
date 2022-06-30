import easygopigo3 as easy
import time 

# PID controlled function to move the bot forward, goal is 60 rpm.
# Currently I have no clue how I will make this function non-blocking,
# so this will contain not only the fwd functionality but also the 
# constant distance checking. To stop I will just use the built in 
# stop function.

def fwd(bot):
  bot.reset_encoders(True)
  
  dist_sensor = bot.init_distance_sensor()
    
  GOAL = 360
  sum_error = 0
  
  kP = 0.02
  kI = 0
  kD = 0

  left_speed = 360
  right_speed = 360
  
  bot.set_motor_dps(bot.MOTOR_LEFT, left_speed)
  bot.set_motor_dps(bot.MOTOR_RIGHT, right_speed)

  time.sleep(1)
  while dist_sensor.read_mm() > 150:
    left_position, right_position = bot.read_encoders()
    
    left_error = GOAL - left_position
    right_error = GOAL - right_position
    
    left_speed += kP * left_error
    right_speed += kP * right_error
    
    bot.set_motor_dps(bot.MOTOR_LEFT, left_speed)
    bot.set_motor_dps(bot.MOTOR_RIGHT, right_speed)
  
  bot.stop()
    
    
