import random

letras = 'ABCDEFGHIJ' # coordenadas laterais


campo1 = [[' '] * 11 for _ in range(11)] # campo do jogador 1
campo2 = [[' '] * 11 for _ in range(11)] # campo do jogador 2

partida = 1 # conta as partidas
rodada = 0 # conta as rodadas
modoJogo = '' # guarda o modo de jogo; recebe ' ' para não quebrar o código

jogador1 = '0' # nome inicial para não quebrar o código
jogador2 = 'Máquina' # nome inicial para não quebrar o código

listaAtaques1 = []  # Ataques feitos pelo jogador 1 no campo 2
listaAtaques2 = []  # Ataques feitos pelo jogador 2 no campo 1

barcos = [('encouraçado', 5), ('porta-aviões', 4), ('contratorbedeiros', 3), ('contratorbedeiros', 3), ('submarino', 2), ('submarino', 2)] # dados dos barcos



def inicioJogo(): # função responsável por rodar o início do jogo
    global modoJogo # impede que o código faça novas variáveis com base na 'modoJogo', garante que a 'modoJogo' permaneça único no decorrer do programa
    print('--- Bem-vindo ao Batalha Naval! ---')
    print('Por favor, escolha seu modo de jogo:')
    print('1. Jogador vs Jogador')
    print('2. Jogador vs Máquina')

    modoJogo = input('Escolha o modo (1 ou 2): ') # transforma o valor em string para evitar problemas no código, como colocar um valor de tipo diferente
    while modoJogo != '1' and modoJogo != '2': # garante que o modo de jogo seja 1 ou 2
        modoJogo = input('Por favor, insira um modo válido (1 ou 2): ')


def nomes(): # função responsável por nomear os jogadores (tanto o jogador 1 quanto o jogador 2)
    global jogador1, jogador2
    jogador1 = input('Digite o seu apelido, jogador 1: ')
    if modoJogo == '1':
        jogador2 = input('Digite o seu apelido, jogador 2: ') # disponível somente quando modoJogo == '1', se não jogador2 continuará com o nome definido na variável


def tabuleiroVazio(campo): # função responsável por 'polir' o tabuleiro (chamdos 'campo' inicialmente)
    campo[0][0] = ' '
    for i in range(1, 11):
        campo[0][i] = i
        campo[i][0] = letras[i-1]
    for i in range(1, 11):
        for j in range(1, 11):
            campo[i][j] = ' '


def possivelPosicionarBarco(campo, x, y, tamanho, orientacao): # função responsável por determinar se é ou não possível posicionar um barco em um determinado local
    if orientacao == 'H':
        if y + tamanho - 1 > 10:
            return False
        for coluna in range(y, y + tamanho):
            if campo[x][coluna] != ' ':
                return False
    else:
        if x + tamanho - 1 > 10:
            return False
        for linha in range(x, x + tamanho):
            if campo[linha][y] != ' ':
                return False
    return True


def posicionarBarco(campo, x, y, tamanho, orientacao): # função responsável por determinar a posição do barco
    if orientacao == 'H':
        for coluna in range(y, y + tamanho):
            campo[x][coluna] = 'N'
    else:
        for linha in range(x, x + tamanho):
            campo[linha][y] = 'N'


def posicionarBarcosAutomaticamente(campo): # auto
    for nome, tamanho in barcos:
        colocado = False
        while not colocado:
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            orientacao = random.choice(['H', 'V'])
            if possivelPosicionarBarco(campo, x, y, tamanho, orientacao):
                posicionarBarco(campo, x, y, tamanho, orientacao)
                colocado = True


def mostrarTabuleiro(campo, ocultarBarcos=False): # função responsável por mostrar o tabuleiro ao(s) jogador(es)
    print('  ' + ' '.join(str(i) for i in range(1, 11)))
    for i in range(1, 11):
        linha = letras[i-1] + ' '
        for j in range(1, 11):
            if ocultarBarcos:
                # Se for barco, mostra vazio para esconder
                if campo[i][j] == 'N':
                    linha += ' ' + ' '
                else:
                    linha += campo[i][j] + ' '
            else:
                linha += campo[i][j] + ' '
        print(linha)
    print()


def converterCoordenada(entrada): # função responsável por converter as letras das coordenadas em números
    entrada = entrada.strip().upper()
    if len(entrada) < 2 or len(entrada) > 3:
        return None
    letra = entrada[0]
    if letra not in letras:
        return None
    try:
        numero = int(entrada[1:])
    except:
        return None
    if numero < 1 or numero > 10:
        return None
    linha = letras.index(letra) + 1
    coluna = numero
    return (linha, coluna)


