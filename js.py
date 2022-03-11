class Character:
    def __init__(self, name, phrase1, phrase2, level):
        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2
        self.level = level
    def speak(self, phraseNum):
        if phraseNum == 1:
            print(self.phrase1)
        elif phraseNum == 2:
            print(self.phrase2)
    def setLevel(self,level):
        self.level = level
        print(level)

c1 = Character("Kung Fu Panda", "Skadoosh babaga", "BAKANA KONO DIO DA", 1000)
c2 = Character("Ayankoji", "omg liek are we equal!??!?!", "I have no friends.", 1)
c1.speak(1)
c2.setLevel(2)
c1.speak(2)