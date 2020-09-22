print("*******************************")
print("Bem Vindo ao Jogo de Adivinhação!")
print("###############################")

numero_secreto = 42
total_de_tentativas = 3
#rodada = 1
# for rodada in range(1,10,2):

for rodada in range(1, total_de_tentativas + 1):
    #print(f'tentativa {rodada} {total_de_tentativas}')
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite seu numero entre 1 e 100: ")
    print(f"voce digitou {chute}")
    chute = int(chute)

    if (chute < 1 or chute > 100):
        print("Voce deve digitar um numero entre 1 é 100!:")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você Acertou!")
        break
    else:
        if (maior):
            print("Voce errou! O seu chute foi maior do que o numero secreto")
        elif (menor):
            print("Voce errou! O seu chute foi menor que o numero secreto")
    print("Fim de Jogo!")
    #rodada = rodada + 1
