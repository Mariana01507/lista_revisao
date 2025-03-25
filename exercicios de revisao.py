import math

# 1. Faça uma função que receba o nome de uma pessoa como entrada e retorne uma saudação.
# Exemplo:
# Boa tarde, Samuel. Seja bem vindo!
def saudacao(nome):
    mensagem = f"Boa tarde, {nome}. Seja bem vindo!"
    return mensagem

# 2. Faça uma função que peça o raio de um círculo e retorne sua área.
import math
def area_circulo(raio):

    return math.pi * raio ** 2

# 3. Faça uma função que converta a temperatura de Fahrenheit para Celsius.
# C = 5 * ((F-32) / 9).
def fahrenheit_para_celsius(fahrenheit):
    
    celsius = 5 * ((fahrenheit - 32) / 9)
    return celsius

# 4. Faça uma função que calcule a multa por excesso de peso de peixes.
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça uma funçao que receba como 
# entrada o peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite 
# e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
# Exemplos de saidas para os parâmetros 70 e 25 respectivamente:
#
# Excesso de peso: 20 kg.
# Multa a pagar: R$ 80.00.
#
# Peso dentro do limite. Nenhuma multa aplicada.
    def calculo_multa(peso):
       limite = 50 
    valor_multa = 4.00  
    
    if peso > limite:
        excesso = peso - limite  
        multa = excesso * valor_multa
        print(f"Excesso de peso: {excesso} kg.")
        print(f"Multa a pagar: R$ {multa:.2f}.")
    else:
        print("Peso dentro do limite. Nenhuma multa aplicada.")


# 5. Faça uma função para calcular a quantidade de tinta necessária para pintar uma área.
# O função deverá receber o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é 
# de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
# galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga no cálculo de litros necessários para cobrir
# a área a ser pintada e sempre arredonde os valores para cima, 
# isto é, considere latas cheias.

## Exemplo de saída para uma área de 100 metros quadrados
# Quantidade de latas de 18L: 2
# Preço total: R$ 160.00
# 
# Quantidade de galões de 3,6L: 6
# Preço total: R$ 150.00
#
# Quantidade de latas: 1, Quantidade de galões: 1
# Preço total: R$ 105.00
import math
def calcular_tinta(area):

    
    cobertura_litro = 6  
    folga = 0.1  
    litro_por_lata = 18  
    litro_por_galao = 3.6  
    preco_lata = 80.00  
    preco_galao = 25.00 
    
    
    area_com_folga = area * (1 + folga)  
    litros_necessarios = area_com_folga / cobertura_litro
    
    latas_necessarias = math.ceil(litros_necessarios / litro_por_lata)
    preco_latas = latas_necessarias * preco_lata
    
   
    galoes_necessarios = math.ceil(litros_necessarios / litro_por_galao)
    preco_galoes = galoes_necessarios * preco_galao
    
   
    latas_mistura = math.floor(litros_necessarios / litro_por_lata)
    litros_restantes = litros_necessarios - (latas_mistura * litro_por_lata)
    galoes_mistura = math.ceil(litros_restantes / litro_por_galao)
    preco_mistura = (latas_mistura * preco_lata) + (galoes_mistura * preco_galao)
    
    
    return (latas_necessarias, preco_latas), (galoes_necessarios, preco_galoes), (latas_mistura, galoes_mistura, preco_mistura)


# 6. Faça uma função que receba dois números e retorne o maior deles.
def maior_numero():
    valor1 = int(input("Digite o primeiro valor:"))
    valor2 = int(input("Digite o segundo valor:"))
    
    if valor1 > valor2:
            print("O maior valor será:" (valor1))
    else:
            print("O maior valor será:"(valor2))
         

# 7. Faça uma função que verifique se uma letra é vogal ou consoante.
def verificar_letra(letra):
    if (letra in("a","e","i","o","u")) :
        return "vogal"
    else: 
        return "consoante"
  
# 8. Faça um Programa que receba três números e retorne o maior deles.
def maior_tres_numeros(a, b, c):
    
    
    return max(a, b, c)


numero1 = 2
numero2 = 86
numero3 = 78

maior = maior_numero(numero1, numero2, numero3)
print(f"O maior número é: {maior}")

# 9. Faça uma função que retorne o menor valor entre três numeros informados.
def produto_mais_barato(a, b, c):
    return min(a, b, c)


numero1 = 2
numero2 = 86
numero3 = 78


menor = produto_mais_barato(numero1, numero2, numero3)
print(f"O menor número é: {menor}")

