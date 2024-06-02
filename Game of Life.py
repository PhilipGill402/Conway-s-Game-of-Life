import pygame
from Board import *
from Simulation import *
import time
from Constants import *
from copy import deepcopy

def getPos(x:int,y:int) -> tuple:
    return (int(x//SQUAREX), int(y//SQUAREY))

pygame.init()
surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")
running = True
board = Board()
gameBoard = board.board
oldBoard = board.oldBoard
dragging = False
simRunning = False
counter = 0

while running:
    surface.fill(BLACK)
    board.drawBoard(surface)
    (x,y) = pygame.mouse.get_pos()
    sim = Simulation()

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if not dragging:
                x,y = getPos(x, y)
                val = not gameBoard[y][x]
                board.changeVal(x,y,val)
            dragging = True
        elif ev.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif ev.type == pygame.MOUSEMOTION:
            if dragging:
                time.sleep(.01)
                x,y = getPos(x, y)
                board.changeVal(x,y,True)
        elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    #begins simulatio
                    simRunning = True
                if ev.key == pygame.K_r:
                    board.board = board.createBoard()
                    gameBoard = board.board
            

    #everyrun of the loop is a new generation
    while simRunning:
        oldBoard = deepcopy(gameBoard)
        surface.fill(BLACK)
        board.drawBoard(surface)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                simRunning = False
                running = False

            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    #ends simulation
                    simRunning = False
        counter += 1
        print(f'Generation {counter}: {sim.calcNumAlive(gameBoard)}')

        for y in range(len(gameBoard)):
            for x in range(len(gameBoard[y])):
                numNeighbors = sim.checkNeighbors(x,y,oldBoard)
                if gameBoard[y][x]:
                    if numNeighbors not in [2,3]:
                        board.changeVal(x,y,False)
                else:
                    if numNeighbors == 3:
                        board.changeVal(x,y,True)
        time.sleep(.075)

        pygame.display.update()

    pygame.display.update()