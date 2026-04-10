# Entrada de dados
# Em Python, podemos usar a função input() para receber dados do usuário. A função input() lê uma linha de texto do usuário e retorna como uma string. Podemos armazenar esse valor em uma variável para usá-lo posteriormente em nosso programa.
# Exemplo de entrada de dados:
# Solicitando ao usuário que digite seu nome
nome = input("Digite seu nome: ")
# Exibindo o nome digitado pelo usuário 
print("Olá, " + nome + "! Bem-vindo ao curso de Python.")
# Podemos também solicitar outros tipos de dados, como números. No entanto, a função input() sempre retorna uma string, então precisamos converter o valor para o tipo desejado.
# Solicitando ao usuário que digite sua idade
idade_str = input("Digite sua idade: ")
# Convertendo a string para um número inteiro
idade = int(idade_str)
# Exibindo a idade digitada pelo usuário
print("Você tem " + str(idade) + " anos.")
# Podemos realizar operações com os dados recebidos do usuário
idade_ano_que_vem = idade + 1
print("No próximo ano, você terá " + str(idade_ano_que_vem) + " anos.")
# Também podemos solicitar outros tipos de dados, como números decimais, usando a função float() para converter a string.
# Solicitando ao usuário que digite um número decimal
preco_str = input("Digite o preço do produto: ")
# Convertendo a string para um número decimal
preco = float(preco_str)
# Exibindo o preço digitado pelo usuário
print("O preço do produto é: R$ " + str(preco))
