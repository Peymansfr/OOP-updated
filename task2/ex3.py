import random

class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def toss_the_coin(self):
        posibility = random.randint(1, 100)
        if posibility <= 35:
            self.sideup = "Heads"
        elif posibility <= 70:
            self.sideup = "Tails"
        elif posibility <= 85:
            self.sideup = "Upright"
        elif posibility <= 95:
            self.sideup = "Rabbit Hole"
        else:
            self.sideup = "Wormhole"

    def get_sideup(self):
        return self.sideup

def main():
    my_coin = Coin()
    print("this side is up:", my_coin.get_sideup())
    print("tossing the coin ...")
    my_coin.toss_the_coin()
    print("Now this side is up:", my_coin.get_sideup())

main()