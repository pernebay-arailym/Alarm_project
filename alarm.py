#https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203
from playsound import playsound
import time #module

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds): 
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1) #wait for a second
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 #125 // 60 = 2
        seconds_left = time_left % 60 #125 % 60 = 5

        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")


    playsound("alarm.mp3")

minutes = int(input("how many minutes to wait"))
seconds = int(input("How many seconds to wait"))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)