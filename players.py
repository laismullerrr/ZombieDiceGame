def dadosPlayer(i):
    nome = input("Olá Player {}! Digite seu nome: ".format(i))
    cerebros = 0
    return nome,cerebros
    
def inserir(Players,i):
    player = dadosPlayer(i)
    Players[player[0]] = player[1]
    return True

def addBrain(nomePlayer,Players,diceFaces):
    pontos = Players[nomePlayer]
    if pontos > 0:        
        c = pontos
    else:
        c = 0
    
    for i in diceFaces:
        if i == "- \N{brain} (você comeu um cérebro!)":
            c = c + 1
    Players[nomePlayer] = c

    return True
    
def removerBrain(nomePlayer,Players):
    c = 0
    Players[nomePlayer] = c
    return True
    
def scoreAtual(nomePlayer,Players):
    
    score = Players[nomePlayer]
    return score
    