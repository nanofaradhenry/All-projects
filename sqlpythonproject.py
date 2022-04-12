
import time
import random

print("Hello World")
print("Welcome to Module 3B Term Dictionary")

transistor_terms={
    "transistor":"A device that can be used in variable resistance, electronic switching, and signal amplification",
    "bias":"Commonly referred to as voltage; The average DC voltage or current used to establish a transistor circuits used to establish circuits for a quiescent or static ocnditions",
    "common amplifier classes":"Made of four types of classes ; A AB B and C",
    "capacitor":"A device that can hold charge in an electrostatic field , it passes AC and blocks DC",
    
    

}


phrases=["That word is gone like the wind","That word is out of this world"," Try Google..."]

enter_term=input("What word are you looking for?:")

if enter_term in transistor_terms:
    print(transistor_terms[enter_term])



elif enter_term != transistor_terms:
    print("Try Again")
    time.sleep(3)
    enter_term_again=input("Try typing it in again or try another definition:")
    if enter_term_again in transistor_terms:
        print(transistor_terms[enter_term_again])
    elif enter_term_again != transistor_terms:
        print("Hmmm... We might not have that one")
        time.sleep(2)
        print("Third times a charm right?")
        third_try=input("Give it one more shot or enter another term:")
        if third_try !=transistor_terms:
            time.sleep(1)
            print(random.choice(phrases))