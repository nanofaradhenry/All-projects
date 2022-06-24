import time ,sys , os

time.sleep(1);
print("initiating")
time.sleep(1)
print("program"); 

## functions utilized for main program

def welcomefunction():
    joe="Welcome to THE QUEST"
    for char in joe:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)


def startfunction():
    message="A Journey not for the faint of heart"
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)


def dottedfunc():
    animation=print("Going to menu ......")
    for char in animation:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)


### program commence options 
time.sleep(1)
begin=input("Commence Program ? (Y or N on keyboard):")
if begin == 'Y' or 'y':
    welcomefunction()
    print("  ")
    startfunction()
elif begin == 'N' or 'n':
    dottedfunc()
else: input=("Press ANY key to EXIT the program !")
    




    
  




 




