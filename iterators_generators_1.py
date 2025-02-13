def square(N):
    result = []
    for i in range(N + 1):
        result.append(i**2)
    return result
N = int(input())
print(square(N))