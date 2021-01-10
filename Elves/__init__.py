from math import sqrt
from random import randint
from skillOfElves import characterDictionary, skillDictionary


class ElvesFactory:
    """精灵工厂，产生性别，个体值，性格，属性"""

    def __init__(self, __sex=None, __character=None, __attributes=None):
        __deIQ: int
        __deSex = ['male', 'female']
        __deCharacter = ['NB', 'rubbish', 'happy']
        __deAttributes = ['fire', 'water', 'grass']
        if __sex is None:
            __sex = __deSex
        if __attributes is None:
            __attributes = __deAttributes
        if __character is None:
            __character = __deCharacter

        self.__sex = __sex[1]
        self.__IQ = randint(1, 24)
        self.__character = __character[randint(0, 2)]
        self.__attributes = __attributes[randint(0, 2)]

    def __str__(self):
        return str(self.__sex) + str(self.__IQ) + str(self.__attributes) + str(self.__character)

    @property
    def sex(self):
        return self.__sex

    @property
    def IQ(self):
        return self.__IQ

    @property
    def character(self):
        return self.__character

    @property
    def attributes(self):
        return self.__attributes


class ElvesMachine(ElvesFactory):
    """精灵加工，产生攻击力，防御力，体力"""

    def __init__(self, level=1, hp=100, chDic=characterDictionary):
        super(ElvesMachine, self).__init__()
        self.level = level
        self.normalAttack = sqrt(10) * self.IQ * \
                            self.level * chDic.get(self.character + 'NA', 1)
        self.specialAttack = sqrt(
            10) * self.IQ * self.level * chDic.get(self.character + 'SA', 1)
        self.normalDefense = sqrt(
            5) * self.IQ * self.level * chDic.get(self.character + 'ND', 1)
        self.specialDefense = sqrt(
            5) * self.IQ * self.level * chDic.get(self.character + 'SD', 1)
        self.hp = int(hp * sqrt(10))


class NatureElves(ElvesMachine):
    """野生精灵生成器"""

    def __init__(self):
        super(NatureElves, self).__init__()
        self.skill = skillDictionary[self.attributes][self.level]
        self.hp = self.hp * 1.5
        self.consthp = self.hp
        self.catch = 1 / self.IQ

    def battle(self, enemy, numberOfSkill=0):
        battleDictionary = {'NA': self.normalAttack, 'SA': self.specialAttack}
        attack = battleDictionary[self.skill[numberOfSkill]
        [0:2]] * int(self.skill[numberOfSkill][-2:])
        print("use" + self.skill[numberOfSkill][2:-2])
        enemy.defense(attack, "".join([self.skill[numberOfSkill][0:2]]))

    def defense(self, Attack, attackCategory):
        battleDictionary = {'NA': self.normalDefense,
                            'SA': self.specialDefense}
        self.hp -= (Attack - battleDictionary[attackCategory])

    def avoidCatch(self, catchCategory):
        if self.catch < catchCategory:
            return 1
        else:
            return 0


class HumanElves(NatureElves):
    def __init__(self, owner="OS", name="samllHong", hp="-1"):
        super(HumanElves, self).__init__()
        self.__owner = owner
        if hp == -1:
            self.__hp = self.hp / 1.5
        else:
            self.__hp = hp / 1.5
        self.__name = name
        self.__learn = 1
        self.skill = []
        self.__skil = skillDictionary[self.attributes][self.level]

    def __levelUp(self, chDic=characterDictionary):
        self.level += 1
        self.hp = self.level * int(self.hp * sqrt(10))
        self.normalAttack = sqrt(10) * self.IQ * \
                            self.level * chDic.get(self.character + 'NA', 1)
        self.specialAttack = sqrt(
            10) * self.IQ * self.level * chDic.get(self.character + 'SA', 1)
        self.normalDefense = sqrt(
            5) * self.IQ * self.level * chDic.get(self.character + 'ND', 1)
        self.specialDefense = sqrt(
            5) * self.IQ * self.level * chDic.get(self.character + 'SD', 1)

    def checkLevel(self):
        if self.__learn % 10 == 0:
            self.__levelUp()
            print("I am level up")
        else:
            print("I need beat more elves")

    def battle(self, enemy, numberOfSkill=0):
        battleDictionary = {'NA': self.normalAttack, 'SA': self.specialAttack}
        attack = battleDictionary[self.__skill[numberOfSkill]
        [0:2]] * int(self.__skill[numberOfSkill][-2:])
        print("use" + self.__skill[numberOfSkill][2:-2])
        enemy.defense(attack, "".join([self.__skill[numberOfSkill][0:2]]))

    def listOfSkill(self):
        print(self.__skill)

    def learnSkill(self):
        if len(self.__skil) < 4:
            self.__skill = skillDictionary[self.attributes][self.level].append(
                "SA垃圾30")
        else:
            del self.__skill[0]

    def __win(self):
        self.__learn += 1

# TODO  模块名
# TODO  地图类
# TODO  战斗设计
# TODO  模块调用
