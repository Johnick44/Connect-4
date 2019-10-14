from players import P1, P2
import random


class Game:
    '''
     Skeleton of the game connect 4, where Player 1 and Player 2 have to
    think of a strategy against each other in order to win, first person to put
    4 signs in a row will win the game, this row can be vertical, horizontal,
    and diagonal.
    '''


    def __init__(self, position1: int, position2: int):
        '''
        Initializes all of the players movements and also creates the map for
        the player.
         '''

        self.position1 = position1
        self.position2 = position2
        self.turn = random.randint()
        self.player1 = P1(input(), input(), input())
        self. player2 = P2(input(), input(), input())
        self.current_map = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

        if (self.player1.first == self.player2.first) and \
                (self.player1.last == self.player2.last):
            print("Player1 or Player2 please select another name, thank you!")
            raise AttributeError

    def move(self, point):
        '''
        Makes a player make a command that will allow to put a sign in which
        the position given'''
        if self.turn % 2 == 0:
            self.position1 = int(point)
            if(self.position1 >= 7) or (self.position1 <= -1):
                raise AttributeError
            else:
                Game.update_map(self, self.position1)
                return self.current_map
        else:
            self.position2 = int(point)
            if(self.position2 >= 7) or (self.position2 <= -1):
                raise AttributeError
            else:
                Game.update_map(self, self.position2)
                return self.current_map

    def update_map(self, position):
        count = 0
        while count <= len(self.current_map):
            if (self.current_map[5-count][position] == P1.sign1) \
                or(self.current_map[5-count][position] == P2.sign2):
                count+= 1
            else:
                if self.turn % 2 ==0:
                    self.current_map[5-count][position] = P1.sign1
                    return
                else:
                    self.current_map[5-count][position] = P2.sign2
                    return


    def win(self):
        column_count = 6
        row_count = 5
        #check for horizontal win
        for column in range(column_count-3):
            for row in range(row_count):
                if self.current_map[row][column] == P2.sign2 \
                    and self.current_map[row][column+1] == P2.sign2 \
                    and self.current_map[row][column+2] == P2.sign2 \
                    and self.current_map[row][column+3] == P2.sign2:
                    return True
                elif self.current_map[row][column] == P1.sign1 \
                    and self.current_map[row][column+1] == P1.sign1 \
                    and self.current_map[row][column+2] == P1.sign1 \
                    and self.current_map[row][column+3] == P1.sign1:
                    return True
        #check for vertical win
