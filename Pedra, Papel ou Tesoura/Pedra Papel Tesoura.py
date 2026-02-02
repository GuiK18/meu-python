import random

opcoesJogadas = {1 : "pedra", 2 : "papel", 3 : "tesoura"}
vitoria = {1:3, 2:1, 3:2}

listaRespostaSim = ["s","sim"]
listaRespostaNao = ["n","nao","não"]

nomeMaquina = "GuiK"

jogo = "continue"


print("##!!  BEM VINDO AO PEDRA, PAPEL OU TESOURA  !!##")

nomeJogador = input("--!! digite o nome de jogador: ")

while True:
        trocaNomeMaquina = input("\n--!! deseja trocar o nome da máquina? [s/n]: ")
        if (trocaNomeMaquina not in listaRespostaNao) and (trocaNomeMaquina not in listaRespostaSim):
            print("##!! por favor, digite uma opção válida")
            continue
        break



for escolha in listaRespostaNao:
    if trocaNomeMaquina.strip().lower() == escolha:
        print(f"\n--!! {nomeJogador} jogará contra {nomeMaquina} !!--")
        continue
for escolha in listaRespostaSim:
    if trocaNomeMaquina.strip().lower() == escolha:
        nomeMaquina = input("--!! digite o novo nome da máquina: ")
        print(f"\n##!! {nomeJogador} jogará contra {nomeMaquina} !!--")
        continue


while jogo != "end":
    escolhaMaquina = random.randint(1,3)
    
    while True:
        try:
            print("\n&&!! 1. Pedra\n&&!! 2. Papel\n&&!! 3.Tesoura")
            escolhaJogador = int(input("\n##!! digite a jogada escolhida: "))

            if escolhaJogador not in opcoesJogadas:
                print("##!! por favor, escolha uma opção válida ")
                continue
            break
        except ValueError:
            print("##!! ERRO: você digitou um valor de tipo diferente")


    print(f"\n@@!!{nomeJogador} jogou {opcoesJogadas[escolhaJogador]}")
    print(f"@@!!{nomeMaquina} jogou {opcoesJogadas[escolhaMaquina]}")

    if escolhaJogador == escolhaMaquina:
        print("\n$$!! empate")
    elif vitoria[escolhaJogador] == escolhaMaquina:
        print(f"\n$$!! {nomeJogador} venceu")
    else:
        print(f"\n$$!! {nomeMaquina} venceu")
    

    while True:
        continuar = input("\n##!! deseja continuar jogando? [s/n]: ")
        if (continuar not in listaRespostaNao) and (continuar not in listaRespostaSim):
            print("##!! por favor, digite uma opção válida")
            continue
        break
    
    for escolha in listaRespostaSim:
        if continuar.strip().lower() == escolha:
            jogo = jogo
            print("\n##!! ----##----##----##----##---- !!##")
            continue

    for escolha in listaRespostaNao:
        if continuar.strip().lower() == escolha:
            print("##!!  OBRIGADO POR JOGAR !!##")
            jogo = "end"
            continue