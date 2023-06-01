import random
from players import addBrain,removerBrain
import time
def randomDice(Dice,dadosRetirados,repetirDado):
    
    print('')
    print("Dados retirados: ")
    for i in range(3):
        if Dice != []:
            if len(dadosRetirados) <= 2:
                diceResult = random.choice(Dice)
            else: 
                print('')
                print("Dados reutilizados:")
                for dado in repetirDado:
                  print(dado)
                  
                repetirDado = []
                return dadosRetirados,repetirDado
            if diceResult == '🟢 VERDE 🟢':
                Dice.remove('🟢 VERDE 🟢')
                dadosRetirados.append(diceResult)
                print('🟢 VERDE 🟢')
            elif diceResult == "Vermelho":
                Dice.remove('Vermelho')
                dadosRetirados.append(diceResult)
                print( '🔴 VERMELHO 🔴')
            elif diceResult == '🟡 AMARELO 🟡':
                Dice.remove('🟡 AMARELO 🟡')
                dadosRetirados.append(diceResult)
                print('🟡 AMARELO 🟡')
        else:
            print("Os dados acabaram")
            repetirDado = False
            return dadosRetirados,repetirDado
        
    repetirDado = []
    return dadosRetirados,repetirDado
    

def randomResult(resultDados,faces,Dice,Players,nomePlayer,dadosRetirados,repetirDado):
   
    c = Players[nomePlayer]
    f = 0
    t = 0
    Gdice = ['- \N{brain} (você comeu um cérebro!)',"- \N{brain} (você comeu um cérebro!)","- \N{brain} (você comeu um cérebro!)", "- 💥 (você levou um tiro)","- 👣 (uma vítima escapou)","- 👣 (uma vítima escapou)"]
    Ydice = ["- \N{brain} (você comeu um cérebro!)","- \N{brain} (você comeu um cérebro!)","- \N{brain} (você comeu um cérebro!)","- \N{brain} (você comeu um cérebro!)","- 👣 (uma vítima escapou)","- 👣 (uma vítima escapou)"]
    Rdice = ["- \N{brain} (você comeu um cérebro!)","- 💥 (você levou um tiro)","- 💥 (você levou um tiro)","- 💥 (você levou um tiro)","- 👣 (uma vítima escapou)","- 👣 (uma vítima escapou)"]
    for i in resultDados:
        if i == '🟢 VERDE 🟢':
            g = random.choice(Gdice)
            faces.append(g)
            if g == '- 👣 (uma vítima escapou)':
                repetirDado.append('🟢 VERDE 🟢')
            print(g)
        elif i == '🟡 AMARELO 🟡':
            y = random.choice(Ydice)
            faces.append(y)
            if y == '- 👣 (uma vítima escapou)':
                repetirDado.append('🟡 AMARELO 🟡')
            print(y)
        elif i == 'Vermelho':
            r = random.choice(Rdice)
            faces.append(r)
            if r == '- 👣 (uma vítima escapou)':
                repetirDado.append('Vermelho')
            print(r)
        time.sleep(1)
    
    for i in faces:
        if i == '- \N{brain} (você comeu um cérebro!)':
            c = c + 1
           
            if c >= 13:
                c = 'WINNER'
                return c
        elif i ==  '- 👣 (uma vítima escapou)':
            f = f + 1
            
        elif i == '- 💥 (você levou um tiro)':
            t = t + 1
            
            if t >= 3:
                removerBrain(nomePlayer,Players)
                print('')
                print("⚠️⚠️⚠️ Ah não! Você foi baleado 3 vezes e perdeu todos os pontos... ⚠️⚠️⚠️")
                print('')
                t = 'LOSER'
                return t
           
    return faces
    

def resultRound(diceFaces,nomePlayer,Players):
    c = 0
    f = 0
    t = 0
    geral = Players[nomePlayer]
    for i in diceFaces:
        if i == '- \N{brain} (você comeu um cérebro!)':
            c = c + 1 
        elif i ==  '- 👣 (uma vítima escapou)':
            f = f + 1 
        elif i == '- 💥 (você levou um tiro)':
            t = t + 1
    print("O seu resultado nessa partida foi de: \n",c," Cerebros\n",f," Fugitivos\n",t," Tiros\n""Pontuação Geral :", geral, "Cérebro(s)")
    