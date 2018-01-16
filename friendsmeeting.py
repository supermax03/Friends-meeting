class Friend:
    def __init__(self, days=[]):
        self.days = Set(days)

    def getDaysOff(self):
        return self.days

    DaysOff = property(fget=getDaysOff)


class Set:
    def __init__(self, collection=[]):
        self.collection = collection

    def getCollection(self):
        return self.collection

    def setCollection(self, collection=[]):
        self.collection = collection

    Collection = property(fget=getCollection, fset=setCollection)

    def union(self, other=None):  # Implementa la union entre conjuntos
        result = self.Collection
        for item in other.Collection:
            if not item in result:
                result.append(item)
        return Set(result)

    def minus(self, other=None):  # Implementa la resta entre conjuntos
        result = []
        for item in self.Collection:
            if not item in other.Collection:
                result.append(item)
        return Set(result)

    def intersect(self, other=None):
        result = []
        if isinstance(other, Set):
            for item in self.Collection:
                if item in other.Collection:
                    result.append(item)
        return Set(result)


# Calcula los dias comunes para todos los amigos y los dias no comunes

def common_and_no_common(friends=[]):
    days_in_common = friends[0].DaysOff
    no_common = days_in_common
    for index in range(1, len(friends)):
        item = friends[index].DaysOff
        days_in_common = days_in_common.intersect(item)
        no_common = no_common.union(item)
    return {"days in common": days_in_common.Collection, "no common days": no_common.minus(days_in_common).Collection}


if __name__ == '__main__':
    a = Friend([1, 2, 3, 5])
    b = Friend([2, 3, 5])
    c = Friend([5, 6, 7])
    d = Friend([5, 6])
    friends = [a, b, c, d]
    result = common_and_no_common(friends)
    print result
