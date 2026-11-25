# Exercício 02 - Sistema de acesso a parque de diversões
#
# Objetivo:
# Avaliar as condições de entrada dos visitantes,
# definir valores de ingressos e identificar benefícios
# de acordo com critérios de idade, peso, altura,
# deficiência, condição de estudante e tamanho da família.
#
# Conteúdos praticados:
# - Variáveis e tipos de dados (int, float e bool)
# - Entrada de dados (input)
# - Conversão de tipos
# - Operadores relacionais
# - Operadores lógicos (and, or e not)
# - Estruturas condicionais (if, elif e else)
# - Estruturas condicionais aninhadas


nome=input("Digite seu nome:")
idade=int(input("Digite sua idade:"))
altura=float(input("Qual é a sua altura?"))
peso=float (input("Digite o seu peso:"))
dia = input("Digite o dia da visita (segunda, terça, quarta,quinta,sexta, sábado):")
deficiencia=(True if input("Possui alguma deficiência? (1-sim, 0-não):")=="1" else False)
estudante=(True if input("É estudante?(1-sim, 0-não:)")=="1" else False)
familia=int (input("Quantas pessoas vieram com você? (Incluindo você):"))

if idade<5 or peso>140 or altura<1:
    print("Entrada proibida")
    if idade<5:
        print("Crianças com 5 anos de idade ou menos não podem entrar")
    if peso>140:
        print("Peso acima de 140kg")
    if altura<1:
        print("Altura abaixo de 1 metro")

else:
        if idade<=6 or deficiencia=="1":
            print("Entrada gratuita")

        elif idade>=60 or estudante:
            print("Você irá pagar apenas meia entrada")

        elif familia>=4 and dia=="terça" or dia=="quarta":
             print("Promoção especial")

        else:
             print("Valor normal do ingresso.")

        if idade>=14 and altura>=1.50 and peso<=120:
             print("Brinquedos radicais")

        elif idade>=60 or deficiencia:
             print("Prioridade na fila")

        elif familia>=6 and idade>6 and deficiencia=="0":
             print("Visitante VIP")

        elif familia>=6 and not (idade<=6 or deficiencia=="1"):
             print("Visitante VIP")

        elif  idade>=14 and altura>=1.50 and peso<=120 and dia=="sabado" or dia=="domingo":
             print("Acesso Premium")

             
