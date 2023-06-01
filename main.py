#jogo ZombieDice- semana 8 - RC
#Laís Müller Aliski
#Big Data e Inteligência Analítica


from players import inserir,addBrain,removerBrain,scoreAtual
from Dados import randomDice,randomResult,resultRound
import time

facesround = []
faces = []
dadosRetirados = []
repetirDado = []
Dice = ['🟢 VERDE 🟢','🟢 VERDE 🟢','🟢 VERDE 🟢','🟢 VERDE 🟢','🟢 VERDE 🟢','🟢 VERDE 🟢','Vermelho','Vermelho','Vermelho','🟡 AMARELO 🟡','🟡 AMARELO 🟡','🟡 AMARELO 🟡','🟡 AMARELO 🟡']
manterJogo = True


def menu():
  print("\N{brain} \N{zombie} Bem-Vindo ao Zombie Dice!\N{zombie} \N{brain}" ) 
  print('')

def regras():
  rgs = int(input("Vocês conhecem as regras do jogo? (1 para SIM // 2 para NÃO)  "))
  print('')
  if rgs == 2:
    print("-Seu objetivo no jogo é conseguir 13 Cérebros primeiro\n"
          "-Mas cuidado! Ao levar 3 tiros em um mesmo round, você perde todos os seus pontos.\n"
          "-Caso seu dado caia em passos, poderá ser lançado novamente.\n")
  else:
    print("Ótimo! Vamos começar.")


def novoRound():
    print("")
    print("❕❕❕ Prepare-se,vamos iniciar um novo round: ❕❕❕")
    print("")
  
Players = {}
menu()
while True:
  try:
    numbPlayers = int(input("Primeiramente, qual o número de jogadores? "))
    print('')
    if numbPlayers <2:
      print("Ops, você precisa de no mínimo 2 jogadores! Tente novamente.")
      print("")
    elif numbPlayers > 5:
      print("Ops, número de jogadores excedido! O máximo é 5. ")
    else: 
      break
  except ValueError:
    print("Ops! Por favor, insira um número válido.")
  
for i in range(1,numbPlayers+1):
    inserir(Players,i)
print("")
regras()

input("Aperte ENTER para iniciar o jogo:")

while manterJogo:
  for nomePlayer in Players:
       
    scorePlayer = scoreAtual(nomePlayer,Players)
    novoRound()
    print("É sua vez, {}!".format(nomePlayer))
    print("lembre-se, sua pontuação atual é de {} 🧠".format(scorePlayer))
    print('')
    faces = []
    dadosRetirados = []
    repetirDado = []
    c = 0
    f = 0
    t = 0
    Dice = ['🟢 VERDE 🟢','🟢 VERDE 🟢','🟢 VERDE 🟢','🟢 VERDE 🟢','🟢 VERDE 🟢','🟢 VERDE 🟢','Vermelho','Vermelho','Vermelho','🟡 AMARELO 🟡','🟡 AMARELO 🟡','🟡 AMARELO 🟡','🟡 AMARELO 🟡']
       
    while True:
      try:
        input("Aperte ENTER para sortear os dados: ")
              
        resultDados = randomDice(Dice,dadosRetirados,repetirDado)
               
        if repetirDado == False:
          break
               
        repetirDado = resultDados[1]
        print('')
        input("Aperte ENTER para revelar seus resultados!")
        print('')
               
        diceFaces = randomResult(resultDados[0],faces,Dice,Players,nomePlayer,dadosRetirados,repetirDado)
      
                
        if diceFaces == 'WINNER':
          print("🎉🏆🎉 Parabéns, {}! Você Venceu! 🎉🏆🎉".format(nomePlayer))
          time.sleep(100)
          exit()
                
        if diceFaces == 'LOSER':
          break
                
        print('')
        continuarJogada = int( input ("E ai? Vai querer jogar mais dados? (1 para SIM // 2 para NÃO)  ")) 
        if continuarJogada == 2:
          addBrain(nomePlayer,Players,diceFaces)
          resultRound(diceFaces,nomePlayer,Players)
          break
        dadosRetirados = []
        
        if Dice != []:
          dadosRetirados.extend(repetirDado)         
        else:
          print("Todos os dados foram retirados da caixa!!")
          break
      except ValueError:
        print("Tente Digitar novamente")
        break
