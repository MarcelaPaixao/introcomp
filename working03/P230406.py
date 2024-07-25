v = float(input())

if v > 300:
    print(f"Valor final com desconto: R$ {v*0.7:.2f}")
elif v > 200:
    print(f"Valor final com desconto: R$ {v*0.8:.2f}")
elif v > 100:
    print(f"Valor final com desconto: R$ {v*0.9:.2f}")
else:
    print("Desconto nao foi aplicado.")