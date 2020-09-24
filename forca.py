# https://docs.python.org/3/library/stdtypes.html#immutable-sequence-types Documentação
# https: // docs.python.org/3/tutorial/datastructures.html Documentação
# https://discord.gg/QYpExzq


def jogar():
    print("*******************************")
    print("Bem Vindo ao Jogo da Forca!")
    print("###############################")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    print(letras_acertadas)
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
                print(f'Encontrei a letra {letra} na posicao {index}')
            index = index + 1
        print(letras_acertadas)

    print("Fim de jogo")


if(__name__ == "__main__"):
    jogar()
