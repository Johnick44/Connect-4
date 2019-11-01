

class Game:

    # Skeleton of the game connect 4, where Player 1 and Player 2 have to
    # think of a strategy against each other in order to win, first person
    # to put 4 signs in a row will win the game, this row can be vertical,
    # horizontal, and diagonal.

    def __init__(self):

        # Initializes all of the players movements and also creates the map for
        # the player.
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
        player1 = "X"
        player2 = "Y"
        if 0 <= point <= 6:
            if self.moves % 2 == 0:
                Game.update_map(self, point, player2)
                Game.display(self, self.current_map)
            else:
                Game.update_map(self, point, player1)
                Game.display(self, self.current_map)
            self.moves += 1
        else:
            raise TypeError

    def update_map(self, position, sign):
        # Updates the map so that self.current_map has a new sign.
        count = 0
        while count <= len(self.current_map):
            if (self.current_map[5 - count][position] == "X") \
                    or (self.current_map[5 - count][position] == "Y"):
                count += 1
            else:
                self.current_map[5 - count][position] = sign
                Game.win(self, sign)

    def win(self, sign):
        column_count = 6
        row_count = 5
        # check for horizontal win
        for column in range(column_count - 3):
            for row in range(row_count):
                if self.current_map[row][column] == sign \
                        and self.current_map[row][column + 1] == sign \
                        and self.current_map[row][column + 2] == sign \
                        and self.current_map[row][column + 3] == sign:
                    Game.display(self, self.current_map)
                    Game.Game_Over(self)
        # check for vertical win
        for column in range(column_count):
            for row in range(row_count - 3):
                if self.current_map[row][column] == sign \
                        and self.current_map[row + 1][column] == sign \
                        and self.current_map[row + 2][column] == sign \
                        and self.current_map[row + 3][column] == sign:
                    Game.display(self, self.current_map)
                    Game.Game_Over(self)

    def Game_Over(self):
        print("Winner Winner Chicken Dinner")
        return True


if __name__ == '__main__':
    g = Game()
    while g.Game_Over():
        g.move()
