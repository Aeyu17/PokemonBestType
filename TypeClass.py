import pkmntypes
import csv

class Type(object):
    def __init__(self, primary, secondary=pkmntypes.null):
        """
        primary and secondary are dictionaries
        """
        try:
            self.typeCombo = (
                pkmntypes.typeKeys[pkmntypes.typeList.index(primary)],
                pkmntypes.typeKeys[pkmntypes.typeList.index(secondary)]
            )
        except ValueError:
            self.typeCombo = (
                pkmntypes.typeKeys[pkmntypes.typeList.index(primary)],
                "null"
            )

        self.matchups = pkmntypes.null.copy()

        self.weakList = []
        self.resistList = []
        self.immuneList = []
        self.neutralList = []

        for pkmntype in pkmntypes.typeKeys:
            multiplier = primary[pkmntype] * secondary[pkmntype]
            self.matchups[pkmntype] *= multiplier
            if multiplier > 1:
                self.weakList.append(pkmntype)
            elif multiplier == 0:
                self.immuneList.append(pkmntype)
            elif multiplier < 1:
                self.resistList.append(pkmntype)
            else:
                self.neutralList.append(pkmntype)

        self.offensiveScore = 0
        self.defensiveScore = 0

    def __str__(self):
        if self.typeCombo[1] != "null":
            return f"""Types: {self.typeCombo[0]}, {self.typeCombo[1]}

Weaknesses: {self.weakList}
Resistances: {self.resistList}
Immunities: {self.immuneList}
Neutral: {self.neutralList}
"""
        else:
            return f"""Type: {self.typeCombo[0]}

Weaknesses: {self.weakList}
Resistances: {self.resistList}
Immunities: {self.immuneList}
Neutral: {self.neutralList}
"""

    def getMatchups(self):
        return self.matchups

    def getMultiplier(self, pkmntype):
        return self.matchups[pkmntype]

    def getType(self):
        return (self.typeCombo[0], self.typeCombo[1])

    def getScore(self):
        return (self.offensiveScore, self.defensiveScore)

    
    
def challenge(pkmn1, pkmn2):
    print("POKEMON 1")
    print(pkmn1)

    print("POKEMON 2")
    print(pkmn2)

    attackTypes = pkmn1.getType()
    for atktype in attackTypes:
        if atktype == 'null':
            break
        multiplier = pkmn2.getMultiplier(atktype)
        print(multiplier)
        if multiplier == 4.:
            pkmn1.offensiveScore += 2
            pkmn2.defensiveScore -= 2
        elif multiplier == 2.:
            pkmn1.offensiveScore += 1
            pkmn2.defensiveScore -= 1
        elif multiplier == 0.5:
            pkmn1.offensiveScore -= 1
            pkmn2.defensiveScore += 1
        elif multiplier == 0.25:
            pkmn1.offensiveScore -= 2
            pkmn2.defensiveScore += 2
        elif multiplier == 0.:
            pkmn1.offensiveScore -= 3
            pkmn2.defensiveScore += 3


def runSim():
    allPkmn = []
    # should be in the form {Type(Grass, Dark): (2, 4)} where the value is (OffensiveScore, DefensiveScore)
    # for i in range(len(pkmntypes.typeList)):
    #     for j in range(i, len(pkmntypes.typeList)):
    #         ptype = pkmntypes.typeList[i]
    #         stype = pkmntypes.typeList[j]
    for i, ptype in enumerate(pkmntypes.typeList):
        for stype in pkmntypes.typeList[i:]:
            if ptype == stype:
                pkmn = Type(ptype)
            else:
                pkmn = Type(ptype, stype)
            print(pkmn)
            allPkmn.append(pkmn)       

    for attacker in allPkmn:
        for defender in allPkmn:
            challenge(attacker, defender)
            # print(attacker)
            # print(attacker.getScore())
            # print(defender)
            # print(defender.getScore())

    with open('types.csv', 'w') as f:
        writer = csv.writer(f)
        for pkmn in allPkmn:
            print(pkmn)
            print(pkmn.getScore())
            writer.writerow([pkmn.getType(), pkmn.getScore()])
        



if __name__ == "__main__":
    runSim()

