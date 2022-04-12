print("Hello World")
#paint surface area calculator

enter_height=int(input("Please enter wall height:"))
enter_width=int(input("Please enter wall width:"))

def calc_ul(height,width):
    print("You will need approximatlely" +" "+str(round(height*width/5))+" "+"Cans of paint !")

calc_ul(height=enter_height,width=enter_width)
    







