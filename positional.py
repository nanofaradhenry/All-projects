#positional vs keyword arguments
import time
import random
import webbrowser
import tkinter

print("Hello World")
print("Welcome to Global Discovery")

mex_fact_1=("""Mexico city, the capital of mexico, was once home to the Aztec capital of 
tenochtitlan""")
mex_fact_2=webbrowser.open("https://www.nationalgeographic.org/media/dia-de-los-muertos/")

random_mex_fact_set=random.choice[mex_fact_1,mex_fact_2]

def mexico_data():
    print("Welcome to Mexico !")
    time.sleep(1)
    print("A country that is full of amazing food and culture")

from tkinter import *
root=Tk()
root.geometry('100x100')
btn= Button(root,text='Access WeB',bd='5',command=root.destroy)
btn.pack(side='top')
root.mainloop()



print("Just type in a  country that you would like to learn more about!")
time.sleep(1)
enter_city_country=input("Enter the  country:")
if enter_city_country=='Mex'or'mexico'or'm':
    mexico_data(random_mex_fact_set)
