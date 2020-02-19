class Set:
    def __init__(self, skup = None):
        if skup == None:
            self.stranice = {}
        else:
            self.stranice = skup.stranice

    def add(self, other):
        if other not in self.stranice:
            self.stranice[other] = other
    def __str__(self):
        string = ""
        for stranica in self.stranice:
            string += stranica + "\n"
        return string

    def __copy__(self):
        return Set(self)

    def __or__(self, other):
        konacanSet = Set()
        for key in other.stranice:
            konacanSet.add(key)
        for key in self.stranice:
            konacanSet.add(key)
        return konacanSet

    def komplement(self, other):
        konacanSet = Set()
        for key in self.stranice:
            if key not in other.stranice:
                konacanSet.add(key)
        return konacanSet
        # delete = [key for key in other.stranice if key in self.stranice]
        # for key in delete:
        #     del self.stranice[key]
        # return self

    def __and__(self, other):
        konacanSet = Set()
        for key in self.stranice:
            if key in other.stranice:
                konacanSet.add(key)
        return konacanSet