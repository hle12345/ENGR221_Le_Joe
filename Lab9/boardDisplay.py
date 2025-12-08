"""
Author: Prof. Alyssa
Description: Creates and displays the graphics
    based on the current state of the board.

Assignment adapted from HMC CS60

# Description:
#   Handles all drawing and rendering of the Snake game using pygame.
#   The updateGraphics method fills each cell with the color specified
#   by gameData.getCellColor(), and draws the snake head image if loaded.

"""

import pygame
from preferences import Preferences

class BoardDisplay:
    def __init__(self):
        # The display where the board is drawn
        self.__display = pygame.display.set_mode((Preferences.GAME_BOARD_WIDTH, Preferences.GAME_BOARD_HEIGHT))
        # Image to show as the "head"
        self.headImage = None
        # Offsets used for the balancing/rotation visual effect
        self.__xOffset = 0
        self.__yOffset = 0

    def updateGraphics(self, gameData):
        """ Re-draws the board, food, and snake based
            on the current state of the board """
        self.clear()

        # --- Traversal visualization: build a mapping cell -> traversal index ---
        traversalIndexByCell = {}
        if hasattr(gameData, "getTraversalMode") and hasattr(gameData, "getSnakeCells"):
            mode = gameData.getTraversalMode()
            snake = gameData.getSnakeCells()
            if mode != 0 and len(snake) > 0:
                n = len(snake)
                order_indices = []

                if mode == 1:
                    # Preorder traversal on an implicit tree (array indices)
                    def pre(i):
                        if i >= n:
                            return
                        order_indices.append(i)
                        pre(2 * i + 1)
                        pre(2 * i + 2)
                    pre(0)

                elif mode == 2:
                    # Postorder traversal
                    def post(i):
                        if i >= n:
                            return
                        post(2 * i + 1)
                        post(2 * i + 2)
                        order_indices.append(i)
                    post(0)

                elif mode == 3:
                    # Level-order traversal (BFS on indices)
                    queue = [0]
                    while queue:
                        i = queue.pop(0)
                        if i >= n:
                            continue
                        order_indices.append(i)
                        queue.append(2 * i + 1)
                        queue.append(2 * i + 2)

                for idx, snakeIndex in enumerate(order_indices):
                    if 0 <= snakeIndex < n:
                        cell = snake[snakeIndex]
                        traversalIndexByCell[cell] = idx

                # --- Balancing / rotation visualization: compute board offsets ---
        self.__xOffset = 0
        self.__yOffset = 0
        if hasattr(gameData, "isBalanceModeOn") and hasattr(gameData, "getSnakeCells"):
            if gameData.isBalanceModeOn():
                snake = gameData.getSnakeCells()
                if len(snake) > 0:
                    sumRow = sum(c.getRow() for c in snake)
                    sumCol = sum(c.getCol() for c in snake)
                    n = len(snake)
                    centerRow = sumRow / n
                    centerCol = sumCol / n

                    midRow = Preferences.NUM_CELLS_TALL / 2.0
                    midCol = Preferences.NUM_CELLS_WIDE / 2.0

                    # If center is left of middle, push board right; else push left.
                    if centerCol < midCol:
                        self.__xOffset = Preferences.ROTATION_SHAKE_AMOUNT
                    else:
                        self.__xOffset = -Preferences.ROTATION_SHAKE_AMOUNT

                    # If center is above middle, push board down; else push up.
                    if centerRow < midRow:
                        self.__yOffset = Preferences.ROTATION_SHAKE_AMOUNT
                    else:
                        self.__yOffset = -Preferences.ROTATION_SHAKE_AMOUNT

        # --- Draw all cells ---
        for row in range(Preferences.NUM_CELLS_TALL):
            for col in range(Preferences.NUM_CELLS_WIDE):
                cell = gameData.getCell(row, col)
                self.drawSquare(cell, gameData, traversalIndexByCell)

        # Draw score in top-left
        self.drawScore(gameData)

        # Draw the game over message, if appropriate
        if gameData.getGameOver():
            self.displayGameOver()

        # Update the display
        pygame.display.update()


    def clear(self):
        """ Resets the background of the display """
        self.__display.fill(Preferences.COLOR_BACKGROUND)

    def drawSquare(self, cell, gameData, traversalIndexByCell):
        """ Draws a cell-sized square at the given location.
        Inputs:
            cell - the Cell to draw
            gameData - current GameData instance
            traversalIndexByCell - dict mapping cell -> traversal index
        """
        row = cell.getRow()
        col = cell.getCol()

        # Special image for head
        if cell.isHead() and self.headImage:
            self.drawImage(row, col, self.headImage)
            return

        # Start from the cell's default color
        cellColor = cell.getCellColor()

        # Override food color based on its priority (heap-like)
        if cell.isFood() and hasattr(gameData, "getFoodPriority"):
            priority = gameData.getFoodPriority(cell)
            if priority == 3:
                cellColor = Preferences.COLOR_FRUIT_PRIORITY_HIGH
            elif priority == 2:
                cellColor = Preferences.COLOR_FRUIT_PRIORITY_MED
            else:
                cellColor = Preferences.COLOR_FRUIT_PRIORITY_LOW

        # If this cell is part of the traversal order, highlight it
        if cell in traversalIndexByCell:
            idx = traversalIndexByCell[cell]
            if idx == 0:
                # "Root" of traversal
                cellColor = Preferences.COLOR_TRAVERSAL
            else:
                cellColor = Preferences.COLOR_TRAVERSAL_SECOND

        # Apply offsets for balancing/rotation effect
        x = col * Preferences.CELL_SIZE + self.__xOffset
        y = row * Preferences.CELL_SIZE + self.__yOffset

        pygame.draw.rect(
            self.__display,
            cellColor,
            [x, y, Preferences.CELL_SIZE, Preferences.CELL_SIZE],
        )

    def drawImage(self, row, col, image):
        """ Displays an image at the given cell location.
            Inputs: row - row coordinate to draw the image at
                    col - column coordinate to draw the image at
                    image - the pygame image to draw """

        # First, convert the image to a Surface type (with transparent background)
        image = image.convert_alpha()
        # You will want to uncomment the below line if you want your image to fit within one cell
        #image = pygame.transform.scale(image, (Preferences.CELL_SIZE, Preferences.CELL_SIZE))
        # Grab the dimensions of the image
        imageRect = image.get_rect()
        # Place the image in the center of the given cell coordinates
        imageRect.center = (
            (col * Preferences.CELL_SIZE) + (Preferences.CELL_SIZE / 2) + self.__xOffset,
            (row * Preferences.CELL_SIZE) + (Preferences.CELL_SIZE / 2) + self.__yOffset,
        )

        # Place the image on the display
        self.__display.blit(image, imageRect)

    def drawScore(self, gameData):
        """Draw the current score in the upper-left corner."""
        if not hasattr(gameData, "getScore"):
            return
        score = gameData.getScore()
        font = pygame.font.SysFont("arial", 24, bold=True)
        text = font.render(f"Score: {score}", True, pygame.Color("black"))
        self.__display.blit(text, (10, 10))


    def displayGameOver(self):
        """ Displays the game over message """

        # Get the font
        font = Preferences.GAME_OVER_FONT
        # Create the text
        text = font.render(Preferences.GAME_OVER_TEXT, True, Preferences.GAME_OVER_COLOR)
        # Get the dimensions of the text box
        textRect = text.get_rect()
        # Specify the location of the text
        textRect.center = (Preferences.GAME_OVER_X, Preferences.GAME_OVER_Y)
        # Place the game over text on the display
        self.__display.blit(text, textRect)