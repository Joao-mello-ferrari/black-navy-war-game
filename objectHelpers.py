from time import sleep
from graphics import *
from datetime import datetime as d
from random import randint

shipPrices = [200,400,700]
shipHps = [100, 200, 400]

# Desenhar rodapé
def drawFooter(win, color):
  t = Text(Point(1060,588), "@ Todos os direitos reservados. Atualizado em 29/11/2021, por João Mello.")
  t.setOutline(color)
  t.setFace("helvetica")
  t.setSize(10)
  t.setStyle("bold")
  t.draw(win)


def getNewShip(index, color=None):
  ship = None
  hp = None
  size = None
  
  if color == 'black':
    if index == 0:
      ship = Polygon(Point(0,420),Point(0,413),Point(15,413),Point(15,403),Point(20,403),Point(20,398),
                      Point(30,398),Point(30,413),Point(60,413),Point(60,410),Point(65,410),Point(65,420))
      ship.setFill("#555555")
      ship.setOutline("#555555")
      ship.setWidth(0)
      hp = 100
      pos = 65
      size = 65
            
    elif index == 1:
      ship = Polygon(Point(0,420),Point(0,410),Point(5,410),Point(5,390),Point(20,390),Point(20,400),
                      Point(55,400),Point(55,405),Point(60,405),Point(60,410),Point(65,410),Point(65,420))
      ship.setFill("#555555")
      ship.setOutline("#555555")
      ship.setWidth(0)
      pos = 65
      hp = 200
      size = 65
            
    else:
      ship = Polygon(Point(10,420),Point(0,413),Point(55,413),Point(55,407),Point(65,407),Point(65,409),
                      Point(75,409),Point(75,411),Point(65,411),Point(65,413),Point(90,413),Point(80,420))
      ship.setFill("#555555")
      ship.setOutline("#555555")
      ship.setWidth(0)
      hp = 400
      pos = 90
      size = 90
            
  else:
    if index == 0:
      ship = Polygon(Point(1300,420),Point(1300,413),Point(1285,413),Point(1285,403),Point(1280,403),Point(1280,398),
                  Point(1270,398),Point(1270,413),Point(1240,413),Point(1240,410),Point(1235,410),Point(1235,420))
      ship.setFill("#cc1111")
      ship.setOutline("#cc1111")
      ship.setWidth(0)
      hp = 100
      pos = 1235
      size = 65
        
    elif index == 1:
      ship = Polygon(Point(1300,420),Point(1300,410),Point(1295,410),Point(1295,390),Point(1280,390),Point(1280,400),
                  Point(1245,400),Point(1245,405),Point(1240,405),Point(1240,410),Point(1235,410),Point(1235,420))
      ship.setFill("#cc1111")
      ship.setOutline("#cc1111")
      ship.setWidth(0)
      hp = 200
      pos = 1235
      size = 65
    
    else:
      ship = Polygon(Point(1290,420),Point(1300,413),Point(1245,413),Point(1245,407),Point(1235,407),Point(1235,409),
                      Point(1225,409),Point(1225,411),Point(1235,411),Point(1235,413),Point(1210,413),Point(1220,420))
      ship.setFill("#cc1111")
      ship.setOutline("#cc1111")
      ship.setWidth(0)
      hp = 400
      pos = 1210
      size = 90
  
  return { "object":ship, "lineObject":None, "currentHp":hp, 
          "initialHp":hp, "shipFrontPos":pos, "shipSize":size, 
          "bulletObject": Text(Point(0,0),"")}
    


# Desenhar a linha de vida dos navios
def drawShipHp(win, ship, shipColor, lineStartPos):
  totalSize = ship["shipSize"]
  hpRatio = ship["currentHp"]/ship["initialHp"]

  life = hpRatio*totalSize
  
  if shipColor == 'black': 
    line = Line(Point(lineStartPos, 385),Point(lineStartPos+life, 385))
    lineColor = '#555555'
  else: 
    line = Line(Point(lineStartPos-life, 385), Point(lineStartPos, 385))
    lineColor = '#cc1111'

  line.setOutline(lineColor)
  line.setWidth(2)
  line.draw(win)
  
  ship["lineObject"] = line
  
  return ship


