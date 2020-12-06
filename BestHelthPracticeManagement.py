#####################################################
#       Healthy Programmer Reminder System          #
#       Developer: Ajeet Pandey                     #
#                                                   #
####################################################

print(" Healthy Programmer Reminder System  ")

from pygame import mixer

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(3)
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

if __name__ == '__main__':
    musiconloop("water.mp3","stop")
