# Solicita ao usuário para inserir a resistência e a corrente
resistencia = float(input("Digite o valor da resistência em ohms (Ω): "))
corrente = float(input("Digite o valor da corrente em amperes (A): "))

# Calcula a tensão usando a fórmula U = R * i
tensao = resistencia * corrente

# Exibe o resultado da tensão
print("A tensão é:", tensao, "volts (V)")

# Solicita ao usuário para inserir a tensão e a corrente
tensao = float(input("Digite o valor da tensão em volts (V): "))
corrente = float(input("Digite o valor da corrente em amperes (A): "))

# Calcula a tensão usando a fórmula U = R * i
resistencia = tensao * corrente

# Exibe o resultado da tensão
print("A resistencia é:", resistencia, "ohms (Ω)")

# Solicita ao usuário para inserir a resistência e a tensão
resistencia = float(input("Digite o valor da resistência em ohms (Ω): "))
tensao = float(input("Digite o valor da tensão em volts (V): "))

# Calcula a corrente usando a fórmula U = R * i
corrente = resistencia * tensao

# Exibe o resultado da corrente
print("A corrente é:", corrente, "amperes (A)")