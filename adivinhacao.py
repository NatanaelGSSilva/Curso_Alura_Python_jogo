print("*******************************")
print("Bem Vindo ao Jogo de Adivinhação!")
print("###############################")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1
while (rodada <= total_de_tentativas):
    #print(f'tentativa {rodada} {total_de_tentativas}')
    print("Tentativa {} de {}".format(rodada,total_de_tentativas))
    chute = input("Digite seu numero: ")
    print(f"voce digitou {chute}")
    chute = int(chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você Acertou!")
    else:
        if (maior):
            print("Voce errou! O seu chute foi maior do que o numero secreto")
        elif (menor):
            print("Voce errou! O seu chute foi menor que o numero secreto")
    print("Fim de Jogo!")
    rodada = rodada + 1
