import time
# Declare global variables
done_before1 = 0
standard_case = 0
Abit_AB_PB4 = 0
Intel_80286_12 = 0
Matrox_Millennium = 0
Ram16mb = 0
StorageHDD500mb = 0  # Initialize StorageHDD500mb
PSU45w = 0
small_fan = 0
tutorial1 = 0
standard_case_price = 10
Abit_AB_PB4_price = 25
Intel_80286_12_price = 30
Matrox_Millennium_price = 15
Ram16mb_price = 5
StorageHDD500mb_price = 15
PSU45w_price = 15
small_fan_price = 3
sell_price1 = 0
money_idk1 = 0
clear_case_price = 20
ventilated_case_price = 40

def get_price1():
    global sell_price1
    if tutorial1 == 1:
        sell_price1 = 118
    else:
        print("idk rn")


def tutorial_done1():
    global money_idk1, standard_case
    useless_text_thing1 = input("There are 1 place you can go currently, the electronics store. Would you like to go there? ")
    if useless_text_thing1.lower() == "y":
        print("You go to the electronics store.")
        time.sleep(1)
        print("  _______")
        print(' /       \ ')
        print("|  SHOP   |")
        print("|   ___   |")
        print("|  |   |  |")
        print("|  |___|  |")
        print("|_________|")
        time.sleep(1)
        print("You enter the electronics store.")
        time.sleep(1)
        useless_text_thing2 = input("You see 8 sections of the store, labelled, Cases, Motherboards, CPUs, GPUs, RAM, Memory, PSUs, and Fans, where would you like to go? ")
        if useless_text_thing2.lower() == "case" or useless_text_thing2.lower() == "cases" or useless_text_thing2.lower() == "c":
            print("Currently there are 3 different types of cases in stock, Standard Cases, Clear Cases, And Ventilated Cases.")
            time.sleep(2)
            useless_text_thing3 = input(f"Which one do you want? (Standard case is {standard_case_price} dollars, the Clear Case is {clear_case_price} dollars, the Ventilated Case is {ventilated_case_price} dollars) : ")
            if useless_text_thing3.lower() == "standard case" or useless_text_thing3.lower() == "standard" or useless_text_thing3.lower() == "sc":
                if money_idk1 >= standard_case_price:
                    money_idk1 = money_idk1 - standard_case_price
                    print("You bought the Standard Case")
                    time.sleep(1)
                    print('  ________')
                    print(' /       /|')
                    print('/_______/ |')
                    print('|  ___  | |')
                    print('| |   | | |')
                    print('| |___| | |')
                    print('|       | |')
                    print('|_______|/')
                    print('Computer Case Bought!')
                    time.sleep(0.75)
                    standard_case = standard_case + 1
                    print(f"New balance is {money_idk1} dollars")
        elif useless_text_thing2.lower() == "cpu" or useless_text_thing3.lower() == "cpus" or useless_text_thing3.lower() == "c":
            print("Currently there are 3 different CPUs in stock, the Intel 80286 12, ERROR:UNKNOWN, and ERROR:UNKNOWN.")
            time.sleep(2)
            useless_text_thing4 = input(f"Which one do you want? (The Intel 80286 12 is {Intel_80286_12_price} dollars) : ")
            if useless_text_thing4.lower() == "intel 80286 12" or useless_text_thing4.lower() == "intel" or useless_text_thing4.lower() == "intel 80286" or useless_text_thing4.lower() == "i81":
                if money_idk1 >= Intel_80286_12_price:
                    money_idk1 = money_idk1 - Intel_80286_12_price
                    print("You bought the Intel 80286 12.")
    else:
        print("idk rn")
    

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


def tutorial_podium1():
    global sell_price1
    if tutorial1 == 1:
        sell_price1 = 118
        podium_every_minute1 = sell_price1 / 10
        print(podium_every_minute1)
    


def tutorial_computer_built1():
    global sell_price1, money_idk1
    while True:
        tutorial_text_thing_idk1 = input("You finished your first computer, you can put it on the podium to generate money over time or sell it right now to be able to buy better parts, what do you want to do? (podium for podium, sell for sell) : ")
        if tutorial_text_thing_idk1.lower() == "sell" or tutorial_text_thing_idk1.lower() == "s":
            get_price1()
            text_thingy_idk_input1 = input(f"The computer you are going to sell is worth {int(sell_price1)} dollars, do you want to sell? ")
            if text_thingy_idk_input1.lower() == "y" or text_thingy_idk_input1.lower() == "yes":
                money_idk1 = int(sell_price1)
                print(f"You have {money_idk1} dollars.")
                time.sleep(1)
                print("idk rn")
            break
        elif tutorial_text_thing_idk1 == "podium" or tutorial_text_thing_idk1 == "p":
            tutorial_podium1()
            break


