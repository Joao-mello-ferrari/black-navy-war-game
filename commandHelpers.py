from graphics import *
from random import randrange as r


# Atualizar o recurso do time preto
def updateResource(win, resource, resourceBar, resourceText, resourceMult, storageMult):
  if resource > 1000*storageMult:
    resource = 1000*storageMult
    return resource, resourceBar, resourceText
  
  resource += 0.5*resourceMult
  resourcePercentage = (resource/(1000*storageMult)) * (839-511) + 511
  
  resourceBar.undraw()
  resourceText.undraw()

  resourceBar = Rectangle(Point(511,471), Point(resourcePercentage, 484))
  resourceBar.setWidth(0)
  resourceBar.setFill("#666666")
  resourceBar.draw(win)
  
  resourceText = Text(Point(675,477), "{:.0f}%".format((resource/1000)*100))
  resourceText.setSize(8)
  resourceText.setStyle("bold") 
  resourceText.setFace("helvetica")
  resourceText.setTextColor("#FFFFFF")
  resourceText.draw(win)

  return resource, resourceBar, resourceText


# Autualizar o recurso do time vermelho
def updateRedResource(redResource, storageMult, resourceMult, dificulty):
  if redResource > 1000*storageMult:
    redResource = 1000*storageMult
    return redResource

  redResource += 0.5*resourceMult*dificulty
  return redResource


# Checar atualização de recurso do time preto
def checkResourceUpdate(area, resource, cmdButtons, cmdButtonsOverlay, cmdButtonsText, resourceMult, storageMult):
  if not area: return resource, cmdButtonsOverlay, cmdButtonsText, resourceMult, storageMult
  
  for i in range(len(cmdButtons)):
    thisButton = cmdButtons[i]

    x = area.getX()
    y = area.getY()
    coords = thisButton["coords"]
    
    if x >= coords[0] and x <= coords[1]:
      if y >= coords[2] and y <= coords[3]:
        if cmdButtonsOverlay[i]["current%"] > 0.01 or cmdButtonsText[i]["currentNum"] == 5:
          return resource, cmdButtonsOverlay, cmdButtonsText, resourceMult, storageMult
                      
        if cmdButtonsText[i]["currentNum"] < 5:
          cmdButtonsOverlay[i]["current%"] = 100
          cmdButtonsText[i]["currentNum"] += 1
          if i == 0: storageMult += 0.75
          elif i == 1: resourceMult += 0.25
            
  return resource, cmdButtonsOverlay, cmdButtonsText, resourceMult, storageMult

# Checar se os botões de navios do time preto estão disponíveis, conforme o recurso
def checkShipAvailability(win, shipIcons, resource):
  for i in shipIcons:
    if resource - i["price"] < 0 and i["currentColor"] == 'dark':
      i["currentColor"] = 'light'
      i["object"].setFill("#999999")
      i["object"].setOutline("#999999")
    
    if resource - i["price"] > 0 and i["currentColor"] == 'light':
      i["currentColor"] = 'dark'
      i["object"].setFill("#555555")
      i["object"].setOutline("#555555")
  
  return shipIcons


# Checar se os botões de comando do time preto estão disponíveis
def checkCmdButtonsAvailability(win, cmdButtonsIcons, cmdButtonsOverlay):
  if cmdButtonsOverlay[0]["object"] is None: return cmdButtonsIcons
  
  for i in range(len(cmdButtonsIcons)):
    thisIcon = cmdButtonsIcons[i]
    
    if False and thisIcon["currentColor"] != 'green':
      thisIcon["currentColor"] = 'green'
      thisIcon["object"].setTextColor("#22CC22")
        
    elif cmdButtonsOverlay[i]["current%"] < 0.01 and thisIcon["currentColor"] == 'light':
      thisIcon["currentColor"] = 'dark'
      thisIcon["object"].setTextColor("#333333")
        
    elif cmdButtonsOverlay[i]["current%"] >= 0.01 and thisIcon["currentColor"] == 'dark':
      thisIcon["currentColor"] = 'light'
      thisIcon["object"].setTextColor("#777777")
          
  return cmdButtonsIcons


