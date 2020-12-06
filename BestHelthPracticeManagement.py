#####################################################
#       Healthy Programmer Reminder System          #
#       Developer: Ajeet Pandey                     #
#                                                   #
####################################################

print(" Healthy Programmer Reminder System  ")

from pygame   import mixer
from datetime import datetime
from time     import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:  # when we just play and exit then program didn't get enough time
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylog.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")  #return Activity performed & its Time stamp

if __name__ == '__main__':
    #  musiconloop("water.mp3","stop")
    init_water = time()
    init_eye   = time()
    init_exercise = time()
    watersecs = 5
    exsec = 10
    eyesecs = 20

    while True:
        if time() - init_water > watersecs:
            print(f"water drinking time. Enter 'drank' to stop alarm")
            musiconloop("water.mp3",'drank')
            init_water = time() #initializing again
            log_now("Drank water at: ")
        if time() - init_eye > eyesecs:
            print(f" Eye exercise time Enter 'doneeye' to stop alarm")
            musiconloop("eye.mp3",'doneeye')
            init_eye = time() #initializing again
            log_now("Eye relaxed at: ")
        if time() - init_exercise > exsec:
            print(f"Physical Activity Time. Enter 'donephy' to stop alarm")
            musiconloop("rest.mp3",'donephy')
            init_exercise = time() #initializing again
            log_now("Physical Activity done at: ")

