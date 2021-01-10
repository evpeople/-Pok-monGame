class People:
    """人物"""

    def __init__(self):
        self.name = "xh"
        self.__money = 1
        self.__bag = []

    def changeName(self, name="None"):
        self.name = name

    def useMoney(self, method="use", money=1):
        if method == "use":
            self.__money -= money
        else:
            self.__money += money

    def useBag(self, method="use", thing="rubbish"):
        if method == "use":
            self.__bag.append(thing)
        else:
            self.__bag.append(thing)


class NPC(People):
    def buy(self, money=1):
        self.useMoney("use", money)
        self.useBag("use")