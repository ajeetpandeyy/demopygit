from pygame import mixer
import time
from datetime import datetime


def getdate():
    c1 = datetime.now()
    return c1

water_intake = time.time()
eye_ex_intake = time.time()
physical_ex_intake = time.time()

a = 18
b = 24
c = 27

while True:
    print("")
    activate_program_or_check_record = input(
        "If you want to activate program then enter 'ap' or if you want to check records then enter 'cr' or enter 'close' to close the program: ")
    if activate_program_or_check_record == "ap":
        currenttime = time.strftime('%H:%M:%S')
        print(currenttime)
        while True:
            if time.time() - water_intake > a:
                print("Time to drink water.")
                mixer.init()
                mixer.music.load("water.mp3")
                mixer.music.set_volume(0.5)
                mixer.music.play()
                z = input("Enter Done if you had water: ").lower()
                if z == "done":
                    mixer.music.stop()
                    water_intake = time.time()
                    with open("water_drank_record.txt", "a") as op:
                        op.write(str([str(getdate())]) + ": water drank." + "\n")
                        print("Record updated successfully!!")
                        print("")
                elif z == "exit":
                    mixer.music.stop()
                    # to close or exit the program.
                    break
            if time.time() - eye_ex_intake > b:
                print("Time for an eye excercise.")
                mixer.init()
                mixer.music.load("eye.mp3")
                mixer.music.set_volume(0.5)
                mixer.music.play()
                z1 = input("Enter Done if you have if you completed your eye excercise: ").lower()
                if z1 == "done":
                    mixer.music.stop()
                    eye_ex_intake = time.time()
                    with open("eye_ex_record.txt", "a") as op:
                        op.write(str([str(getdate())]) + ": eye exercise done." + "\n")
                        print("Record updated successfully!!")
                        print("")
                elif z1 == "exit":
                    mixer.music.stop()
                    # to close or exit the program.
                    break

            if time.time() - physical_ex_intake > c:
                print("Time for physical excercise.")
                mixer.init()
                mixer.music.load("rest.mp3")
                mixer.music.set_volume(0.5)
                mixer.music.play()
                z2 = input("Enter Done if you have if you completed your physical excercise: ").lower()
                if z2 == "done":
                    mixer.music.stop()
                    physical_ex_intake = time.time()
                    with open("physical_ex_record.txt", "a") as op:
                        op.write(str([str(getdate())]) + ": physical exercise done." + "\n")
                        print("Record updated successfully!!")
                        print("")
                elif z2 == "exit":
                    mixer.music.stop()
                    # to close or exit the program.
                    break
    elif activate_program_or_check_record == "cr":
        def record_check():
            while True:
                r1 = input(
                    "For which record do you want to check :[ w for water_drinking, e for eye_exercise, p for physical_excercise ]: ").lower()
                if r1 == "w":
                    with open("water_drank_record.txt") as op:
                        for i in op:
                            print(i, end="")
                        break
                elif r1 == "e":
                    with open("eye_ex_record.txt") as op:
                        for i in op:
                            print(i, end="")
                        break
                elif r1 == "p":
                    with open("physical_ex_record.txt") as op:
                        for i in op:
                            print(i, end="")
                        break
                else:
                    print(
                        "Please enter a valid input from [ w for water_drinking, e for eye_exercise, p for physical_excercise ].")
                    print("")
                    continue


        record_check()
    elif activate_program_or_check_record == "close":
        break
    else:
        print(
            "Please enter a valid input to activate program then enter 'ap' or if you want to check records then enter 'cr' or enter 'enter' close to close the program as you run the code next time.")
        print("")