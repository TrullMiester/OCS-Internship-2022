import easygopigo3 as easy 
import time
import os 

if __name__ == '__main__':
    print("running")
    gpg = easy.EasyGoPiGo3() 

    gpg.forward() 
    time.sleep(1)
    gpg.backward()
    time.sleep(1)

    gpg.set_speed(100)
    gpg.forward() 
    time.sleep(1)
    gpg.backward()
    time.sleep(1)

    gpg.set_speed(500)
    gpg.forward() 
    time.sleep(1)
    gpg.backward()
    time.sleep(1)

    gpg.stop()


