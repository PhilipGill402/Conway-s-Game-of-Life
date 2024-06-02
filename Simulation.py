from Constants import XCELLS, YCELLS

class Simulation:
    def checkNeighbors(self, x:int, y:int, board:list) -> int:
        total = 0
        for i in range(8):
            altY = y
            altX = x
            if i == 0:
                altY += 1
            elif i == 1:
                altX += 1
                altY += 1
            elif i == 2:
                altX += 1
            elif i == 3:
                altX += 1
                altY -= 1
            elif i == 4:
                altY -= 1
            elif i == 5:
                altX -= 1
                altY -=1
            elif i == 6:
                altX -= 1
            elif i == 7:
                altX -= 1
                altY += 1
            
            if altX >= XCELLS:
                altX = altX % XCELLS
            if altY >= YCELLS:
                altY = altY % YCELLS

            if board[altY][altX]:
                total += 1
        
        return total

    def calcNumAlive(self, board:list) -> int:
        count = 0
        for i in range(len(board)):
            for j in board[i]:
                if j:
                    count += 1
        
        return count