# Desenhar a abertura do jogo, com alguns objetos iniciais
def drawIntro(win, animation=True):
  line = Line(Point(0,420),Point(1300,420))
  line.setWidth(3)
  line.setFill("#444444")
  line.draw(win)
  
  base = Polygon(Point(0,80),Point(50,80),Point(200,400),Point(200,550),Point(0,550))    
  base.setFill("#777777")
  base.setOutline("#777777")
  base.setWidth(0)
  base.draw(win)
  
  base1 = Polygon(Point(1300,80),Point(1250,80),Point(1100,400),Point(1100,550),Point(1300,550))    
  base1.setFill("#cc3333")
  base1.setOutline("#cc3333")
  base1.setWidth(0)
  base1.draw(win)
  
  blackShip = getNewShip(0, 'black')
  blackShip = drawShipHp(win, blackShip, 'black', 0)
  blackShip["object"].draw(win)
  
  redShip = getNewShip(0, 'red')
  redShip = drawShipHp(win, redShip, 'red', 1300)
  redShip["object"].draw(win)
  
  blackShips = [blackShip]
  redShips = [redShip]
  
  if animation: i0 = 0
  else: i0 = 99
    
  # Animação da mensagem inicial
  logo = None
  for i in range(i0,100):
    if logo: logo.undraw()
    x1 = 650 - 2.2*i
    x2 = 650 + 2.2*i
    y1 = 200 - 0.75*i
    y2 = 200 + 0.75*i
    logo = Rectangle(Point(x1,y1), Point(x2,y2))
    logo.setFill("#999999")
    logo.setOutline("#666666")
    logo.setWidth(2)
    logo.draw(win)
    update(100)
    
  text = Text(Point(650,190), "BLACK NAVY WAR")
  text.setFace("helvetica")
  text.setSize(20)
  text.setStyle("bold")
  text.draw(win)

  text1 = Text(Point(650,225), "Para inciar, pressione ENTER")
  text1.setFace("helvetica")
  text1.setSize(16)
  text1.draw(win)
  
  while win.checkKey() != "Return": continue
      
  logo.undraw()
  text.undraw()
  text1.undraw()
  
  return blackShips, redShips, [base, base1, line]

# Desenhar a interface de visualização de recursoss
def renderResourceBoard(win, objects):
  rec = Rectangle(Point(500,460), Point(850, 540))
  rec.draw(win)
  rec.setWidth(0)
  rec.setFill("#BBBBBB")
  
  resourceFrame = Rectangle(Point(510,470), Point(840, 485))
  resourceFrame.setOutline("#777777")
  resourceFrame.setWidth(2)
  resourceFrame.draw(win)
  
  resourceBar = Rectangle(Point(511,471), Point(839, 484))
  resourceBar.setWidth(0)
  resourceBar.setFill("#666666")
  resourceBar.draw(win)
    
  resourceText = Text(Point(675,477), "100%")
  resourceText.setSize(8)
  resourceText.setStyle("bold") 
  resourceText.setFace("helvetica")
  resourceText.setTextColor("#FFFFFF")
  resourceText.draw(win)
  
  objects.append(rec)
  objects.append(resourceFrame)

  return resourceBar, resourceText, objects


# Desenhar os botões de dificuldade
def renderDificultyButtons(win):
  difRec = Rectangle(Point(880, 490), Point(1070, 540))
  difRec.setFill("#BBBBBB")
  difRec.setWidth(2)
  difRec.setOutline("#BBBBBB")
  difRec.draw(win)
      
  easyButton = Rectangle(Point(895, 500), Point(940, 530))
  easyButton.setFill("#888888")
  easyButton.setWidth(0)
  easyButton.draw(win)
  
  mediumButton = Rectangle(Point(952.5, 500), Point(997.5, 530))
  mediumButton.setFill("#444444")
  mediumButton.setWidth(0)
  mediumButton.draw(win)
  
  hardButton = Rectangle(Point(1010, 500), Point(1055, 530))
  hardButton.setFill("#888888")
  hardButton.setWidth(0)
  hardButton.draw(win)
  
  easyText = Text(Point(917,515), "Easy")
  easyText.setSize(10)
  easyText.setFace("helvetica")
  easyText.setTextColor("#FFFFFF")
  easyText.setStyle("bold")
  easyText.draw(win)
  
  mediumText = Text(Point(975,515), "Normal")
  mediumText.setSize(9)
  mediumText.setFace("helvetica")
  mediumText.setTextColor("#FFFFFF")
  mediumText.setStyle("bold")
  mediumText.draw(win)
  
  hardText = Text(Point(1032,515), "Hard")
  hardText.setSize(10)
  hardText.setFace("helvetica")
  hardText.setTextColor("#FFFFFF")
  hardText.setStyle("bold")
  hardText.draw(win)

  return easyButton, mediumButton, hardButton, easyText, mediumText, hardText, difRec


