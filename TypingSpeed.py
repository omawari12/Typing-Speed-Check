from time import *
import random as r
def mistake(partest,usertest): # this function is for checking the error in the 
    error = 0                   #user input string and the provided srting.
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1 
    return error

def speed_time(time_s, time_e, userinput): # this function is for calculating the time or speed
    time_delay = time_e - time_s
    time_R =  round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)


while True:
    ck = input("Ready to Test (yes/no) =")
    if ck == "yes":
        test  = ["A paragraph is a self contained unit of discourse in writing dealing with  a particular point or idea",
                "My name is Akash", "Welcome to Check a your typing Speed"]
        test1 = r.choice(test)
        print("Typing Speed Calculator")
        print(test1)
        print()
        print()
        time1 = time()
        test_Input = input("Enter : ")
        time2 = time()
        print('Speed = ',speed_time(time1, time2, test_Input),"Word/Sec")
        print("Error = ", mistake(test1, test_Input ))
    
    elif ck == "no":
        print("Thank You")
        break

    else:
        print("WrongInput")