def even(N):
    result = []
    for i in range(N + 1):
        if i % 2 == 0:
            result.append(i)
    return result
N = int(input())
print(even(N))