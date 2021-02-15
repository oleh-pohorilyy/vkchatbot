def u_map(callback, array):
    outarray = []
    for i in range(len(array)):
        outarray.append(callback(array[i], i))
    return outarray


def u_find(callback, array):
    for i in range(len(array)):
        if callback(array[i], i):
            return array[i]
    return None
