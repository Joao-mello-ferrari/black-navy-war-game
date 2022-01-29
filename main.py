try: from errorHelpers import importErrorMessage
except: print("Coloque o arquivo errorHelpers.py no diretório do main.py!")


try:
    from graphics import *

    from objectHelpers import *
    from commandHelpers import *

except: print(importErrorMessage())


def main(firstTime, win):
    if firstTime:
        win=GraphWin("ChromeDino", 1300, 600, autoflush=False)
        drawFooter(win, "#222222")
    
    blackShips, redShips, introObjects = drawIntro(win, firstTime)
    
    # Barra de vida da base dos jogadores
    blackXp = 10000
    redXp = 10000
    blackFrame = None
    redFrame = None
    blackBar = None
    redBar = None
    
    # Dano for frame de cada time
    blackDmg = 0
    redDmg = 0
    
    # Recurso de cada time
    resource = 1000
    redResource = 1000

    # Multiplicadores de recurso e armazenamento
    resourceMult = 1
    storageMult = 1

    # Contador de navios vermelhos
    redShipCounter = 0
    redShipIndex = 0

    # Dificuldade do jogo
    dificulty = 0.6
    lastDificultyButtonIndex = 1

    # Desenhar itens iniciais para o funcionamento do jogo
    dificultyButtons = renderDificultyButtons(win)
    buttons, buttonsOverlay, buttonsText, shipIcons = renderAddShipsButtons(win)
    resourceBar, resourceText, introObjects = renderResourceBoard(win, introObjects)
    cmdButtons, cmdButtonsOverlay, cmdButtonsText, cmdButtonsIcons = renderCommandButtons(win)
 
    while True:
      area = win.checkMouse()

      # Ver se algum time perdeu
      if blackXp <= 0 or redXp <= 0: 
        blackFrame, redFrame, blackBar, redBar = renderBasesHp(win, blackXp, redXp, blackFrame, redFrame, blackBar, redBar)
        break        
      
      # Atualizar recursos
      resource, cmdButtonsOverlay, cmdButtonsText, resourceMult, storageMult = checkResourceUpdate(area, resource, cmdButtons, cmdButtonsOverlay, cmdButtonsText, resourceMult, storageMult)    
      resource, resourceBar, resourceText = updateResource(win, resource, resourceBar, resourceText, resourceMult, storageMult)
      redResource = updateRedResource(redResource, storageMult, resourceMult, dificulty)
      
      # Ver disponibilidade dos botões
      shipIcons = checkShipAvailability(win, shipIcons, resource)
      cmdButtonsIcons = checkCmdButtonsAvailability(win, cmdButtonsIcons, cmdButtonsOverlay)
      
      # Mover navios, contabilizar dano e renderizar as barras de vida atualizadas
      blackShips, redShips, blackDmg, redDmg, firstBlackShipI, firstRedShipI = moveShipsAndReduceDamage(win, blackShips, redShips)   
      blackFrame, redFrame, blackBar, redBar = renderBasesHp(win, blackXp, redXp, blackFrame, redFrame, blackBar, redBar)
      blackShips, redShips = renderShipsHp(win, blackShips, redShips, blackDmg, redDmg, firstBlackShipI, firstRedShipI)

      # Ver se as bases sofream dano
      blackXp, redXp = checkBaseDamage(blackShips, redShips, blackXp, redXp, blackDmg, redDmg, firstBlackShipI, firstRedShipI)
      
      # Ver se novos navios devem ser renderizados
      buttonsOverlay, buttonsText, resource = shouldRenderNewShips(area, buttons, buttonsOverlay, buttonsText, resource)
      blackShips = renderNewShip(win, blackShips, buttonsOverlay, buttonsText)
      redShips, redResource, redShipCounter, redShipIndex = renderRedShips(win, redShips, redResource, redShipCounter, redShipIndex)
      
      # Deletar navios que foram destruídos
      blackShips, redShips = deleteShips(blackShips, redShips, firstBlackShipI, firstRedShipI)
      
      # Renderizar os overlays dos botões
      buttonsOverlay, buttonsText = renderButtonsOverlay(win, buttonsOverlay, buttonsText, buttons)
      cmdButtonsOverlay, cmdButtonsText = renderCmdButtonsOverlay(win, cmdButtonsOverlay, cmdButtons, cmdButtonsText)

      # Alterar a dificuldade do jogo
      if area: 
        dificultyButtons, dificulty, lastDificultyButtonIndex = changeDificulty(win, area, dificulty, dificultyButtons, lastDificultyButtonIndex)

      update(250)

    # Juntar os objetos da tela
    ships = blackShips + redShips 
    shipButtons = buttons + buttonsOverlay + buttonsText + shipIcons  
    cmdButtons = cmdButtons + cmdButtonsOverlay + cmdButtonsText + cmdButtonsIcons
    resourceItems = [resourceBar, resourceText]
    hpItems = [blackFrame, redFrame, blackBar, redBar]

    # Obter o comando do usuário sobre jogar novamente
    shouldClose = renderFinalCenario(win, blackXp, introObjects, 
      ships, shipButtons, cmdButtons, resourceItems, hpItems, dificultyButtons)

    if shouldClose:
        win.close()
        return win, True
    
    return win, False

if __name__=="__main__":
    firstTime = True
    win = None
    
    while True:
        try: 
          win, shouldClose = main(firstTime, win)
          
          firstTime = False
          if shouldClose:
              print("Programa encerrado")
              break
        
        except Exception as err: # Se houver exceções
          print(err)
          print("ERRO AO EXECUTAR O PROGRAMA! / PROGRAMA FINALIZADO!")
          break
