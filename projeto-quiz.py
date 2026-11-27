#Projeto - Quiz de conhecimentos gerais
#Objetivo:Desenvolver um quiz interativo com perguntas de conhecimentos gerais, contabilização de pontos e possibilidade de jogar novamente.

#Conteúdos praticados:
#- Variáveis e tipos de dados
#- Input e conversão/tratamento de dados
#- Operadores relacionais
#- Operadores lógicos
#- Estruturas condicionais (if, elif e else)
#- Estruturas de repetição (while)
#- Validação de entradas
#- Contadores e acumuladores


jogar_novamente="S"
while jogar_novamente=="S":
    pontos=0

    nome_jogador=input("Digite seu nome:")
    print(f"Seja bem-vindo(a), {nome_jogador}!")

    answer_user=input("Vamos começar?(S/N)").strip().upper()    

    while answer_user not in ["S","N"]:
        print("Você digitou um valor inválido")
        print("Tente novamente")
        answer_user=input("Vamos começar?(S/N)").strip().upper()
    
    if answer_user=="S":    
        print('''
    Qual é o país conhecido como Terra do Sol Nascente?
    A) China
    B) Japão
    C) Coreia do Sul
    D) Tailândia  ''')
        
        resposta=input("Resposta:").strip().upper()

        if resposta=="B":
            pontos+=25
            print('Resposta Correta!')
            print("O Japão recebeu esse apelido porque está localizado a leste da Ásia, na direção de onde o sol nasce.")
        else:
            print("Resposta incorreta!")
            print("A resposta correta é letra (B) Japão.")
            print("O Japão recebeu esse apelido porque está localizado a leste da Ásia, na direção de onde o sol nasce.")
        print('''
    Qual é o maior oceano do planeta?
    A) Atlântico
    B) Índico
    C) Pacífico
    D) Ártico''')
        resposta=input("Resposta:").strip().upper()
        if resposta=="C":
            pontos+=25
            print("Resposta Correta!")
            print("O Oceano Pacífico é o maior e mais profundo oceano da Terra.")
        else:
            print("Resposta Incorreta!")
            print("A resposta correta é letra (C) Pacífico.")
            print("O Oceano Pacífico é o maior e mais profundo oceano da Terra.")
        print('''
    Quantos ossos possui, aproximadamente, o corpo humano adulto?
    A) 106
    B) 206
    C) 306
    D) 406''')
        resposta=input("Resposta:").strip().upper()
        if resposta=="B":
            pontos+=25
            print("Resposta Correta!")
            print("Um adulto possui, geralmente, 206 ossos, que sustentam o corpo e protegem os órgãos.")
        else:
            print("Resposta Incorreta!")
            print("A resposta correta é letra (B) 206.")
            print("Um adulto possui, geralmente, 206 ossos, que sustentam o corpo e protegem os órgãos.")
        print('''
    4. Qual é a capital da Austrália?
    A) Sydney
    B) Melbourne
    C) Canberra
    D) Brisbane''')
        resposta=input("Resposta:").strip().upper()
        if resposta=="C":
            pontos+=25
            print("Resposta Correta!")
            print("Canberra foi escolhida como capital para ser uma solução intermediária entre Sydney e Melbourne, duas grandes cidades australianas.")
        else:
            print("Resposta Incorreta!")
            print("A resposta correta é letra (C) Canberra.")
            print("Canberra foi escolhida como capital para ser uma solução intermediária entre Sydney e Melbourne, duas grandes cidades australianas.")
        if pontos == 100:
            print(f"100 pontos - Parabéns, {nome_jogador}! Você acertou todas!")
        elif pontos == 75:
            print(f"75 pontos - Mandou muito bem, {nome_jogador}! Você está quase lá!")
        elif pontos == 50:
            print(f"50 pontos - Bom trabalho, {nome_jogador}! Você acertou metade!")
        elif pontos == 25:
            print(f"25 pontos - Não desista, {nome_jogador}! Você pode melhorar!")
        elif pontos == 0:
            print(f"0 pontos - Parece que precisamos estudar um pouquinho mais, {nome_jogador}!")
        jogar_novamente=input("Jogar novamente? (S/N)").strip().upper()
   
    elif answer_user=="N":
        print("Fim do quiz!")
        break


