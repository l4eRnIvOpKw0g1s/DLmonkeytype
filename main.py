  import pgzrun
  import random
  WIDTH = 500
  HEIGHT = 450

  #intro setup
  pictureRect = Rect((100, 382), (90, 35))
  cardAmtRect = [Rect((100, 150), (90, 60)), Rect((310, 150), (90, 60))]
  gameModeRect = [Rect((100, 267), (90, 60)), Rect((200, 267), (100, 60)), Rect((310, 267), (90, 60))]
  startRect = Rect((290, 350), (180, 70))

  cardAmt = 14
  intro = True
  pictMode = False
  popCards = False
  notifTimer = 0
  gameMode = 0
  hardCPU = False
  impossibleCPU = False
  counter = 0

  #game variables
  cards = []
  cardValues = []
  cardFlipTimer = 0
  storedCard = None
  currentCard = None
  comparisons = 0
  matches = 0
  matchesP2 = 0
  player1Turn = bool(random.getrandbits(1))
  botStorage = []
  botTimer = 0

  #ended setup
  ending = False
  resetRect = Rect((100, 374), (202, 56))

  for i in range(24):
    #creating card list
    cards.append(Rect((20 + (80 * (i%6)), 20 + (80 * (i//6))), (70, 70)))

  def draw():
    if intro:
      #background
      screen.blit("cardsbg", (0, 0)) 
      
      #title and text under
      screen.draw.text("MATCHING CARDS", (53, 48), fontname="sketch", fontsize=40)
      screen.draw.text("Amount of Cards:", (163, 126), fontsize=30)
      screen.draw.text("Game Mode:", (186, 243), fontsize=30)
    
      screen.draw.filled_rect(startRect, color="black")
      screen.draw.text("PLAY", (310, 360), fontsize = 80)
      #pictmode button
      screen.draw.text("Picture Mode:", (92, 357))
      if pictMode:
        screen.draw.filled_rect(pictureRect, color="orange")
        screen.draw.text("ON", (122, 387), fontsize=40)
      else:
        screen.draw.filled_rect(pictureRect, color="gray")
        screen.draw.text("OFF", (118, 387), fontsize=40, color = "black")
      screen.draw.rect(pictureRect, color="black")
      
      #amt of cards
      screen.draw.filled_rect(Rect((200, 150), (100, 60)), color="white")
      screen.draw.rect(Rect((200, 150), (100, 60)), color="black")
      #centering the number
      if cardAmt < 10:
        screen.draw.text(str(cardAmt), (242, 165), color="black", fontsize=55)
      else:
        screen.draw.text(str(cardAmt), (230, 165), color="black", fontsize=55)

      
      #delete the number if cannot go higher/lower
      if cardAmt != 8:
        screen.draw.filled_rect(cardAmtRect[0], color="firebrick")
        screen.draw.rect(cardAmtRect[0], color="black")
        screen.draw.text("-2", (129, 165), color="black", fontsize=50)
        
      if cardAmt != 20:
        screen.draw.filled_rect(cardAmtRect[1], color="limegreen")
        screen.draw.rect(cardAmtRect[1], color="black")
        screen.draw.text("+2", (334, 165), color="black", fontsize=50)
    
      #game mode buttons
      if gameMode != 2:
        screen.draw.filled_rect(gameModeRect[2], color="azure")
      else:
        if impossibleCPU:
          screen.draw.filled_rect(gameModeRect[2], color="red")
        elif hardCPU:
          screen.draw.filled_rect(gameModeRect[2], color="orange")
        else:
          screen.draw.filled_rect(gameModeRect[2], color="dodgerblue")
      screen.draw.rect(gameModeRect[2], color="black")
    
      for i in range(2):
        if gameMode != i:
          screen.draw.filled_rect(gameModeRect[i], color="azure")
        else:
          screen.draw.filled_rect(gameModeRect[i], color="dodgerblue")
        screen.draw.rect(gameModeRect[i], color="black")
      screen.draw.text("Solo", (109, 280), fontsize = 50, color="black")
      screen.draw.text("1v1", (222, 280), fontsize = 50, color="black")
      screen.draw.text("CPU", (319, 280), fontsize = 50, color="black")

      
        
      
      if notifTimer > 0:
        if impossibleCPU:
          screen.draw.text("IMPOSSIBLE CPU has been enabled", (30, 23), color="red")
        elif hardCPU:
          screen.draw.text("Hard CPU has been enabled", (30, 23))

        
    #in the game/ending
    else:
      screen.blit("cardsbg2", (0, 0))
      #card designs
      for i in range(len(cards)):
        screen.draw.filled_rect(cards[i], color="white")
        screen.draw.filled_rect(Rect((cards[i][0]+5, cards[i][1]+5), (60, 60)), color="firebrick")
        screen.draw.filled_circle((cards[i][0]+35, cards[i][1]+35), 30, color="white")
        screen.draw.filled_circle((cards[i][0]+35, cards[i][1]+35), 25, color="firebrick")
      
      #flipped cards
      if storedCard != None:
        screen.draw.filled_rect(cards[storedCard], color="white")
        screen.draw.text(str(cardValues[storedCard]), (cards[storedCard][0] + 20, cards[storedCard][1] + 10) , color="black", fontsize=80)
        if pictMode:
          screen.blit(str(cardValues[storedCard]) + "small", (cards[storedCard][0], cards[storedCard][1]))
        screen.draw.rect(cards[storedCard], color="firebrick")
      #second flipped card
      if currentCard != None:
        screen.draw.filled_rect(cards[currentCard], color="white")
        screen.draw.text(str(cardValues[currentCard]), (cards[currentCard][0] + 20, cards[currentCard][1] + 10) , color="black", fontsize=80)
        if pictMode:
          screen.blit(str(cardValues[currentCard]) + "small", (cards[currentCard][0], cards[currentCard][1]))
        screen.draw.rect(cards[currentCard], color="firebrick")
        
      #comparisons/matches in the bottom
      
      screen.draw.text("Flips", (32, 363), fontsize = 30)
      if gameMode == 1:
        if player1Turn:
          screen.draw.text("P1's Turn", (115, 390), fontsize = 60)
        else:
          screen.draw.text("P2's Turn", (115, 390), fontsize = 60)
      if gameMode == 2:
        if player1Turn:
          screen.draw.text("P1's Turn", (115, 390), fontsize = 60)
        else:
          screen.draw.text("CPU's Turn", (102, 393), fontsize = 55)

          
      if gameMode == 0:
        screen.draw.text("Points", (428, 363), fontsize = 25)
          
        if matches < 10:
          screen.draw.text(str(matches), (442, 387), fontsize=70)
        else:
          screen.draw.text(str(matches), (431, 387), fontsize=70)
      else: 
        
        screen.draw.text("P1 points", (318, 365), fontsize = 22)
        if gameMode == 1:
          screen.draw.text("P2 points", (418, 365), fontsize = 22)
        else:  
          screen.draw.text("CPU points", (410, 365), fontsize = 22)
          
        if matches < 10:
          screen.draw.text(str(matches), (342, 387), fontsize=70, color="dodgerblue")
        else:
          screen.draw.text(str(matches), (331, 387), fontsize=70, color="dodgerblue")
          
        if matches < 10:
          screen.draw.text(str(matchesP2), (442, 387), fontsize=70, color="firebrick")
        else:
          screen.draw.text(str(matchesP2), (431, 387), fontsize=70, color="firebrick")
        
      if comparisons < 10:
        screen.draw.text(str(comparisons), (43, 387), fontsize=70)
      else:
        screen.draw.text(str(comparisons), (32, 387), fontsize=70)
          
    if ending:
      if gameMode == 0:
        screen.draw.text("YOU", (115, 30), fontname="noitaliz", fontsize=120)
      else:
        if matches > matchesP2:
          screen.draw.text("P1", (160, 30), fontname="noitaliz", fontsize=120)
        elif matches < matchesP2:
          if gameMode == 1:
            screen.draw.text("P2", (160, 30), fontname="noitaliz", fontsize=120)
          else:
            screen.draw.text("CPU", (120, 30), fontname="noitaliz", fontsize=120)
        else:
          screen.draw.text("TIE", (120, 30), fontname="noitaliz", fontsize = 120)
          screen.draw.text("GAME", (50, 165), fontname="noitaliz", fontsize=120)
      if matches != matchesP2:
        screen.draw.text("WIN!", (100, 165), fontname="noitaliz", fontsize=120)
      
      screen.draw.filled_rect(resetRect, color="firebrick")
      screen.draw.rect(resetRect, color="black")
      screen.draw.text("Reset?", (110, 378), fontsize = 80)
      
      
    


  def update(dt):
    global cardFlipTimer, storedCard, currentCard, ending, intro, popCards, cardValues, matches, matchesP2, notifTimer, player1Turn, comparisons, botTimer, botStorage, impossibleCPU
    
    #timers
    if notifTimer > 0:
      notifTimer -= dt
    if botTimer > 0:
      botTimer -= dt
    if cardFlipTimer > 0:
      cardFlipTimer -= dt

    if counter > 16:
      impossibleCPU = True
    
    #done right after intro
    if popCards:
      #change the amount of cards

      cards.pop(0)
      cards.pop(4)
      if cardAmt == 18:
        for i in range(4):
          cards.pop(0)
      else:
        cards.pop(16)
        cards.pop(20)
        if cardAmt != 20:
          for i in (4, 8, 8, 12):
            cards.pop(i)
          if cardAmt != 16:
            cards.pop(0)
            cards.pop(2)
            if cardAmt != 14:
              cards.pop(0)
              cards.pop(0)
              if cardAmt == 8:
                for i in range(4):
                  cards.pop()
              if cardAmt == 10:
                cards.pop(0)
                cards.pop(2)

      #update card Values
      for i in range(cardAmt):
        cardValues.append(i//2)
      random.shuffle(cardValues)

      #setting up bot storage
      for i in range(len(cards)):
        botStorage.append(-1)
        if impossibleCPU:
          botStorage[-1] = cardValues[i]
        
      popCards = False
  
    if gameMode == 2 and player1Turn == False and intro == False and ending == False:
      if botTimer == 0:
        botTimer = 0.4
      if storedCard == None and botTimer < 0:
        storedCard = random.randint(0, len(cards)-1)
        for i in (cardValues):
          if botStorage.count(i) == 2:
            storedCard = botStorage.index(i)
        
        botTimer = 0.5
        
      elif botTimer < 0 and currentCard == None:
        currentCard = storedCard
        if botStorage.count(cardValues[storedCard]) == 2:
          if storedCard == botStorage.index(cardValues[storedCard]):
            currentCard = len(botStorage) - botStorage[::-1].index(cardValues[storedCard]) - 1
          else: 
            currentCard = botStorage.index(cardValues[storedCard])
          
        if botStorage.count(cardValues[storedCard]) == 1:  
          if storedCard == botStorage.index(cardValues[storedCard]):
            while currentCard == storedCard:
              currentCard = random.randint(0, len(cards)-1)
          else:
            currentCard = botStorage.index(cardValues[storedCard])
            
        if botStorage.count(cardValues[storedCard]) == 0:
          while currentCard == storedCard:
              currentCard = random.randint(0, len(cards)-1)
        cardFlipTimer = 0.75
        

    
    if cardFlipTimer < 0:
      #remove cards
        
      comparisons += 1
      if cardValues[storedCard] == cardValues[currentCard]:
        if gameMode == 0:
          matches += 1
        else:
          if player1Turn:
            matches += 1
          else:
            matchesP2 += 1
        
        if storedCard > currentCard:
          cards.pop(storedCard)
          cardValues.pop(storedCard)
          botStorage.pop(storedCard)
          cards.pop(currentCard)
          cardValues.pop(currentCard)
          botStorage.pop(currentCard)
        else:
          cards.pop(currentCard)
          cardValues.pop(currentCard)
          botStorage.pop(currentCard)
          cards.pop(storedCard)
          cardValues.pop(storedCard)
          botStorage.pop(storedCard)

      else:
        player1Turn = not player1Turn
        if not hardCPU:
          botStorage[random.randint(0, len(botStorage)-1)] = -1
          botStorage[random.randint(0, len(botStorage)-1)] = -1
        botStorage[storedCard] = cardValues[storedCard]
        botStorage[currentCard] = cardValues[currentCard]

        #reset variables
      storedCard = None
      currentCard = None
      cardFlipTimer = 0
      botTimer = 0
      #check for win condition
      if matches + matchesP2 == cardAmt//2:
        ending = True
    
  def on_mouse_up(pos, button):
    global cardAmt, intro, currentCard, cardFlipTimer, storedCard, popCards, pictMode, notifTimer, gameMode, hardCPU, counter
    
    if intro:
      if pictureRect.collidepoint(pos):
        pictMode = not pictMode

      if startRect.collidepoint(pos):
        intro = False
        popCards = True
        
      if gameModeRect[2].collidepoint(pos):
        if gameMode == 2:
          notifTimer = 1
          hardCPU = not hardCPU
          counter += 1
          
        else:
          gameMode = 2
      if not impossibleCPU:
        for i in range(2):
          if gameModeRect[i].collidepoint(pos):
            gameMode = i

          
      #add or remove to total cards in the intro
      if cardAmtRect[0].collidepoint(pos) and cardAmt != 8:
        cardAmt -= 2
      if cardAmtRect[1].collidepoint(pos) and cardAmt != 20:
        cardAmt += 2
      
    #make sure second card cannot be pressed multiple times - you can only process inputs if current card = none
    elif currentCard == None:
      if player1Turn or gameMode != 2:
        for i in range(len(cards)):
          if cards[i].collidepoint(pos):
            #first stored
            if storedCard == None:
              storedCard = i
            #second card then timer till break (only if stored card is not current card to avoid pressing same card twice)
            elif i != storedCard: 
              cardFlipTimer = 0.75
              currentCard = i

            
              
    if ending:
      if resetRect.collidepoint(pos):
        resetVar()
          
  def resetVar():
    global intro, cardFlipTimer, storedCard, currentCard, comparisons, matches, ending, matchesP2, player1Turn, counter, botStorage, impossibleCPU
    intro = True
    counter = 0
    storedCard = None
    currentCard = None
    comparisons = 0
    matches = 0
    matchesP2 = 0
    player1Turn = bool(random.getrandbits(1))
    botStorage = []
    impossibleCPU = False
    ending = False
    for i in range(24):
      cards.append(Rect((20 + (80 * (i%6)), 20 + (80 * (i//6))), (70, 70)))

  pgzrun.go()