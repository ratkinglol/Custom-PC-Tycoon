import turtle

global screen, starttext1, titletext
screen = turtle.Screen()
def start1():
    global starting_screen, titletext, starttext1, screen
    starting_screen = 1
    screen.bgcolor("black")
    screen.setup(1500, 900)
    screen.title("Custom PC Tycoon V0.01")
    # Create a turtle for the title
    titletext = turtle.Turtle()
    titletext.speed(0)
    titletext.penup()
    titletext.hideturtle()
    titletext.goto(0, 400)
    neon_orange1 = "#FF5F1F"
    light_green1 = "#65fe08" 
    titletext.color(neon_orange1) 
    titletext.write("Custom PC Tycoon", align="center", font=("Courier", 50, "normal"))
    titletext.penup()
    titletext.goto(0, 400)
    starttext1 = turtle.Turtle()
    starttext1.speed(0)
    starttext1.penup()
    starttext1.hideturtle()
    starttext1.goto(-300, 200)
    starttext1.color(light_green1)
    starttext1.write("Start", align="center", font=("Courier", 50, "normal"))


def starting_game1():
    global starting_screen, standard_case, Abit_AB_PB4, Intel_80286_12, Matrox_Millennium, Ram16mb, StorageHDD500mb, PSU45w, small_fan, tutorial1
    starting_screen = 0
    tutorial1 = 1
    tutorial_text1 = turtle.textinput("", "Let's get you greeted with the basics of this tycoon game, press enter or 'OK' to continue.")
    tutorial_text2 = turtle.textinput("", "Of course to build a PC you need parts, we will supply you with your first pair of parts for this tutorial.")
    standard_case = 1
    Abit_AB_PB4 = 1
    Intel_80286_12 = 1
    Matrox_Millennium = 1
    Ram16mb = 1
    StorageHDD500mb = 1
    PSU45w = 1
    small_fan = 1
    main_build_func()

start_data_text1 = [
'testing 1, clicked at coordinates -398.0 261.0',
'testing 1, clicked at coordinates -197.0 260.0',
'testing 1, clicked at coordinates -197.0 216.0',
'testing 1, clicked at coordinates -403.0 219.0'
]
cases_data_text1 = [
'testing 1, clicked at coordinates -712.0 437.0',
'testing 1, clicked at coordinates -592.0 435.0',
'testing 1, clicked at coordinates -594.0 412.0',
'testing 1, clicked at coordinates -711.0 412.0'
]
motherboard_data_text1 = [
'testing 1, clicked at coordinates -548.0 438.0',
'testing 1, clicked at coordinates -260.0 439.0',
'testing 1, clicked at coordinates -258.0 410.0',
'testing 1, clicked at coordinates -547.0 410.0'
]
cpu_data_text1 = [
'testing 1, clicked at coordinates -224.0 437.0',
'testing 1, clicked at coordinates -129.0 438.0',
'testing 1, clicked at coordinates -129.0 410.0',
'testing 1, clicked at coordinates -221.0 410.0'
]
gpu_data_text1 = [
'testing 1, clicked at coordinates -99.0 437.0',
'testing 1, clicked at coordinates -5.0 437.0',
'testing 1, clicked at coordinates -5.0 411.0',
'testing 1, clicked at coordinates -99.0 411.0'
]
d = "DEBUG:"


def start_click1():
    titletext.clear()
    starttext1.clear()
    starting_game1()


def click_mechanic1(x, y):
    print("testing 1, clicked at coordinates", x, y)
    if starting_screen == 1:
        if -400 <= x <= -197 and 216 <= y <= 261:
            print(d, "Clicked start")
            start_click1()
    elif tutorial1 == 1:
        if -712 <= x <= -593 and 412 <= y <= 436:
            print(d, "Cases clicked, tutorial")
            Cases_click_func1()
            #Not done yet
        elif -548 <= x <= -259 and 410 <= y <= 439:
            print(d, "Motherboards clicked, tutorial")
            #Not done yet
        elif -223 <= x <= -129 and 410 <= y <= 438:
            print(d, "CPUs clicked, tutorial")
            #Not done yet
        elif -99 <= x <= -5 and 411 <= y <= 437:
            print(d, "GPUs clicked, tutorial")



screen.onscreenclick(click_mechanic1)


def square_thing_case_thing_idk1():
    square_thingidk1 = turtle.Turtle()
    square_thingidk1.speed(0)
    square_thingidk1.color('white')
    square_thingidk1.penup()
    square_thingidk1.hideturtle()
    square_thingidk1.goto(585, 400)
    square_thingidk1.shape('square')
    # Draw a square using the turtle
    square_thingidk1.showturtle()
    square_thingidk1.pendown()
    # Draw the square
    for _ in range(4):
        square_thingidk1.forward(50)
        square_thingidk1.right(90)
    square_thingidk1.hideturtle()


def main_build_titles1():
    # Case text
    case_text1 = turtle.Turtle()
    case_text1.speed(0)
    case_text1.color("white")
    case_text1.penup()
    case_text1.hideturtle()
    case_text1.goto(-650, 400)
    case_text1.write("Cases", align="center", font=("Courier", 30, "normal"))
    # Motherboard text
    motherboard_text1 = turtle.Turtle()
    motherboard_text1.speed(0)
    motherboard_text1.color("white")
    motherboard_text1.penup()
    motherboard_text1.hideturtle()
    motherboard_text1.goto(-400, 400)
    motherboard_text1.write("Motherboards", align="center", font=("Courier", 30, "normal"))
    # CPU Text
    cpu_text1 = turtle.Turtle()
    cpu_text1.speed(0)
    cpu_text1.color("white")
    cpu_text1.penup()
    cpu_text1.hideturtle()
    cpu_text1.goto(-175, 400)
    cpu_text1.write("CPUs", align="center", font=("Courier", 30, "normal"))
    #GPU Text
    gpu_text1 = turtle.Turtle()
    gpu_text1.speed(0)
    gpu_text1.color("white")
    gpu_text1.penup()
    gpu_text1.hideturtle()
    gpu_text1.goto(-50, 400)
    gpu_text1.write("GPUs", align="center", font=("Courier", 30, "normal"))
    #RAM Text
    ram_text1 = turtle.Turtle()
    ram_text1.speed(0)
    ram_text1.color("white")
    ram_text1.penup()
    ram_text1.hideturtle()
    ram_text1.goto(75, 400)
    ram_text1.write("RAM", align="center", font=("Courier", 30, "normal"))
    # Memory Text
    memory_text1 = turtle.Turtle()
    memory_text1.speed(0)
    memory_text1.color("white")
    memory_text1.penup()
    memory_text1.hideturtle()
    memory_text1.goto(225, 400)
    memory_text1.write("Memory", align="center", font=("Courier", 30, "normal"))
    # PSU Text
    psu_text1 = turtle.Turtle()
    psu_text1.speed(0)
    psu_text1.color("white")
    psu_text1.penup()
    psu_text1.hideturtle()
    psu_text1.goto(375, 400)
    psu_text1.write("PSUs", align="center", font=("Courier", 30, "normal"))
    # Fan Text
    fan_text1 = turtle.Turtle()
    fan_text1.speed(0)
    fan_text1.color("white")
    fan_text1.penup()
    fan_text1.hideturtle()
    fan_text1.goto(500, 400)
    fan_text1.write("Fans", align="center", font=("Courier", 30, "normal"))


def Cases_click_func1():
    if tutorial1 == 1:
        standard_case_text1 = turtle.Turtle()
        standard_case_text1.speed(0)
        standard_case_text1.color("white")
        standard_case_text1.penup()
        standard_case_text1.hideturtle()
        standard_case_text1.goto(610, 385)
        standard_case_text1.write("Standard", align="center", font=("Courier", 7, "normal"))
        standard_case_text2 = turtle.Turtle()
        standard_case_text2.speed(0)
        standard_case_text2.color("white")
        standard_case_text2.penup()
        standard_case_text2.hideturtle()
        standard_case_text2.goto(610, 375)
        standard_case_text2.write("Case", align="center", font=("Courier", 7, "normal"))
        standard_case_text3 = turtle.Turtle()
        standard_case_text3.speed(0)
        standard_case_text3.color("white")
        standard_case_text3.penup()
        standard_case_text3.hideturtle()
        standard_case_text3.goto(610, 360)
        standard_case_text3.write(f"{standard_case}", align="center", font=("Courier", 10, "normal"))
        square_thing_case_thing_idk1()


def main_build_func():
    if tutorial1 == 1:
        main_build_titles1()





start1()
turtle.mainloop()
