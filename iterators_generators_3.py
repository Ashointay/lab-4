def  divisible_3_4(N):
    result = []
    for i in range(N + 1):
        if i % 3 == 0 and i % 4 == 0:
            result.append(i)
    return result
N = int(input())
print(divisible_3_4(N))