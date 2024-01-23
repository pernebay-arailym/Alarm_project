#https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203
from playsound import playsound
import time #module

def alarm(seconds): 
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1) #wait for a second
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 #125 // 60 = 2
        seconds_left = time_left % 60 #125 % 60 = 5

        print(f"{minutes_left}:{seconds_left}")



alarm(10)