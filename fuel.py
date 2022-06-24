

import time , sys 
print("Welcome to Trip Fuel Cost Calculator")


mpg=input("Enter vehicle Miles Per Gallon:")
time.sleep(1)
tanksz=input("Enter vehicle Tank Size in Gallons:")
time.sleep(1)
gasprice=input("Enter Current Gas Price:")
time.sleep(1)
distance=input("Enter trip distance in Miles:")


fulltanmil=(float(mpg)*float(tanksz));
fulltankcost=(float(gasprice)*float(tanksz))
tripcostvalue=(fulltankcost*float(distance)/fulltanmil)
tripcostrounded=round(tripcostvalue,2)
tripcoststring=str(tripcostrounded)
monchar=str('$')

endscript=("Your total Trip Cost Estimate(USD):"+" "+monchar+" "+tripcoststring)

for char in endscript:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.10)

quartercost=(float(fulltankcost/4))
quarterstr=str(quartercost);
halfcost=(float(quartercost*2))
halfstr=str(halfcost);
threefourthcost=(float(halfcost+quartercost))
threfourthstr=str(threefourthcost);
fulltankstr=str(fulltankcost)

print("""

Cost to Fill certain amounts of Tank:

""")
print("Cost of FUll tank :"+" "+fulltankstr)
print("Cost of 3/4 tank  :"+" "+threfourthstr)
print("Cost of 1/2 tank  :"+" "+halfstr)
print("Cost of 1/4 tank  :"+" "+quarterstr)



