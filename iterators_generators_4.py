def  squares(a, b):
    result = []
    for i in range(a, b + 1):
        result.append(i**2)
    return result
a = int(input())
b = int(input())
print(squares(a, b))