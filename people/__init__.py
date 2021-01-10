from Elves import HumanElves, NatureElves


class People:
    """人物"""

    def __init__(self):
        self.name = "xh"
        self.location = "home"
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
            try:
                self.__bag.remove(thing)
                print("you used" + thing)
                return thing
            except ValueError:
                print("you don't have " + thing)
                return 0


class NPC(People):
    def buy(self, money=1, thing="rubbish"):
        self.useMoney("use", money)
        self.useBag("use", thing)

    def sell(self, money=1, thing="rubbish"):
        self.useMoney("sell", money)
        self.useBag("sell", thing)

    def use(self, thing="rubbish"):
        a = self.useBag("sell", thing)
        return a


class Player(NPC):
    def __init__(self):
        super().__init__()
        firstElves = HumanElves()
        self.__ElvesBag = [firstElves]

    def catchElves(self, Elves: NatureElves):
        dicOfCatch = {"rubbish": 1}
        a = self.use()
        if a == 0:
            return
        else:
            t = Elves.avoidCatch(dicOfCatch[a])
            if t == 1:
                self.__ElvesBag.append(HumanElves(self.name, hp=Elves.consthp))
            else:
                print("you lose")

    def changeLocation(self, location="home"):
        self.location = location

    def showElves(self):
        print(self.__ElvesBag)

    def useElves(self, number=0):
        return self.__ElvesBag[number]
