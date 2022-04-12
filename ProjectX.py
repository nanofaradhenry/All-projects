print("Hello World")
import code
import time
time.sleep(1)
print("Welcome to Fate ")

code_alpha=input("Please Enter a Password to play Fate : ")

type_pass = input("Enter password to confirm identity:")
if type_pass == code_alpha :
    

    first_question=input("Would you like to START the Game ? :")


if first_question == 'yes'or 'y'or 'Y'or 'YES' :
    time.sleep(1)
    print( """
    You Have Just been contracted by the C.I.B. , otherwise known as he Central Intelligence Board in 
    order to complete a task that will require great mental capacity and focus...
     """)
    time.sleep(10)
elif first_question == 'NO' or 'no' or 'n'or 'N':
    text_exit=input("Press enter to EXIT:")