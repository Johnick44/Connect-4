

class Game:

    # Skeleton of the game connect 4, where Player 1 and Player 2 have to
    # think of a strategy against each other in order to win, first person
    # to put 4 signs in a row will win the game, this row can be vertical,
    # horizontal, and diagonal.

    def __init__(self):

        # Initializes all of the players movements and also creates the map for
        # the player.
        self.rows_count = 6
        self.column_count = 7
        self.player1 = "X"
        self.player2 = "Y"
        self.moves = 1
        self.current_map = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

        Game.display(self, self.current_map)

    def display(self, maps):
            print(maps)

    def move(self):

        # Makes a player make a command that will allow to put a sign in which
        # the position given
        point = int(input("please put a number between 0-6:"))
        if 0 <= point <= 6:
            if self.moves % 2 == 0:
                Game.update_map(self, point, self.player2)
                Game.display(self, self.current_map)
            else:
                Game.update_map(self, point, self.player1)
                Game.display(self, self.current_map)
            self.moves += 1
        else:
            raise ValueError("The number selected is either below 0 or above 6,\
             please put another number in between 0-6!")

    def update_map(self, position, sign):
        # Updates the map so that self.current_map has a new sign.
        count = 0
        while count <= len(self.current_map):
            if (self.current_map[5 - count][position] == self.player1) \
                    or (self.current_map[5 - count][position] == self.player2):
                count += 1
            else:
                self.current_map[5 - count][position] = sign
                Game.win(self, sign)
                count = 7

    def win(self, sign):
        # Horizontal Win
        for rows in range(self.rows_count):
            for columns in range(self.column_count-3):
                if self.current_map[rows][columns] == sign \
                    and self.current_map[rows][columns+1] == sign and \
                    self.current_map[rows][columns+2] == sign and \
                        self.current_map[rows][columns+3] == sign:
                    Game.display(self, self.current_map)
                    Game.game_over(self)
        # Vertical Win
        for rows in range(self.rows_count-3):
            for columns in range(self.column_count):
                if self.current_map[rows][columns] == sign \
                    and self.current_map[rows+1][columns] == sign and \
                    self.current_map[rows+2][columns] == sign and \
                        self.current_map[rows+3][columns] == sign:
                    Game.display(self, self.current_map)
                    Game.game_over(self)
        # Diagonal Positive Win
        for rows in range(self.rows_count-3):
            for columns in range(self.column_count-3):
                if self.current_map[rows][columns] == sign \
                    and self.current_map[rows+1][columns+1] == sign and \
                    self.current_map[rows+2][columns+2] == sign and \
                        self.current_map[rows+3][columns+3] == sign:
                    Game.display(self, self.current_map)
                    Game.game_over(self)
        # Diagonal Negative Win
        for rows in range(-1, 2-self.rows_count, -1):
            for columns in range(self.column_count-3):
                if self.current_map[rows][columns] == sign \
                    and self.current_map[rows-1][columns+1] == sign and \
                    self.current_map[rows-2][columns+2] == sign and \
                        self.current_map[rows-3][columns+3] == sign:
                    Game.display(self, self.current_map)
                    Game.game_over(self)

    def game_over(self):
        print("Winner Winner Chicken Dinner "
              "\n good job! "
              "\n new game will start now!")
        self.current_map = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

if __name__ == '__main__':
    g = Game()
    while True:
        g.move()
