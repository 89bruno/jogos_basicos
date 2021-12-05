""" Jogo de adivinhar o numero secreto """
import random

# Introduçao ao jogo

def jogar():
    print("**************************************\n")
    print("   Bem vindo ao jogo de Adivinhação!  \n")
    print("***************************************\n")
    print("Escolha em qual nível  você quer jogar:\n")
    print("(1) Fácil     (2) Médio    (3) Difícil \n")

    # Escolhendo o nível e sorteando um numero aleatório
    nivel = int(input("Digite o nível:"))
    chances = 0
    numero = random.randrange(1,101)
    tentativa = 0
    pontos = 1000

    if (nivel == 1):
        chances = 15
    elif (nivel == 2):
        chances = 10
    else:
        chances = 5
    print(f' Muito bem, você escolheu o nivel {nivel}.\n',
          f'Logo, você terá {chances} tentativas\n',
          "Caso queira desistir digite 0 \n",
          "Boa sorte!")

    # Chutando o número sorteado(jogando)
    for tentativa in range(1, chances+1):
        print(f'------->Tentativa {tentativa} de {chances}<-------')
        chute    = int(input("Digite sua tentativa: "))
        acertou  = chute == numero
        maior    = chute > numero
        menor    = chute < numero
        desistir = chute == 0
        aviso    = tentativa == chances-1

        if(acertou):
            print(f'Você acertou, sua pontuação foi de: {pontos}!')
            break
        if(desistir):
            print("Você desistiu!")
            break

        else:
            if(maior):
                print("Você errou! O número é menor")
            elif(menor):
                print("Você errou! O número é maior")
            if(aviso):
                print("**********Atenção, esta é sua última chance!**********")
        pontos_perdidos = abs(numero - chute)
        pontos = pontos - pontos_perdidos

    print("Fim de jogo!")
    print(f'O número secreto era {numero}')

if(__name__== "__main__"):
    jogar()