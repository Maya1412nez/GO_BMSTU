# l = [8, 4, 1, 5, 6, 2]
# MAX = 999999999999999999999999999999999
# print(MAX)

# def rec(array):
#     if len(array) < 2:
#         return ...
#     else:
#         left, right = array[len(array) // 2], array[len(array) - (len(array) // 2)] 


# def f2(m1, m2) :
#     len1 = len(m1)
#     len2 = len(m2) 
#     res = [0] * (len1 + len2) 
#     i = j = k = 0
#     while k < (len1+len2 + 1):
#         print(k, i, j, res)
#         if m1[i] < m2[j]:
#             res[k] = m1[i]
#             k += 1
#             i += 1
#         else:
#               res[k] = m2[j]
#               k += 1
#               j += 1
#     return res

# print(f2([2, 5, 7], [1, 3, 6])) 






l = [8, 4, 1, 5, 3, 6, 7, 9, 12, 14, 25, 61, 12, 16, 19, 18]

def sovmest(lft, rght):
    MAX = 999999999999999999999999999999999
    i = 0
    j = 0
    result = []
    print(lft, rght)
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
        return sovmest(rec(left), rec(right))

print(rec(l))

