print("Hello World")
import time
import random
print("Welcome to the GET TO KNOW YOU 3000")
time.sleep(1)
print("I am your personal chatbot")
#functions that will allow for input

enter_name=input("Please enter name:")

def greet_with_name(input_name):
    print(f"Hello {input_name}")
    print(f"How do you do {input_name}?")

greet_with_name(enter_name)

random_color=random.choice(['red','orange','yellow','green','blue','indigo','violet'])
enter_color=input("What is your favorite color?:")
def color_choice(input_color):
    time.sleep(1)
    print(f"Wow { input_color} is a wonderful color isn't it?")
    time.sleep(1)
    print("But...I think"+" "+random_color+" " +"is pretty neat in my opinion")

color_choice(enter_color)
time.sleep(1)
print("Anyhow, I think it may be my bedtime")
time.sleep(2)
exit_now=input("You may now exit if you please:")








    

