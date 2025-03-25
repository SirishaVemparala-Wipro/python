matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Primary Diagonal Elements:", [matrix[i][i] for i in range(3)])

print("Secondary Diagonal Elements:", [matrix[i][2 - i] for i in range(3)])
