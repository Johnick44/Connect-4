class Player:
    first = ""
    ''' Defining what a player  in connect 4.'''
    def __init__(self, first, last):
        self.first = first
        self.last = last

class P1(Player):
    ''' Input data for player 1, this includes name and sign.'''
    def __init__(self, first, last, sign1):
        Player.__init__(self, first, last)
        self.sign1 = sign1
        if self.sign1 == 0:
            print("please select another sign")
            raise AttributeError
class P2(Player):
    ''' Input data for player 2, this includes name and sign. '''
    def __init__(self, first, last, sign2):
        Player.__init__(self, first, last)
        self.sign2 = sign2
        if self.sign2 == 0:
            print("please select another sign")
            raise AttributeError
