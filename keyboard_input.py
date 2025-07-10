

a = 1
b = -3
c = 2

discriminant = b**2 - 4*a*c

if discriminant >= 0:
    root1 = (-b + (discriminant)**0.5) / (2*a)
    root2 = (-b - (discriminant)**0.5) / (2*a)
    print("Roots:", root1, root2)
else:
    print("No real roots")
