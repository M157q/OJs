# http://www.checkio.org/mission/building-base/

class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        '''
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height
        '''

        # http://stackoverflow.com/questions/8682848/assign-function-arguments-to-self
        vars(self).update({k: v for k, v in locals().items() if k != 'self'})

    def corners(self):
        NS = {
            'south': self.south,
            'north': self.south + self.width_NS,
        }
        WE = {
            'west': self.west,
            'east': self.west + self.width_WE,
        }

        return {"{}-{}".format(ns, we): [NS[ns], WE[we]] for ns in NS for we in WE}


    def area(self):
        return self.width_WE * self.width_NS

    def volume(self):
        return self.area() * self.height

    def __repr__(self):
        return "Building({self.south}, {self.west}, {self.width_WE}, {self.width_NS}, {self.height})".format(self=self)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
