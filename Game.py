import players.py

class Game:
    ''' Skeleton of the game connect 4, where Player 1 and Player 2 have to think of a
    strategy against each other in order to win, first person to put 4 signs in a row
    will win the game, this row can be vertical, horizontal, and diagonal.'''


    def __init__(self, position1, position2):
        '''Initializes all of the players movements and also creates the map for the player.'''
        self.count = 0
        self.position1 = position1
        self.position2 = position2
        self.turn = randint()
        self.player1 = P1.first
        self. player2 = P2.first
        if (P1.first == P2.first) and (P1.last == P2.last):
            print("Player1 or Player2 please select another name, thank you!")
        self.current_map = [
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0]
                       ]

    def move(self):

        if self.turn % 2 == 0:
            self.position1 = input(int())
            if self.position1.isalp() or  ((self.position1>=7) or (self.position1<=-1)):
                raise AttributeError
            else:
                Game.update_map(self, self.position1)
        else:
            self.position2 = input(int())
            if self.position2.isalp() or ((self.position2>=7) or (self.position2<=-1)):
                raise AttributeError
            else:
                Game.update_map(self, self.position2)

    def update_map(self, position):
        self.count = 0
        if self.turn % 2 == 0:
            for row in self.current_map:
                for columb in row:
                    if self.current_map[5-self.count][position] == 0:
                        self.count+=1
                        Game.update_map(self, self.position1)
                    else:
                        self.current_map[5-self.count][position] = Player.P1.sign1
        for row in self.current_map:
            for columb in row:
                if self.current_map[5-self.count][position] == 0:
                    self.count += 1
                    Game.update_map(self, self.position2)
                else:
                    self.current_map[5-self.count][position] = Player.P2.sign2



