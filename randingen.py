#dev --- ma_build.dev
#program to generate text input
###
##
#
import random
add_expression = int
add_more_mesg = str
loop_continue = str
user_name = str
rand_text_user = str
rand_welcome_list = []
def gen_welcome_text():
    global loop_continue
    global gen_randwelcome
    rand_text_1 = "Ohhhh, what a nice name"
    rand_text_2 = "We'd like to welcome you.."
    rand_text_3 = "We do hope you're having a good time..."
    rand_text_4 = "Have a good day ahead.."
    rand_text_5 = "You're doing great, ain't you?"
    rand_welcome_list.append(rand_text_1)
    rand_welcome_list.append(rand_text_2)
    rand_welcome_list.append(rand_text_3)
    rand_welcome_list.append(rand_text_4)
    rand_welcome_list.append(rand_text_5)
    
    gen_randwelcome = random.choice(rand_welcome_list)
    
def add_welcome_text():
    global add_more_mesg
    global gen_randwelcome
    global rand_text_user
    global rand_welcome_list
    add_more_mesg  = input("Add user expression respectively : ")
    rand_welcome_list.append(add_more_mesg)
    if rand_welcome_list.append(add_more_mesg):
        print(f"The expression(s) has been added successfully")
    else:
        print("Something 's probably wrong, I guess..")
    
def accept_user_expresson():
    global add_more_mesg
    global add_expression
    global convert_loop
    global gen_randwelcome
    global loop_continue
    global rand_text_user
    global rand_welcome_list
    #I've made the program more dynamic in this function by making the user 
    #to add more user welcoming messages and generating them randomly in the 
    #output messages.. cool hun
    
    add_expression = int(input("How many more expression(s) do you wanna add? : "))
    for i in range(add_expression):
            i=+1
            add_welcome_text()
        
def welcome():
    global loop_continue
    global gen_randwelcome
    print("_______________________________________")
    print("I'd like to get to know your name...")
    print("_______________________________________")
    user_name = input("Tell me your name please ..:>>:")
    print("_______________________________________")
    print(f"{gen_randwelcome}, {user_name}")
    print("_______________________________________")

def loop_over():
    global loop_continue
    global gen_randwelcome
    global convert_loop
    print("_______________________________________")
    loop_continue = input("Do you wish to continue(yes/no)?? ")
    convert_loop = loop_continue.upper()
    for i in (convert_loop):
        if convert_loop == "YES":
            gen_welcome_text()
            welcome()
            loop_over()
        elif convert_loop == "NO":
            pass
        else:
            print("Invalid expression")
    print("_______________________________________")


    
    
gen_welcome_text()
welcome()
loop_over()
#accept_user_expresson()