# www.checkio.org/mission/friends/

class Friends:
    def __init__(self, connections):
        self.connections = list(connections)


    def add(self, connection):
        if connection in self.connections:
            return False

        self.connections.append(connection)
        return True


    def remove(self, connection):
        if connection not in self.connections:
            return False

        self.connections.remove(connection)
        return True


    def names(self):
        return set.union(*self.connections)


    def connected(self, name):
        connected_nodes = set()

        if name in self.names():
            for connection in self.connections:
                if name in connection:
                    connected_nodes.update(connection)
            connected_nodes.remove(name)

            # connected_nodes.union(*(connection.difference({name}) for connection in self.connections if name in connection))

        return connected_nodes



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
