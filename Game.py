from players import P1, P2
import random


class Game:
    ''' Skeleton of the game connect 4, where Player 1 and Player 2 have to
    think of a strategy against each other in order to win, first person to put
    4 signs in a row will win the game, this row can be vertical, horizontal,
    and diagonal.'''


    def __init__(self, position1: int, position2: int):
        '''Initializes all of the players movements and also creates the map for
         the player.'''

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
                (self.player1.last == self.placyer2.last):
            print("Player1 or Player2 please select another name, thank you!")
            raise AttributeError

    def move(self):
        '''Makes a player make a command that will allow the '''
        if self.turn % 2 == 0:
            self.position1 = int(input())
            if(self.position1 >= 7) or (self.position1 <= -1):
                raise AttributeError
            else:
                Game.update_map(self, self.position1)
                return self.current_map
        else:
            self.position2 = int(input())
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
        vertical_count = 0
        horizontal_count = 0
        diagonal_count = 0
        while vertical_count != 4 or horizontal_count !=4 or diagonal_count != 4:
