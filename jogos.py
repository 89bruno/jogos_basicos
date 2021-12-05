from Alura.Jogos import adivinhacao, forca

print("******************************************\n")
print("************Escolha o jogo!***************  \n")
print("******************************************\n")

print("(1)Jogo da adivinhação   (2)Jogo da Forca")
jogo = int(input("Qual opção voce deseja?"))

if jogo == 1:
    print("Você escolheu Jogo da Adivinhação")
    adivinhacao.jogar()
elif jogo == 2:
    print("Você escolheu o Jogo da Forca")
    forca.jogar()