with open("input_multiple.txt", "r") as f:
    for line in f:
        a, b, c, x = map(float, line.strip().split())
        y = a * x**2 + b * x + c
        print(f"Input: a={a}, b={b}, c={c}, x={x} → Predicted y = {y}")