# Desenhar interface de comando dos navios
def renderAddShipsButtons(win):
  button = Rectangle(Point(300,460), Point(340, 500))
  button.draw(win)
  button.setWidth(0)
  button.setFill("#BBBBBB")
  
  button1 = Rectangle(Point(360,460), Point(400, 500))
  button1.draw(win)
  button1.setWidth(0)
  button1.setFill("#BBBBBB")
  
  button2 = Rectangle(Point(420,460), Point(460, 500))
  button2.draw(win)
  button2.setWidth(0)
  button2.setFill("#BBBBBB")
  
  shipFigure = Polygon(Point(305,488),Point(305,484),Point(311,484),Point(311,480),Point(313,480),Point(313,478),
                  Point(317,478),Point(317,485),Point(332,485),Point(332,483),Point(334,483),Point(334,488))
    
  shipFigure.setFill("#555555")
  shipFigure.setOutline("#555555")
  shipFigure.setWidth(0)
  shipFigure.draw(win)
  
  shipFigure1 = Polygon(Point(367,488),Point(367,484),Point(369,484),Point(369,476),Point(375,476),Point(375,480),
                          Point(387,480),Point(387,482),Point(390,482),Point(390,485),Point(393,485),Point(393,488))

  shipFigure1.setFill("#555555")
  shipFigure1.setOutline("#555555")
  shipFigure1.setWidth(0)
  shipFigure1.draw(win)

  shipFigure2 = Polygon(Point(428,488),Point(425,484),Point(442,484),Point(442,478),Point(445,478),Point(445,480),
                          Point(448,480),Point(448,482),Point(445,482),Point(445,484),Point(455,484),Point(452,488))
  
  
  shipFigure2.setFill("#555555")
  shipFigure2.setOutline("#555555")
  shipFigure2.setWidth(0)
  shipFigure2.draw(win)

  numberText = Text(Point(308,468), "0")
  numberText.setSize(8)
  numberText.setStyle("bold") 
  numberText.setFace("helvetica")
  numberText.setTextColor("#000000")
  numberText.draw(win)
  
  numberText1 = Text(Point(368,468), "0")
  numberText1.setSize(8)
  numberText1.setStyle("bold") 
  numberText1.setFace("helvetica")
  numberText1.setTextColor("#000000")
  numberText1.draw(win)
  
  numberText2 = Text(Point(428,468), "0")
  numberText2.setSize(8)
  numberText2.setStyle("bold") 
  numberText2.setFace("helvetica")
  numberText2.setTextColor("#000000")
  numberText2.draw(win)
  
  addShipButton1 = {"object":button ,"coords":[300,340,460,500] ,"price":200 }
  addShipButton2 = {"object":button1 ,"coords":[360,400,460,500] ,"price":400 }
  addShipButton3 = {"object":button2 ,"coords":[420,460,460,500] ,"price":700 }

  buttonOverlay1 = {"object":None ,"coords":[300,340,460,500] ,"current%":0 ,"last%":0 }
  buttonOverlay2 = {"object":None ,"coords":[360,400,460,500] ,"current%":0 ,"last%":0 }
  buttonOverlay3 = {"object":None ,"coords":[420,460,460,500] ,"current%":0 ,"last%":0 }

  buttonText1 = {"object":numberText ,"currentNum":0 ,"lastNum":0 }
  buttonText2 = {"object":numberText1 ,"currentNum":0 ,"lastNum":0 }
  buttonText3 = {"object":numberText2 ,"currentNum":0 ,"lastNum":0 }

  shipIcon1 = {"object":shipFigure ,"price":200 ,"currentColor":'dark' }
  shipIcon2 = {"object":shipFigure1 ,"price":400 ,"currentColor":'dark' }
  shipIcon3 = {"object":shipFigure2 ,"price":700 ,"currentColor":'dark' }
  
  addShipButtons = [addShipButton1, addShipButton2, addShipButton3]
  buttonOverlays = [buttonOverlay1, buttonOverlay2, buttonOverlay3]
  buttonTexts = [buttonText1, buttonText2, buttonText3]
  shipIcons = [shipIcon1, shipIcon2, shipIcon3]

  return addShipButtons, buttonOverlays, buttonTexts, shipIcons

