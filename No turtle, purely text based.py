import time

# Declare global variables
done_before1 = 0
standard_case = 0
Abit_AB_PB4 = 0
Intel_80286_12 = 0
Matrox_Millennium = 0
Ram16mb = 0
StorageHDD500mb = 0
PSU45w = 0
small_fan = 0
tutorial1 = 0


def start1():
    start_question1 = input("Custom PC Tycoon - Are you ready to start? ")
    start2()


def start2():
    global done_before1, standard_case, Abit_AB_PB4, Intel_80286_12, Matrox_Millennium, Ram16mb, StorageHDD500mb, PSU45w, small_fan, tutorial1
    tutorial_prompt1 = input("Let's get you greeted with the basics of the game. ")
    tutorial_prompt2 = input("Of course to build a PC you need parts, we will supply you with your first pair of parts for this tutorial. ")
    tutorial1 = 1
    standard_case = 1
    Abit_AB_PB4 = 1
    Intel_80286_12 = 1
    Matrox_Millennium = 1
    Ram16mb = 1
    StorageHDD500mb = 1
    PSU45w = 1
    small_fan = 1
    done_before1 = 0
    main_build_func()


def main_build_func():
    global done_before1, standard_case, Intel_80286_12, Matrox_Millennium, small_fan, Ram16mb, PSU45w, Abit_AB_PB4
    if tutorial1 == 1:
        if done_before1 == 0:
            tutorial_prompt3 = input("Finally, there are 8 different components you have right now, we supplied you with 1 of each. These include, Cases, Motherboards, CPUs, GPUs, RAM, Memory, PSUs, and Fans. ")
            actual_prompt = input("Which of these 8 do you want to choose first? ")
            if actual_prompt.lower() == "cases" or actual_prompt.lower() == "case":
                if standard_case == 1:
                    case_input_thing1 = input(f"You have {standard_case} case, labelled, 'standard case' do you want to use it? ")
                    if case_input_thing1.lower() == 'y' or case_input_thing1.lower() == 'yes':
                        standard_case = 0
                        print("Standard case used.")
                        time.sleep(1.5)
                    else:
                        print("idk what to do with this rn")
            else:
                print("You must have a case to put this in first")
        else:
            while True:
                actual_prompt = input("Which component do you want to use ")
                if actual_prompt.lower() == "motherboard" or actual_prompt.lower() == "motherboards":
                    motherboard_input_thing1_idk = input(f"You have {Abit_AB_PB4} motherboard, labelled, 'Abit AB PB4' do you want to use it? ")
                    if motherboard_input_thing1_idk.lower() == "y" or motherboard_input_thing1_idk.lower() == "yes":
                        print("The Abit AB PB4 has been inserted and secured into the computer case")
                        if Abit_AB_PB4 == 0 and Intel_80286_12 == 0 and small_fan == 0 and Matrox_Millennium == 0 and Ram16mb == 0 and PSU45w == 0 and StorageHDD500mb == 0:
                            print("idk rn")
                            break
                        else:
                            time.sleep(1)


start1()