# 10. Faça uma funçao que retorne uma saudação com base no turno de estudo.
# A entrada deverá ser M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
def saudacao_turno():
    
    if(saudacao) == "M":
        print ("Bom dia!")
    elif(saudacao) == "V":
        print ("Boa Tarde")
    elif  (saudacao) == "N":
        print ("Boa Noite")
    else: 
        print("Expressão Inválida!")


saudacao = input("Digite M para matutino, V para vespertino ou N para noturno:")


# 11. Faça uma função para um caixa eletrônico que informe quantas notas de cada valor serão fornecidas
# ao ser solicitado um saque.
# A função receberá como entrada o valor do saque e e retornará quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo de saída para uma entrada de 346
# Notas fornecidas:
# 3 nota(s) de R$ 100
# 4 nota(s) de R$ 10
# 1 nota(s) de R$ 5
# 1 nota(s) de R$ 1

def caixa_eletronico(saque):
    
    notas = [100, 50, 10, 5, 1]
    
    
    resultado = {}
    
    
    for nota in notas:
        quantidade = saque // nota  
        if quantidade > 0:
            resultado[nota] = quantidade
            saque -= quantidade * nota  
    
    
    print("Notas fornecidas:")
    for nota, quantidade in resultado.items():
        print(f"{quantidade} nota(s) de R$ {nota}")
        

caixa_eletronico(346)



# 12. Desenvolva uma lógica que classifique uma pessoa com base nas respostas sobre um crime.
# A função deverá receber receba a resposta as seguintes perguntas:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

    def classificar_participacao():
    perguntas = ["Telefonou para a vítima?",
        "Esteve no local do crime?",
        "Mora perto da vítima?",
        "Devia para a vítima?",
        "Já trabalhou com a vítima?"
    ]

    respostasPositivas = 0

    for pergunta in perguntas:
        resposta = input(pergunta + " (sim/não): ").lower()
        if resposta == "sim":
            respostasPositivas += 1

    
    if respostasPositivas == 5:
        classificacao = "Assassino"
        
    elif 3 <= respostasPositivas <= 4:
        classificacao = "Cúmplice"
        
    elif respostasPositivas == 2:
        classificacao = "Suspeita"
      
    else:
        classificacao = "Inocente"
        

    print(f"Classificação: {classificacao}")


classificar_participacao()

        

# 13. Faça um Programa que calcule o preço da carne em uma promoção com desconto opcional.
# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
# receberá ainda um desconto de 5% sobre o total da compra. Escreva uma função que receba o tipo e a quantidade de
# carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de
# carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

def calcular_preco_carne(tipo_carne, quantidade_kg, pagamento_com_cartao):
    
    if tipo_carne == "File Duplo":
        preco_kg = 4.90 if quantidade_kg <= 5 else 5.80
    elif tipo_carne == "Alcatra":
        preco_kg = 5.90 if quantidade_kg <= 5 else 6.80
    elif tipo_carne == "Picanha":
        preco_kg = 6.90 if quantidade_kg <= 5 else 7.80

    
    total = preco_kg * quantidade_kg

    
    if pagamento_com_cartao:
        desconto = total * 0.05
        total -= desconto
    else:
        desconto = 0

    
    print("Tipo de carne:", tipo_carne)
    print("Quantidade:", quantidade_kg, "Kg")
    print("Preço total: R$", round(total, 2))
    print("Desconto: R$", round(desconto, 2) if pagamento_com_cartao else 0)
    print("Total a pagar: R$", round(total, 2))


tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra ou Picanha): ")
quantidade_kg = float(input("Digite a quantidade de carne em Kg: "))
pagamento_com_cartao = input("Pagamento no Cartão Tabajara? (sim/não): ").strip().lower() == "sim"

calcular_preco_carne(tipo_carne, quantidade_kg, pagamento_com_cartao)

# 14. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem.
def potencia():
    
    base = int(input("Digite um valor para a base: "))
    expoente = int(input("Digite um valor para o expoente: "))

    
    resultado = 1

    
    for _ in range(abs(expoente)):
        resultado *= base

    
    if expoente < 0:
        resultado = 1 / resultado

    
    print(f"{base} elevado a {expoente} é {resultado}")


potencia()

# 15. Faça um Programa que retorne o menor, maior e a soma de um conjunto de números.

import math

