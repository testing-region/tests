# 1. a dictionary
# 2. Group keys that point to the same value
# 3. Make the a list of the groups
# 4. set the value as a key.
# 5. The new value will be the grouped keys.
# 6. return a new dictionary

def inverse(old_dict):
    new_dict = {}  # hold the reverse dictionary
    keys = []  # holds the keys for the reversed dictionary
    values = []  # a list of lists that holds a group of keys

    for k, v in old_dict.items():
        # if the value is already present in the keys
        if v in keys:
            values[keys.index(v)].append(k)
        else:
            # if the value does not exist in keys
            keys.append(v)
            values.append([k])

    for k, v in zip(keys, values):
        new_dict[k] = v

    return new_dict


hist = {
    "a": 1,
    "p": 1,
    "r": 2,
    "t": 1,
    "o": 1,
}

print(inverse(hist))
