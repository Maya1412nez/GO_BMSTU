l = [8, 4, 1, 14, 5]
# gg
def sovmest(lft, rght):
    MAX = 999999999999999999999999999999999
    i = 0
    j = 0
    result = []
    # print(lft, rght)
    lft.append(MAX)
    rght.append(MAX)

    while len(result) - 1 < len(rght) + len(lft):
        # print(result, left, i, right, j)
        if lft[i] > rght[j]:
            result.append(rght[j])
            j += 1
        elif rght[j] == lft[i] == MAX:
            return result
        else:
            result.append(lft[i])
            i += 1
    return result

def rec(array):
    if len(array) < 2:
        return array
    else:
        left, right = array[:len(array) // 2], array[(len(array) // 2):] 
        # sovmest(rec(left), rec(right))
        return (sovmest(rec(left), rec(right)))

print(rec(l))
