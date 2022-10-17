import math
#import numpy as np

def multiply2(matrix1, matrix2):
    matrixtemp = []
    for k in range(len(matrix1)):
        matrixtemp.append([])
        for m in range(len(matrix2)):
            matrixtemp[k].append(mult(getnxt(matrix1, k), getcol(matrix2, m)))
            
    return matrixtemp

def mult(nxt, col):
    try:
        sizenxt = len(nxt)
        sizecol = len(col)
        if (sizenxt != sizecol):
            raise ValueError("Exception")
        res = sum([nxt[k] * col[k] for k in range(sizenxt)])
        return res
    except ValueError:
        print("not same length of row and column")
        
def getcol(matrix, numcol):
    size = len(matrix)
    col = [matrix[k] [numcol] for k in range(size)]
    return col

def getnxt(matrix, numnxt):
    nxt = matrix[numnxt]
    return nxt

def matrixbyvector(vector, matrix_):
    tempvaluesMatrix = []
    matrixtemp = []
    counter = 0
    rowcounter = 0
    
    for row in matrix_:
        if (rowcounter != 0):
            rowcounter += 1
        tempvaluesMatrix.append([])
        if counter == len(vector):
            counter = 0
            if (rowcounter == 0):
                rowcounter += 1
        for value in row:
            tempval = value * vector[counter]
            tempvaluesMatrix[rowcounter].append(tempval)
            counter += 1
            
    for row in tempvaluesMatrix:
        sumOf = sum(row)
        matrixtemp.append(sumOf)
        
    return matrixtemp

def array(arr):
    arrays = []
    for i in arr:
        arrays.append(i)
    return arrays

def negativeArray(arr):
    arrays = []
    for i in arr:
        val = -i
        arrays.append(val)
    return arrays

def dot_twoVectorsOfSameSize(vec1, vec2):
    arrays = []
    for i in range(len(vec1)):
        val = vec1[i] * vec2[i]
        arrays.append(val)
        
    return sum(arrays)

def subtract_twoVectorsOfSameSize(vec1, vec2):
    arrays = []
    for i in range(len(vec1)):
        val = vec1[i] - vec2[i]
        arrays.append(val)
    return arrays

def cross_twoVectorsOfOneByThree(vec1, vec2):
    arrays = []
        
    val = (vec1[1] * vec2[2]) - (vec1[2] * vec2[1])
    arrays.append(val)
    val = -((vec1[0] * vec2[2]) - (vec1[2] * vec2[0]))
    arrays.append(val)
    val = (vec1[0] * vec2[1]) - (vec1[1] * vec2[0])
    arrays.append(val)
    
    return arrays

def norm(vec):
    array = []
    for i in vec:
        array.append(i*i)
    return math.sqrt(sum(array))
    

def vectorDivideByNumber(vec, num):
    array = []
    for i in vec:
        try:
            array.append(float(i/num))
        except:
            pass
    return array
    

def vectorMultiplyByNumber(vec, num):
    array = []
    for i in vec:
        try:
            array.append(float(i*num))
        except:
            pass
    return array
   
        
def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[c][r] = cofactors[c][r]/determinant
            
    counter = 0        
    matrix = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    for i in cofactors:
        matrix[0][counter] = i[0]
        matrix[1][counter] = i[1]
        matrix[2][counter] = i[2]
        matrix[3][counter] = i[3]
        counter = counter + 1
    return matrix

def getMatrixValue(matrix, row, value):
    return(matrix[row][value])


def sum_twoVectorsOneByThree(vector1, vector2):
    vector = []
    vector.append(vector1[0] + vector2[0])
    vector.append(vector1[1] + vector2[1])
    vector.append(vector1[2] + vector2[2])

    return vector
    
def mult_twoVectorsOneByThree(vector1, vector2):
    vector = []
    
    vector.append(vector1[0] * vector2[0])
    vector.append(vector1[0] * vector2[0])
    vector.append(vector1[0] * vector2[0]) 

    return vector
    

def subtract_twoVectorsOfSameSize2(vec1, vec2):
    arrays = []
    for i in range(len(vec1)):
        print(vec1[i], vec2[i])
        val = vec1[i] - vec2[i]
        arrays.append(val)
    print(arrays)
    return arrays
    
    
    
    
    
    
    