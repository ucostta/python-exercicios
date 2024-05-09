import json
import urllib.request

# Solicitar ao usuário o CEP
cep = input('Digite o CEP: ')

# Construir na URL de consulta
url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    # Fazer a requisição
    response = urllib.request.urlopen(url)

    # Ler o conteudo da resposta
    data = response.read().decode('utf-8')

    # Converter JSON em dicionario Python
    endereço = json.loads(data)

    #Verificar se a consulta foi bem sucedida
    if endereço.get('erro'):
        print("CEP não encontrado")
    else:
        # Armazenar informações em variáveis
        logradouro = endereço['logradouro']
        complemento = endereço['complemento']
        bairro = endereço['bairro']
        cidade = endereço['localidade']
        estado = endereço['uf']

        # Exibir informações do endereço na tela
        print(f"Logradouro: {logradouro}")
        print(f"Complemento: {complemento}")
        print(f"Bairro: {bairro}")
        print(f"Cidade: {cidade}")
        print(f"Estado: {estado}")

    # Fechar a conexão
    response.close()
except Exception as e:
    print(f"Erro: {e}")