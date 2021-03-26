arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
compressed_arr = []
while len(arr) != 0:
    if len(arr) == 1:
        compressed_arr.append(arr[0])
        arr.pop()
    else:
        new = arr[0] + arr[-1]
        compressed_arr.append(new)
        arr = arr[1:-1]

print(compressed_arr)
    