# Mover os navios
def moveShipsAndReduceDamage(win, blackShips, redShips):
  blackDmg = 0
  redDmg = 0
  firstBlackShipI = 0
  firstRedShipI = 0
  
  blackTroopFrontPoint = 200
  blackBuff = 10
  for j in range(len(blackShips)):
    if blackShips[j]["shipFrontPos"] > blackTroopFrontPoint:
      blackTroopFrontPoint = blackShips[j]["shipFrontPos"]
      blackBuff = 0
      firstBlackShipI = j
  
  redTroopFrontPoint = 1100
  redBuff = 10
  for j in range(len(redShips)):
    if redShips[j]["shipFrontPos"] < redTroopFrontPoint:
      redTroopFrontPoint = redShips[j]["shipFrontPos"]
      firstRedShipI = j
      redBuff = 0
    
  for i in range(len(blackShips)):
    thisShip = blackShips[i]
    thisShipFrontPoint = thisShip["object"].getPoints()[-2].getX()

    thisShip["bulletObject"] = thisShip["bulletObject"]
    if abs(thisShipFrontPoint - redTroopFrontPoint) < 70 - redBuff:
      if thisShip["bulletObject"].getText() != ". . . . .":
        thisShip["bulletObject"] = Text(Point(thisShipFrontPoint+32+i%4, 407), ". . . . .")
        thisShip["bulletObject"].setSize(16)
        thisShip["bulletObject"].draw(win)
      blackDmg += thisShip["initialHp"]/150
      continue

    elif thisShip["bulletObject"].getText() == ". . . . .": thisShip["bulletObject"].setText("")

    speedCoef = 100/thisShip["initialHp"]
    
    thisShip["object"].move(1*speedCoef, 0)
    thisShip["lineObject"].move(1*speedCoef, 0)
    
    thisShip["shipFrontPos"] += 1*speedCoef

  for i in range(len(redShips)):
    thisShip = redShips[i]
    thisShipFrontPoint = thisShip["object"].getPoints()[-2].getX()
    
    if abs(thisShipFrontPoint - blackTroopFrontPoint) < 70 - blackBuff:
        if thisShip["bulletObject"].getText() != ". . . . .":
          thisShip["bulletObject"] = Text(Point(thisShipFrontPoint-32-i%4, 407), ". . . . .")
          thisShip["bulletObject"].setSize(16)
          thisShip["bulletObject"].setTextColor("#cc1111")
          thisShip["bulletObject"].draw(win)
        redDmg += thisShip["initialHp"]/150
        continue

    elif thisShip["bulletObject"].getText() == ". . . . .": thisShip["bulletObject"].setText("")

    speedCoef = 100/thisShip["initialHp"]
    
    thisShip["object"].move(-1*speedCoef, 0)
    thisShip["lineObject"].move(-1*speedCoef, 0)
    
    thisShip["shipFrontPos"] += -1*speedCoef

  return blackShips, redShips, blackDmg, redDmg, firstBlackShipI, firstRedShipI
 

# Checar por dano nas bases
def checkBaseDamage(blackShips, redShips, blackXp, redXp, blackDmg, redDmg, firstBlackShipI, firstRedShipI):
  if len(blackShips):
    if blackShips[firstBlackShipI]["object"].getPoints()[-2].getX() < 200: blackXp -= redDmg
  else: blackXp -= redDmg
  
  if len(redShips):
    if redShips[firstRedShipI]["object"].getPoints()[-2].getX() > 1100: redXp -= blackDmg
  else: redXp -= blackDmg
  
  return blackXp, redXp


# Checar se deve haver renderizações de novos navios pretos
def shouldRenderNewShips(area, buttons, buttonsOverlay, buttonsText, resource):
  if not area: return buttonsOverlay, buttonsText, resource
  
  for i in range(len(buttons)):
    thisButton = buttons[i]

    x = area.getX()
    y = area.getY()
    coords = thisButton["coords"]
    
    if x >= coords[0] and x <= coords[1]:
      if y >= coords[2] and y <= coords[3]:
        if resource - thisButton["price"] < 0: return buttonsOverlay, buttonsText, resource
            
        buttonsOverlay[i]["current%"] = 100
        
        buttonsText[i]["currentNum"] += 1
        resource -= thisButton["price"]
  
  return buttonsOverlay, buttonsText, resource


# Alterar a dificuldade do jogo, conforme os botões forem clicados
def changeDificulty(win, clickArea, dificulty, buttons, lastButtonIndex):
  def checkIfDifButtonsWereClicked(area, index):
    if index == 0: coords = [[895,940],[500,530]]
    elif index == 1: coords = [[952.5,997.5],[500,530]]
    elif index == 2: coords = [[1010,1055],[500,530]]
    else: coords = [[0,0],[0,0]]
    
    x = area.getX()
    y = area.getY()
        
    if x >= coords[0][0] and x <= coords[0][1]:
      if y >= coords[1][0] and y <= coords[1][1]:
        return True
    return False
  
  for i in range(3):
    if checkIfDifButtonsWereClicked(clickArea, i) and i != lastButtonIndex:
      buttons[i].setFill("#444444")
      buttons[lastButtonIndex].setFill("#888888")
      dificulty = [0.4,0.6,0.8][i]
      
      return buttons, dificulty, i
  
  return buttons, dificulty, lastButtonIndex
    