# Desenhar interface de comando de recursos
def renderCommandButtons(win):
  cmdButton1 = Rectangle(Point(515,500), Point(665, 530))
  cmdButton1.draw(win)
  cmdButton1.setWidth(0)
  cmdButton1.setFill("#999999")
  
  cmdButton2 = Rectangle(Point(685,500), Point(835, 530))
  cmdButton2.draw(win)
  cmdButton2.setWidth(0)
  cmdButton2.setFill("#999999")
  
  cmdIcon1 = Text(Point(595,517), "+ Armazenamento")
  cmdIcon1.setSize(9)
  cmdIcon1.setStyle("bold") 
  cmdIcon1.setFace("helvetica")
  cmdIcon1.setTextColor("#000000")
  cmdIcon1.draw(win)
  
  cmdIcon2 = Text(Point(760,517), "+ Produção")
  cmdIcon2.setSize(9)
  cmdIcon2.setStyle("bold") 
  cmdIcon2.setFace("helvetica")
  cmdIcon2.setTextColor("#000000")
  cmdIcon2.draw(win)

  cmdText1 = Text(Point(522,510), "")
  cmdText1.setSize(16)
  cmdText1.setStyle("bold") 
  cmdText1.setFace("helvetica")
  cmdText1.setTextColor("#000000")
  cmdText1.draw(win)
  
  cmdText2 = Text(Point(692,510), "")
  cmdText2.setSize(16)
  cmdText2.setStyle("bold") 
  cmdText2.setFace("helvetica")
  cmdText2.setTextColor("#000000")
  cmdText2.draw(win)
  
  commandButton1 = {"object":cmdButton1 ,"coords":[515,665,500,530] }
  commandButton2 = {"object":cmdButton2 ,"coords":[685,835,500,530] }

  commandButtonOverlay1 = {"object":None ,"coords":[515,665,500,530] ,"current%":0 ,"last%":0 }
  commandButtonOverlay2 = {"object":None ,"coords":[685,835,500,530] ,"current%":0 ,"last%":0 }

  commandButtonText1 = {"object":cmdText1 ,"currentNum":0 ,"lastNum":0 }
  commandButtonText2 = {"object":cmdText2 ,"currentNum":0 ,"lastNum":0 }

  commandButtonIcon1 = {"object":cmdIcon1 ,"currentColor":'dark' }
  commandButtonIcon2 = {"object":cmdIcon2 ,"currentColor":'dark' }

  cmdButtons = [commandButton1, commandButton2]
  cmdButtonOverlays = [commandButtonOverlay1, commandButtonOverlay2]
  cmdButtonTexts = [commandButtonText1, commandButtonText2]
  cmdButtonIcons = [commandButtonIcon1, commandButtonIcon2]

  return cmdButtons, cmdButtonOverlays, cmdButtonTexts, cmdButtonIcons


# Desenhar a barra de vida dos time
def renderBasesHp(win, blackXp, redXp, blackFrame, redFrame, blackBar, redBar):
  if blackFrame is None:
    blackFrame = Rectangle(Point(74, 29),Point(576, 46))
    blackFrame.setOutline("#444444")
    blackFrame.setWidth(2)
    blackFrame.draw(win)
    
    redFrame = Rectangle(Point(724, 29),Point(1226, 46))
    redFrame.setOutline("#444444")
    redFrame.setWidth(2)
    redFrame.draw(win)
  
  if blackBar is not None:
    blackBar.undraw()
    redBar.undraw()
      
  blackBar = Rectangle(Point(75, 30),Point( (blackXp/10000) * 500 + 75 , 45))
  blackBar.setWidth(0)
  blackBar.setFill("#777777")
  blackBar.draw(win)
  
  redBar = Rectangle(Point(725, 30),Point( (redXp/10000) * 500 + 725 , 45))
  redBar.setWidth(0)
  redBar.setFill("#cc3333")
  redBar.draw(win) 
  
  return blackFrame, redFrame, blackBar, redBar


