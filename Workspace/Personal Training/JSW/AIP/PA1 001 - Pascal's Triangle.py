import math
def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = []
        for j in range(i+1):
            row.append(math.comb(i, j))
        triangle.append(row)

    return triangle
def print_pascals_triangle(triangle):
    n = len(triangle[-1])
    for row in triangle:
        print(f"{" ".join(map(str, row)):^{2*n-1}}")

if __name__ == "__main__":

    n = int(input())

    pascal_triangle = generate_pascals_triangle(n)

    print_pascals_triangle(pascal_triangle)

