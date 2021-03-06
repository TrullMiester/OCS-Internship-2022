import motion
import easygopigo3
import math

def main():
    bot = easygopigo3.EasyGoPiGo3()
    
    servo = bot.init_servo()
    servo.reset_servo()

    distance_sensor = bot.init_distance_sensor()

    
    orientation = 0 #degrees, straight forward is 0
    x_distance = 0
    y_distance = 0 
    total_distance = 0
    
    ORBIT_DIAMETER = 115
    WHEEL_DIAMETER = 65
    
    
    while distance_sensor.read_mm() > 300:
        motion.newfwd(bot, 200)
        
        left_position, right_position = bot.read_encoders()
        ddist =  (min(left_position, right_position) / 360) * (WHEEL_DIAMETER * math.pi)
        total_distance += ddist
        
        x_distance += (ddist * math.cos(math.radians(orientation)))
        y_distance += (ddist * math.sin(math.radians(orientation)))
        
        print(total_distance/10)
        
    bot.stop()

if __name__ == '__main__':
    main()