# Desenhar a barra de vida dos navios conforme o dano for contabilizado
def renderShipsHp(win, blackShips, redShips, blackDmg, redDmg, firstBlackShipI, firstRedShipI):
  if not blackDmg and not redDmg: return  blackShips, redShips

  if redDmg and len(blackShips):
    firstBlackShip = blackShips[firstBlackShipI]
    firstBlackShipBackPos = firstBlackShip["object"].getPoints()[1].getX()
    firstBlackShipFrontPos = firstBlackShip["object"].getPoints()[-2].getX()
      

    if firstBlackShipFrontPos > 200:
      firstBlackShip["currentHp"] -= redDmg
      firstBlackShip["lineObject"].undraw()
  
      if blackShips[firstBlackShipI]["currentHp"] > 0:
        firstBlackShip = drawShipHp(win, firstBlackShip, 'black', firstBlackShipBackPos)

          
  if len(redShips) and blackDmg:
    firstRedShip = redShips[firstRedShipI]
    firstRedShipBackPos = firstRedShip["object"].getPoints()[1].getX()
    firstRedShipFrontPos = firstRedShip["object"].getPoints()[-2].getX()
    
    if firstRedShipFrontPos < 1100:
      firstRedShip["currentHp"] -= blackDmg
      firstRedShip["lineObject"].undraw()

      if firstRedShip["currentHp"] > 0:
        firstRedShip = drawShipHp(win, firstRedShip, 'red', firstRedShipBackPos)
          
  return blackShips, redShips
    

# Retirar de tela os navios que foram destruídos
def deleteShips(blackShips, redShips, firstBlackShipI, firstRedShipI):
  if len(blackShips) > 0:
    firstBlackShip = blackShips[firstBlackShipI]
    if firstBlackShip["currentHp"] <= 0: 
      firstBlackShip["object"].undraw()

      if firstBlackShip["bulletObject"] is not None: 
        firstBlackShip["bulletObject"].undraw()

      blackShips.pop(firstBlackShipI)

  if len(redShips) > 0:  
    firstRedShip = redShips[firstRedShipI]
    if firstRedShip["currentHp"] <= 0: 
      firstRedShip["object"].undraw()

      if firstRedShip["bulletObject"] is not None:
        firstRedShip["bulletObject"].undraw()
        
      redShips.pop(firstRedShipI)
  
  return blackShips, redShips
 

# Desenhar os navios vermelhos em tela
def renderRedShips(win, redShips, redResource, redShipCounter, redShipIndex):
  if len(redShips): 
    if redShips[-1]["object"].getPoints()[1].getX() > 1250: 
      return redShips, redResource, redShipCounter, redShipIndex
  
  if redShipCounter == 0:
    redShipIndex = randint(0,2)
    redShipCounter = randint(1,4-redShipIndex)
  
  if redResource - shipPrices[redShipIndex] >= 0: 
    redResource -= shipPrices[redShipIndex]
    
    newShip = getNewShip(redShipIndex, 'red')
    newShip = drawShipHp(win, newShip, 'red', 1300)
    newShip["object"].draw(win)
    
    redShips.append(newShip)
    redShipCounter -= 1

  return redShips, redResource, redShipCounter, redShipIndex
    

# Desenhar um novo navio preto em tela       
def renderNewShip(win, blackShips, buttonsOverlay, buttonsText):
  for i in range(len(buttonsOverlay)):
    if buttonsOverlay[i]["last%"] != 0 or buttonsOverlay[i]["current%"] != 100: continue
    
    newShip = getNewShip(i, 'black')
    newShip = drawShipHp(win, newShip, 'black', 0)
    newShip["object"].draw(win)
    
    blackShips.append(newShip)

  return blackShips


