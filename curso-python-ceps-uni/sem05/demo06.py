a = [[1, 2, 3], [4, 5, 6]]
print(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()