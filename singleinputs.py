with open("input_single.txt", "r") as f:
    lines = f.readlines()
    a = float(lines[0])
    b = float(lines[1])
    c = float(lines[2])
    x = float(lines[3])

y = a * x**2 + b * x + c
print(f"Predicted weather value for day {x} is: {y}")
