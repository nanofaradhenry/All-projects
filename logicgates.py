

#testing out logic gates

output_value_zero=(0)
output_value_one=(1)
print("AND Gate")
and_gate_a=input("Enter a 1 or 0:")
and_gate_b=input("Enter a 1 or 0:")

if and_gate_a ==0 and and_gate_b ==0:
    print(output_value_zero)
elif and_gate_a == 0 and and_gate_b ==1:
    print(output_value_zero)
elif and_gate_a==1 and and_gate_b==0:
    print(output_value_zero)
elif and_gate_a ==1 and and_gate_b==1:
    print(output_value_one)
else: print("Invalid ")
