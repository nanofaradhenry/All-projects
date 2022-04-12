print("Hello World")
import time
time.sleep(1)
print("Welcome to your Budget Calculator")
time.sleep(1)
print("First, I need to know just a little more information")
time.sleep(1)
print("""I am going to ask you a few questions so I can see what your spending looks like """)
time.sleep(1)
mortgage_rent=float(input("How much do you pay monthly on rent or mortgage payments?:"))
time.sleep(1)
food=float(input("How much do you spend monthly on food and health products?:"))
time.sleep(1)
utilities=float(input("""How much do you pay on monthly utilities
ie. phone bill, gas , electricity?: """))
time.sleep(1)
transprt=float(input("""How much do you spend on transportation costs
i.e.gas, insurance, maintenance costs ?:"""))
other=float(input("""Add up any other expenses not mentioned so far, and
 enter them here(i.e. debt,fees,luxury items):"""))
total_costs_monthly=float((mortgage_rent+food+utilities+transprt+other))
string_total_costs_monthly=str(total_costs_monthly)
print("Your expenses add up to"+" "+string_total_costs_monthly)
total_costs_yearly=(total_costs_monthly * 12.0)
yearly_string=str(total_costs_yearly)
print("That's roughly"+" "+yearly_string+" Per year")
time.sleep(1)
monthly_inc=input("Now... please enter your monthly income:")
monthly_inc_str=str(monthly_inc)
monthly_savings=(monthly_inc-total_costs_monthly)
print(monthly_savings)
ending=input("Press any key to exit:")


