elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # (x, y) location of the mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col): # the user clicked the same square twice
                    sqSelected = () # deselect
                    playerClicks = [] # clear player clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) # append for both 1st and 2nd clicks
                if len(playerClicks) == 2: # after 2nd click
                    move = chessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = () # reset user clicks
                    playerClicks = []