def estatisticas_numeros():
    conjunto = [5,6,8,8]
    menor = min(conjunto)
    maior = max(conjunto)
    soma = sum(conjunto)

    
    print(f"O menor valor é: {menor}")
    print(f"O maior valor é: {maior}")
    print(f"A soma dos valores é: {soma}")


estatisticas_numeros()
    
    

# 16. Faça uma função que valide se uma nota está entre 0 e 10.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
# Exemplos de saídas para as entradas -1 e 5.5 respectivamente:
# Erro: A nota deve estar entre 0 e 10. Tente novamente.
# Nota válida: 5.5

def validar_nota():
    while True:
        
        nota = float(input("Digite o valor da nota: "))
        
        
        if 0 <= nota <= 10:
            print(f"Nota válida: {nota}")
            break  
        else:
            print("Erro: A nota deve estar entre 0 e 10. Tente novamente.")


validar_nota()

# 17. Faça uma funçao que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.
# Exemplos de saídas com as entradas "user" "user" "user123" respectivamente
# "Erro: A senha não pode ser igual ao nome de usuário. Tente novamente."
# "Usuário e senha cadastrados com sucesso!"
def validar_usuario_senha():
    def validar_usuario_senha():
    while True:
        
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        
        
        if usuario == senha:
            print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")
        else:
            print("Usuário e senha cadastrados com sucesso!")
            break  


validar_usuario_senha()

# 18. Faça um Programa que calcule a média aritmética de um conjunto de N notas.
def media_notas():
    import math
def media_notas():
    conjunto = [2,3,4,5,6]
        
    soma = sum(conjunto)
    quantidade = len(conjunto)
    
    media =  soma / quantidade
    print(f"Média: {media}")

media_notas()

# 19. Faça um programa que mostre os n termos da Série a seguir:
#     S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
def calcular_serie():
    
    n = int(input("Digite o número de termos da série: "))
    
    
    soma = 0
    
    
    for k in range(1, n+1):
        numerador = k
        denominador = 2 * k - 1
        termo = numerador / denominador
        soma += termo
        
        
        print(f"{numerador}/{denominador}", end=" ")
        if k < n:
            print("+", end=" ")
        else:
            print("=")
    
   
    print(f"Soma total da série: {soma}")


calcular_serie()

# 20. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
#  A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas 
# dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima 
# informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas.
# Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
# Atleta: João Silva
# Nota: 7.9
# Nota: 8.5
# Nota: 9.4
# Nota: 7.0
# Nota: 8.8
# Nota: 9.8
# Nota: 7.9

# Resultado final:
# Atleta: João Silva
# Melhor nota: 9.8
# Pior nota: 7.0
# Média: 8.50

import math

def calcular_media_ginastica():
    
    nome = input("Digite o nome do atleta: ")

    
    nota1 = float(input("Digite a nota do primeiro jurado: "))
    nota2 = float(input("Digite a nota do segundo jurado: "))
    nota3 = float(input("Digite a nota do terceiro jurado: "))
    nota4 = float(input("Digite a nota do quarto jurado: "))
    nota5 = float(input("Digite a nota do quinto jurado: "))
    nota6 = float(input("Digite a nota do sexto jurado: "))
    nota7 = float(input("Digite a nota do sétimo jurado: "))
    
   
    nota_final = [nota1, nota2, nota3, nota4, nota5, nota6, nota7]
    
    
    menor = min(nota_final)
    maior = max(nota_final)
    
    
    nota_final.remove(menor)
    nota_final.remove(maior)
    
    
    media = sum(nota_final) / len(nota_final)
    
    
    print("\nResultado final:")
    print(f"Atleta: {nome}")
    print(f"Melhor nota: {maior}")
    print(f"Pior nota: {menor}")
    print(f"Média: {media:.2f}")


calcular_media_ginastica()

# 21. Faça um Programa que desenhe uma pirâmide alinhada à esquerda.
def piramide_esquerda():
    def piramide_esquerda():
    
    n = int(input("Digite o número de linhas da pirâmide: "))
    
    
    for i in range(1, n+1):
        
        print('*' * i)


piramide_esquerda()

# 22. Faça um Programa que desenhe uma pirâmide alinhada à direita.
def piramide_direita():
    pass

# 23. Faça um Programa que desenhe duas pirâmides lado a lado.
def piramides_lado_a_lado():
    pass

# 24. Faça um Programa que calcule o troco com a menor quantidade de moedas possível.
def calcular_troco():
    pass

# 25. Faça um Programa que valide um número de cartão de crédito usando o algoritmo de Luhn.
def validar_cartao():
    pass
