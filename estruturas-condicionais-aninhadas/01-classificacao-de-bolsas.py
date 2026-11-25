# Exercício 01 - Classificação de bolsas
#
# Objetivo:
# Classificar candidatos de acordo com
# critérios acadêmicos e socioeconômicos.
#
# Conteúdos praticados:
# - Variáveis e tipos de dados
# - Input e conversão de dados
# - Operadores relacionais
# - Operadores lógicos
# - Estruturas condicionais aninhadas

nome=input("Digite seu nome:")
idade=int(input("Digite sua idade:"))
media=float(input("Digite sua média geral:"))
falta=int(input("Digite sua quantidade de faltas nesse semestre:"))
renda=float(input("Digite sua renda familiar:"))
projetos = int(input("Quantos projetos de pesquisa você já realizou:"))
voluntario=(True if input ("Faz atividade voluntário? '1-sim' ou '0-não'") == 's' else False)

if media<6 or falta>25 or idade<16:
    print(f"{nome} Você foi desclassificado porque não atendeu aos critérios de classificação")
    if media<6:
        print("Média inferior a 6")
    if falta>25:
        print("")
    if idade<16:
        print("Menor que 16")

else:
    if media>=9 or falta<25 or idade>16 or renda<=2500 or projetos>=1 or voluntario:
        print("Você foi classificado para receber bolsa integral")

    elif media>=7.5 or renda<=4000 or falta<15:
        print("Você foi classificado para receber bolsa parcial")
    else:
        print("Cadastro reserva")

    if media>=9.5 and projetos>=3:
        print("Candiddato destaque")

    if renda<=1800 and voluntario:
        print("Prioritário")
   
      
      





