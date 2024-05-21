senha_correta = 123456
nome = "Renan"
tentativa = 3

while tentativa > 0:
    senha_digitada = int(input("Digite sua senha"))
    if senha_digitada == senha_correta:
        print(f"Olá {nome}. Seja bem-vindo ao nosso banco")
        break
    else:
        tentativa -= 1
        if tentativa > 0:
            print(f"Senha incorreta! Voce ainda tem {tentativa} tentativas." )
        else:
            print(f"{nome}, sua senha foi bloqueada! Por favor, dirija-se a um dos nossos caixas.")
            break