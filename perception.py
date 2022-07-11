import easygopigo3
import time, math
import motion as m

def main():
    bot = easygopigo3.EasyGoPiGo3()
    servo = bot.init_servo()
    distance_sensor = bot.init_distance_sensor()


if __name__ == '__main__':
    main()