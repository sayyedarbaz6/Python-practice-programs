import math
h = float(input('EnterHeight of cylinder: '))
r= float(input('Radius of cylinder: '))
volume = math.pi * r * r * h
sa = ((2*math.pi*r) * h) + ((math.pi*r**2)*2)
print("Volume is: ", volume)
print("Surface Area is: ", sa)