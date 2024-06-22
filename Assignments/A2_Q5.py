def print_pascals_triangle(n):
    triangle = [[1 for _ in range(i+1)] for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    for row in triangle:
        print(' '.join(str(num) for num in row))

n = int(input("Enter the Number :  "))
print_pascals_triangle(n)