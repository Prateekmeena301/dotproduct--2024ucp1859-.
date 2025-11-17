# vecadd.py
# Program to compute the dot product of two vectors

def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("Both vectors must be of the same length")

    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]

    return result


if __name__ == "__main__":
    # Example vectors
    v1 = [1, 2, 3,0]
    v2 = [4, 5, 6,8]
#added more values in vectors
    print("Vector 1:", v1)
    print("Vector 2:", v2)

    print("Dot Product =", dot_product(v1, v2))

