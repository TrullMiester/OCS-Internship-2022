import easygopigo3
import time 

# Proportional motor control, extra compensation for right motor
# Robot naturally veers to the right

def fwd(bot):
  servo = bot.init_servo()
  servo.reset_servo()
  GOAL = 200
  TICKS = 4
  LOOP_GOAL = GOAL / TICKS
  sum_error = 0
  
  kP = 1 
  kI = 0
  kD = 0

  left_speed =  GOAL
  right_speed = GOAL

  bot.reset_encoders(True)
  bot.set_motor_dps(bot.MOTOR_LEFT, left_speed)
  bot.set_motor_dps(bot.MOTOR_RIGHT, right_speed)

  sensor = bot.init_distance_sensor()

  end = time.time() + 60
  while time.time() < end:
    time.sleep(0.25)
    left_position, right_position = bot.read_encoders()
    
    print(left_position, right_position)
    
    bot.reset_encoders(True)
    
    left_error = LOOP_GOAL - left_position
    right_error = LOOP_GOAL - right_position
    
    left_speed += kP * left_error
    
    if right_error > 0:
        right_error *= 1.05

      right_error *= 1.375
    
    right_speed += kP * right_error

    print(left_speed, right_speed)
    
    if sensor.read_mm() < 300: 
        bot.orbit(90)

    bot.reset_encoders(True)
    bot.set_motor_dps(bot.MOTOR_LEFT, left_speed)
    bot.set_motor_dps(bot.MOTOR_RIGHT, right_speed)
  
  bot.stop() 

if __name__ == '__main__':
    bot = easygopigo3.EasyGoPiGo3() 

    fwd(bot)