def realizarAtaque(jogadorNome, campoInimigo, listaAtaques): # função responsável pelos ataques e a verificação dos mesmos
    while True:
        if jogadorNome == 'Máquina':
            ataqueLinha = random.randint(1, 10)
            ataqueColuna = random.randint(1, 10)
            if (ataqueLinha, ataqueColuna) not in listaAtaques:
                listaAtaques.append((ataqueLinha, ataqueColuna))
                letra = letras[ataqueLinha - 1]
                print(f'Máquina ataca posição: {letra}{ataqueColuna}')
                break
        else:
            entrada = input(f'{jogadorNome}, selecione a posição para o ataque (exemplo: A5): ')
            coords = converterCoordenada(entrada)
            if coords is None:
                print('Coordenada inválida! Use letra (A-J) e número (1-10), ex: B7')
                continue
            ataqueLinha, ataqueColuna = coords
            if (ataqueLinha, ataqueColuna) not in listaAtaques:
                listaAtaques.append((ataqueLinha, ataqueColuna))
                break
            else:
                print('Você já atacou essa posição. Escolha outra.')

    if campoInimigo[ataqueLinha][ataqueColuna] == 'N':
        print(f'{jogadorNome} acertou um barco!')
        campoInimigo[ataqueLinha][ataqueColuna] = 'X'
    else:
        print(f'{jogadorNome} não acertou nada.')
        campoInimigo[ataqueLinha][ataqueColuna] = '~'


def verificarVitoria(campo): # função responsável por verificar a se ocorreu uma vitória
    for i in range(1, 11):
        for j in range(1, 11):
            if campo[i][j] == 'N':
                return False
    return True


def executarRodada(): # função responsável pela rodada, chamando as funções anteriores que garantem o funcionamento do jogo
    global partida, rodada # impede que o código faça novas variáveis com base na 'partida' e 'rodada', garante que a 'partida' e 'rodada' permaneçam únicos no decorrer do programa
    print(f'\nRodada {rodada + 1} - Partida {partida}')
    if modoJogo == '1':  # Jogador vs Jogador
        if partida % 2 != 0:
            print(f'\nTabuleiro de {jogador1}:')
            mostrarTabuleiro(campo1, ocultarBarcos=True)  # oculto, sem revelar barcos do próprio
            print(f'\nTabuleiro de {jogador2}:')
            mostrarTabuleiro(campo2, ocultarBarcos=True)
            print(f'Sua vez, {jogador1}!')
            realizarAtaque(jogador1, campo2, listaAtaques1)
        else:
            print(f'\nTabuleiro de {jogador2}:')
            mostrarTabuleiro(campo2, ocultarBarcos=True)
            print(f'\nTabuleiro de {jogador1}:')
            mostrarTabuleiro(campo1, ocultarBarcos=True)
            print(f'Sua vez, {jogador2}!')
            realizarAtaque(jogador2, campo1, listaAtaques2)
    else:  # Jogador vs Máquina
        if partida % 2 != 0:
            print(f'\nSeu tabuleiro ({jogador1}):')
            mostrarTabuleiro(campo1, ocultarBarcos=False)
            print(f'\nTabuleiro da Máquina:')
            mostrarTabuleiro(campo2,ocultarBarcos=True)
            realizarAtaque(jogador1, campo2, listaAtaques1)
        else:
            realizarAtaque('Máquina', campo1, listaAtaques2)
            print(f'\nSeu tabuleiro após ataque da Máquina:')
            mostrarTabuleiro(campo1, ocultarBarcos=False)

    partida += 1
    if partida % 2 == 0:
        rodada += 1
        print(f'Fim da rodada {rodada}.')


def jogo(): # função que carrega todo o jogo
    tabuleiroVazio(campo1)
    tabuleiroVazio(campo2)

    posicionarBarcosAutomaticamente(campo1)
    posicionarBarcosAutomaticamente(campo2)

    while True:
        executarRodada()
        if modoJogo == '1':
            if verificarVitoria(campo2):
                print(f'\n{jogador1} venceu o jogo! Parabéns!')
                break
            if verificarVitoria(campo1):
                print(f'\n{jogador2} venceu o jogo! Parabéns!')
                break
        else:
            if verificarVitoria(campo2):
                print(f'\n{jogador1} venceu o jogo! Parabéns!')
                break
            if verificarVitoria(campo1):
                print(f'\nMáquina venceu o jogo! Boa sorte na próxima!')
                break


# --- Execução ---
inicioJogo()
nomes()
jogo()