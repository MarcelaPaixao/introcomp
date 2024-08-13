num = int(input())

soma = 0

for div in range(1,num):     
    if num % div == 0:
        soma += div
if soma == num:
    print("Eh perfeito.")
else:
    print(f"{num} nao eh perfeito.")

     