num1= float(input("Enter first number:"))
num2= float(input("Enter second number:"))

print("addition=",num1+num2)
print("multiplication=",num1*num2)

if num2!=0:
    print("divsion=",num1/num2)
    print("floor division=",num1//num2)
    print("modulus=",num1%num2)
else:
    print("Division,floor division and modulus are undifined for zero divisor.")
print("Exponential=",num1**num2)