import pkmntypes

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

    def isWeakTo(self, pkmntype):
        return pkmntype in self.weakList

    def isResistantTo(self, pkmntype):
        return pkmntype in self.resistList

    def isImmuneTo(self, pkmntype):
        return pkmntype in self.immuneList

    def isNeutralTo(self, pkmntype):
        return pkmntype in self.neutralList

    def getMultiplier(self, pkmntype):
        return self.matchups[pkmntype]

    def getPrimaryType(self):
        return self.typeCombo[0]

    def getSecondaryType(self):
        return self.typeCombo[1]
    
def challenge(pkmn1, pkmn2):
    print("POKEMON 1")
    print(pkmn1)

    print("POKEMON 2")
    print(pkmn2)

    print("POKEMON 1 ATTACKING POKEMON 2")
    





if __name__ == "__main__":
    pkmn1 = Type(pkmntypes.grass, pkmntypes.dark)
    print(pkmn1)
    print(pkmn1.getMatchups())
    print(pkmn1.isWeakTo('fire'))
    print(pkmn1.isWeakTo('grass'))
    print(pkmn1.isResistantTo('grass'))
    print(pkmn1.isResistantTo('electric'))
    print(pkmn1.isImmuneTo('grass'))
    print(pkmn1.isImmuneTo('psychic'))
    print(pkmn1.isNeutralTo('grass'))
    print(pkmn1.isNeutralTo('rock'))
    print(pkmn1.getMultiplier('normal'))
    print(pkmn1.getMultiplier('bug'))


