def  numbers(N):
    result = []
    for i in range(N, -1 , -1):
        result.append(i)
    return result
N = int(input())
print(numbers(N))