# Desenhar os overlays dos botões dos navios
def renderButtonsOverlay(win, buttonsOverlay, buttonsText, buttons):
  for i in range(len(buttonsOverlay)):
    currentOverlay = buttonsOverlay[i]
    
    if currentOverlay["object"] is not None: currentOverlay["object"].undraw()
    
    currentOverlay["last%"] = currentOverlay["current%"]
    
    if currentOverlay["current%"] == 0:
      if buttonsText[i]["currentNum"] != 0: currentOverlay["current%"] = 100
      continue

    if currentOverlay["current%"] == 1: buttonsText[i]["currentNum"] -= 1
    
    x1 = currentOverlay["coords"][0]
    x2 = currentOverlay["coords"][1]
    y1 = currentOverlay["coords"][2]
    y2 = currentOverlay["coords"][3]
    
    yPercentage = currentOverlay["current%"]/100 * (y1-y2)
    
    newOverlay = Rectangle(Point(x1, y2 + yPercentage), Point(x2, y2))
    newOverlay.draw(win)
    newOverlay.setWidth(0)
    newOverlay.setFill("#888888")
    
    currentOverlay["current%"] -= 100/shipHps[i]
    currentOverlay["object"] = newOverlay
      
  for i in buttonsText:
    if i["currentNum"] == i["lastNum"]: continue
    
    i["object"].setText(i["currentNum"])
    i["lastNum"] = i["currentNum"]
  
  return buttonsOverlay, buttonsText
      

# Desenhar os overlays dos botões de comando de recursos
def renderCmdButtonsOverlay(win, cmdButtonsOverlay, cmdButtons, cmdButtonsText):
  for i in range(len(cmdButtonsOverlay)):
    currentOverlay = cmdButtonsOverlay[i]

    if currentOverlay["object"] is not None: currentOverlay["object"].undraw()
    
    if currentOverlay["current%"] < 0.01 and currentOverlay["current%"] > -0.01: continue
    
    x1 = currentOverlay["coords"][0]
    x2 = currentOverlay["coords"][1]
    y1 = currentOverlay["coords"][2]
    y2 = currentOverlay["coords"][3]
    
    yPercentage = currentOverlay["current%"]/100 * (y1-y2)
    
    newOverlay = Rectangle(Point(x1, y2 + yPercentage), Point(x2, y2))
    newOverlay.setWidth(0)
    newOverlay.setFill("#888888")
    newOverlay.draw(win)
    
    currentOverlay["current%"] -= 0.1
    currentOverlay["object"] = newOverlay
    
      
  for i in cmdButtonsText: 
    if i["currentNum"] == i["lastNum"] or i["currentNum"] > 5: continue
    
    i["object"].setText(i["currentNum"]*"*")
    i["lastNum"] = i["currentNum"]
    
    if i["currentNum"] != 1 :i["object"].move(4.3,0)

  return cmdButtonsOverlay, cmdButtonsText
      

# Mostrar o cenário final
def renderFinalCenario(win, blackXp, introObjects, ships, 
  shipButtons, cmdButtons, resourceItems, hpItems, dificultyButtons):

  gameOver = False
  if blackXp < 0: 
    introObjects[0].undraw()
    gameOver = True
  else: introObjects[1].undraw()

  msgBlock = Rectangle(Point(430, 125),Point(870, 325))
  msgBlock.setFill("#999999")
  msgBlock.setOutline("#666666")
  msgBlock.setWidth(2)
  msgBlock.draw(win)

  text = Text(Point(650,180), "BLACK NAVY WAR")
  text.setFace("helvetica")
  text.setSize(20)
  text.setStyle("bold")
  text.draw(win)

  text1 = Text(Point(650,215), 
    "Vitória do time {}".format("vermelho!" if gameOver else "preto!"))
  text1.setFace("helvetica")
  text1.setSize(16)
  text1.draw(win)
  if gameOver: text1.setTextColor("#cc1111")

  text2 = Text(Point(650,260), 
    "Para continuar, pressione Enter.\nPara sair, presisone Esc.")
  text2.setFace("helvetica")
  text2.setSize(16)
  text2.draw(win)

  while True:
    key = win.checkKey()
    if key == "Return":
      for i in introObjects: i.undraw()
      for i in resourceItems: i.undraw()
      for i in hpItems: i.undraw()
      for i in dificultyButtons: i.undraw()
      
      for i in shipButtons:
        if i["object"] is not None: i["object"].undraw()

      for i in cmdButtons: 
        if i["object"] is not None: i["object"].undraw()

      for i in ships: 
        i["object"].undraw()
        i["lineObject"].undraw()
        i["bulletObject"].undraw()

      msgBlock.undraw()
      text.undraw()
      text1.undraw()
      text2.undraw()
      return False

    elif key == "Escape": return True