def main_build_func():
    global done_before1, standard_case, Intel_80286_12, Matrox_Millennium, small_fan, Ram16mb, PSU45w, Abit_AB_PB4, StorageHDD500mb
    if tutorial1 == 1:
        if done_before1 == 0 and standard_case == 1:
            while True:
                tutorial_prompt3 = input("Finally, there are 8 different components you have right now, we supplied you with 1 of each. These include, Cases, Motherboards, CPUs, GPUs, RAM, Memory, PSUs, and Fans. ")
                actual_prompt = input("Which of these 8 do you want to choose first? ")
                if actual_prompt.lower() == "cases" or actual_prompt.lower() == "case":
                    if standard_case == 1:
                        case_input_thing1 = input(f"You have {standard_case} case, labelled, 'standard case' do you want to use it? ")
                        if case_input_thing1.lower() == 'y' or case_input_thing1.lower() == 'yes':
                            standard_case = 0
                            print("Standard case used.")
                            time.sleep(1.5)
                            done_before = 1
                            main_build_func()
                            break
                        else:
                            print("idk what to do with this rn")
                else:
                    print("You must have a case to put this in first")
        else:
            while True:
                actual_prompt = input("Which component do you want to use?: ")
                if actual_prompt.lower() == "motherboard" or actual_prompt.lower() == "motherboards":
                    motherboard_input_thing1_idk = input(f"You have {Abit_AB_PB4} motherboard, labelled, 'Abit AB PB4' do you want to use it? ")
                    if motherboard_input_thing1_idk.lower() == "y" or motherboard_input_thing1_idk.lower() == "yes":
                        print("The Abit AB PB4 has been inserted and secured into the computer case")
                        Abit_AB_PB4 = 0
                        time.sleep(2)
                        if Abit_AB_PB4 == 0 and Intel_80286_12 == 0 and small_fan == 0 and Matrox_Millennium == 0 and Ram16mb == 0 and PSU45w == 0 and StorageHDD500mb == 0:
                            print("idk rn")
                            break
                elif actual_prompt.lower() == "cpu" or actual_prompt.lower() == "cpus":
                    if Abit_AB_PB4 == 1:
                        print("You can't place a CPU without a motherboard")
                        time.sleep(2)
                    else:
                        cpu_input_thing1_idk = input(f"You have {Intel_80286_12} CPU, labelled, 'Intel 80286 12' do you want to use it? ")
                        if cpu_input_thing1_idk.lower() == "yes" or cpu_input_thing1_idk.lower() == "y":
                            if Intel_80286_12 == 0:
                                print("You don't have a CPU")
                                time.sleep(1)
                            else:
                                print("The Intel 80286 12 has been inserted and secured onto the motherboard")
                                Intel_80286_12 = 0
                                time.sleep(2)
                elif actual_prompt.lower() == "quit" or actual_prompt.lower() == "q" or actual_prompt.lower() == "x":
                    break
                elif actual_prompt.lower() == "gpu" or actual_prompt.lower() == "gpus":
                    if Abit_AB_PB4 == 1:
                        print("You can't place a GPU without a Motherboard.")
                        time.sleep(2)
                    else:
                        gpu_input_thing1 = input(f"You have {Matrox_Millennium} GPU, labelled 'Matrox Millennium' do you want to use it? ")
                        if gpu_input_thing1.lower() == "yes" or gpu_input_thing1.lower() == "y":
                            print("The Matrox Millennium has been placed and secured onto the motherboard")
                            Matrox_Millennium = 0
                            time.sleep(2)
                elif actual_prompt.lower() == "ram" or actual_prompt.lower() == "rams":
                    if Abit_AB_PB4 == 1:
                        print("You can't place RAM without a motherboard")
                        time.sleep(2)
                    else:
                        ram_input_thing1 = input(f"You have {Ram16mb} stick of RAM, labelled, 'RAM 16 MB' do you want to use it? ")
                        if ram_input_thing1.lower() == "yes" or ram_input_thing1.lower() == "y":
                            Ram16mb = 0
                            print("The 16 MB of RAM was placed and secured onto the motherboard")
                            if Abit_AB_PB4 == 0 and Intel_80286_12 == 0 and small_fan == 0 and Matrox_Millennium == 0 and Ram16mb == 0 and PSU45w == 0 and StorageHDD500mb == 0:
                                tutorial_computer_built1()
                                break
                            else:
                                time.sleep(2)
                elif actual_prompt.lower() == "memory" or actual_prompt.lower() == "mem" or actual_prompt.lower() == "hdd" or actual_prompt.lower() == "ssd":
                    mem_input_thing1 = input(f"You have {StorageHDD500mb} HDD, labelled, 'HDD Memory, 500 MB' do you want to use it? ")
                    if mem_input_thing1.lower() == "y" or mem_input_thing1.lower() == "yes":
                        print("The 500 MB HDD was placed and secured into the computer case.")
                        StorageHDD500mb = 0
                        time.sleep(2)
                elif actual_prompt.lower() == "power supply" or actual_prompt.lower() == "psu" or actual_prompt.lower() == "power supplies" or actual_prompt.lower() == "psus":
                    psu_input_thing1 = input(f"You have {PSU45w} PSU, labelled, 'Power Supply, 45 W' do you want to use it? ")
                    if psu_input_thing1.lower() == "y" or psu_input_thing1.lower() == "yes":
                        print("The Power Supply was placed and secured into the computer case")
                        PSU45w = 0
                        time.sleep(2)
                elif actual_prompt.lower() == "fan" or actual_prompt.lower() == "fans":
                    fan_input_thing1 = input(f"You have {small_fan} fan, labelled, 'Small Fan' do you want to use it? ")
                    if fan_input_thing1.lower() == "y" or fan_input_thing1.lower() == "yes":
                        print("The Small Fan was placed and secured into the computer case")
                        small_fan = 0
                        time.sleep(2)
                elif actual_prompt.lower() == "skip":
                    tutorial_computer_built1()
                    break


start1()
