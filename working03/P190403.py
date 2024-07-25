a = float(input())
b = float(input())
c = float(input())

delta = pow(b,2) - 4*a*c
if delta > 0:
    print("DUAS")
if delta == 0:
    print("UMA")
else:
    print("NENHUMA")