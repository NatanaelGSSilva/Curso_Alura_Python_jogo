# https://docs.python.org/3/library/stdtypes.html#immutable-sequence-types Documentação
# https: // docs.python.org/3/tutorial/datastructures.html Documentação
# https://discord.gg/QYpExzq
# dias = ["S","T","Q","Q","S","S","D"]
# dias.append("D2") Acrecestar D2
# dias.pop("D2")
# dias = ()"S","T","Q","Q","S","S","D") # Lista Fixa
#palavras = []
# palavras.append("BANANA")
# palavras.append("ABACAXI")
#nova = tuple(palavras)
# nova listar
#outra = list(nova)
# outra
# mv palavras.txt ../..

import random


def jogar():
    print("*******************************")
    print("Bem Vindo ao Jogo da Forca!")
    print("###############################")

    arquivo = open("palavras.txt", "r")

    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    print(palavras)
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()
        index = 0

        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                    print(f'Encontrei a letra {letra} na posicao {index}')
                index = index + 1
        else:
            erros += 1
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Voce Ganhou!")
    else:
        print("Você Perdeu!")
    print("Fim de jogo")


if(__name__ == "__main__"):
    jogar()
