a = int(input())
b = int(input())
pessoa = int(input())

distA = abs(a - pessoa)
distB = abs(b - pessoa)

if distA < distB or distA == distB:
    print("A")
else:
    print("B")