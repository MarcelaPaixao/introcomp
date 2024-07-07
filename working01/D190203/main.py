sec = int(input())

mes = 2592000
dia = 86400
hora = 3600
min = 60

print(int(sec/mes))
print(int((sec%mes)/dia))
print(int(((sec%mes)%dia)/hora))
print(int((((sec%mes)%dia)%hora)/min))
print(int((((sec%mes)%dia)%hora)%min))
