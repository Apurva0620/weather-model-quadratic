# stage2.py

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b**2 - 4*a*c

if discriminant >= 0:
    root1 = (-b + (discriminant)**0.5) / (2*a)
    root2 = (-b - (discriminant)**0.5) / (2*a)
    print("Roots:", root1, root2)
else:
    print("No real roots")
