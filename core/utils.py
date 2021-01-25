def u_map(callback, array):
    for i in range(len(array)):
        array[i] = callback(array[i], i)


def u_find(callback, array):
    for i in range(len(array)):
        if callback(array[i], i):
            return array[i]
    return None