def container(data, n):
    for value in data:
        if n == value:
            return True
    return False
print("3 is present so",container([1, 5, 8, 3], 3))
print("-1 is not present so" ,container([1,5, 8, 3], -1))
