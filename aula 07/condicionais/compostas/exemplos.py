# Condicionais compostas
# As estruturas condicionais compostas permitem que o programa tome decisões mais complexas, utilizando as palavras-chave elif (else if) e else. Com essas estruturas, podemos verificar múltiplas condições e executar diferentes blocos de código dependendo do resultado. Aqui estão alguns exemplos de condicionais compostas:
# Exemplo 1: Verificar se um número é positivo, negativo ou zero
numero = 0
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
# Exemplo 2: Verificar a faixa etária de uma pessoa
idade = 25
if idade < 18:
    print("Você é menor de idade.")
elif idade < 65:
    print("Você é adulto.")
else:
    print("Você é idoso.")


# Exemplo 3: Verificar o dia da semana
dia = "Segunda-feira"
if dia == "Segunda-feira":
    print("Hoje é segunda-feira.")
elif dia == "Terça-feira":
    print("Hoje é terça-feira.")
elif dia == "Quarta-feira":
    print("Hoje é quarta-feira.")
elif dia == "Quinta-feira":
    print("Hoje é quinta-feira.")
elif dia == "Sexta-feira":
    print("Hoje é sexta-feira.")
else:
    print("Hoje é fim de semana.")
# Exemplo 4: Verificar o resultado de um exame
nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muito bom")
elif nota >= 70:
    print("Bom")
elif nota >= 60:
    print("Suficiente")
else:
    print("Insuficiente")
