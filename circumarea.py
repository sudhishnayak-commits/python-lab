import math
radius=float(input("Enter the radius:"))
area=math.pi*radius**2
c=2*math.pi*radius
area_integer=int(area)
print(f"area         :{area:.2f}")
print(f"circumference:{c:.2f}")
print(f"Area as in   :{area_integer}")