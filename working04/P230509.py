def eh_primo(n):
    if n < 2:
        return False
    elif n == 2: 
        return True
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
    return True


num = int(input())

if num < 0:
    print("Número inválido, tente novamente")
elif num == 0:
    print("Fim do programa")

for n in range(num):     
    if eh_primo(n):
        print(n, end=" ")
     