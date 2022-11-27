def set_(coll, path, value):
    new = coll
    for i in path[:-1]:
        if i in new:
            new = new[i]
        else:
            new[i] = {}
            new = new[i]
        new[path[-1]] = value


coll = {"a": {"b": {"c": 3}}}
print(set_(coll, ["a", "b", "c"], 4))
print(coll["a"]["b"]["c"])
print(set_(coll, ['x', 'y', 'z'], 5))
print(coll['x']['y']['z'])
