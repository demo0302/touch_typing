from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed)

if __name__ == "__main__":
    while True:
        ck = input("Ready to test: yes/no")
        ck = ck.lower()
        if ck == "yes":
            test = [
                "A touch typing program is a valuable tool designed to improve typing skills by teaching users how to type without looking at the keyboard. By providing exercises and lessons, these programs focus on enhancing typing speed, accuracy, and technique.",
                "A touch typing program is a specialized tool crafted to train individuals in proficient keyboard typing without relying on sight. These programs offer structured lessons, exercises, and drills that emphasize correct finger positioning and keystroke accuracy. By gradually building muscle memory and reinforcing proper techniques",
            ]

            test1 = r.choice(test)

            print(" ***** typing speed *****")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input(" Enter : ")
            time_2 = time()

            print('Speed: ', speed_time(time_1, time_2, testinput), "w/sec")
            print("Error: ", mistake(test1, testinput))
        elif ck == "no":
            print("Thank you")
            break
        else:
            print("Wrong choice!!! Choose again")
