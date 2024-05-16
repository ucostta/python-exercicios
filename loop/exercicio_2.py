# Inicializa a contagem de números pares
numeros_pares = 0

# Solicita ao usuário que insira 5 números
for i in range(2):
    numero = int(input("Digite um número inteiro positivo: "))
    
    # Verifica se o número é par e incrementa a contagem, se for o caso
    if numero % 2 == 0:
        numeros_pares += 1

# Exibe o total de números pares digitados
print("O total de números pares digitados é:", numeros_pares)