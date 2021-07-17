def sparse_matrix_multiplication(matrix_a, matrix_b):
    # Write your code here.
    # In case the matrices are not compatible or one is empty
    if((matrix_a == None or matrix_b == None) or (len(matrix_a[0]) != len(matrix_b))):
        return [[]]
    # NEVER DO THIS !!!!
    #               vvvvvvvvvvvvvvvvvvv
    # YOU ARE CREATING DUPLICATES OF THE SAME POINTER PER ROW
    # returnMatrix = [[0]*len(matrix_b[0])]*len(matrix_a)
    returnMatrix = [[0 for i in range(len(matrix_b[0]))] for j in range(len(matrix_a))] 
    for i in range(len(matrix_b[0])):
        for j in range(len(matrix_a)):
            summation = 0
            for k in range(len(matrix_a[0])):
                if(matrix_a[j][k] == 0 or matrix_b[k][i] == 0):
                    continue
                summation += matrix_a[j][k] * matrix_b[k][i]
            returnMatrix[j][i] += summation
    return returnMatrix

def main():
    matrix_a = [[0, 0, 1], [0, 1, 2], [0, 0, 1]]
    matrix_b = [[0, 1, 0], [1, 1, 0], [0, 1, 0]]
    answer_matrix = sparse_matrix_multiplication(matrix_a, matrix_b)
    print(answer_matrix)
    return 0

main()
