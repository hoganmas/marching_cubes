#!/usr/bin/env python3
from setup import *
from cases import *



V = np.array([
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, 1, -1],
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, 1],
])


def make_hstack(verts):
    if len(verts) == 0:
        return np.array([])
    return np.hstack([
        np.reshape(V[vert], (3, 1)) for vert in verts
    ])


def make_basis(i, j, k):
    return make_hstack([i, j, k])



base_cases = [
    [],     # 0
    [0],    # 1
    [0, 1], # 2
    [0, 2], # 3
    [0, 6], # 4
    [0, 1, 2],  # 5
    [0, 1, 6],  # 6
    [0, 2, 5],  # 7
    [0, 1, 2, 3],   # 8
    [0, 1, 3, 4],   # 9
    [0, 2, 4, 6],   # 10
    [0, 2, 3, 6],   # 11
    [0, 2, 3, 5],   # 12
    [0, 2, 5, 7]    # 13
]



def get_valid_bases():
    bases = []

    for i in range(8):
        adjs = []
        for j in range(8):
            if adjacent(i, j):
                adjs.append(j)
        
        for j in adjs:
            for k in adjs:
                if j != k:
                    bases.append([i, j, k])
            """
            for k in range(8):
                if adjacent(i, j) and adjacent(j, k) and adjacent(k, i):
                    bases.append([i, j, k])
                if i == j or j == k or k == i:
                    continue
                elif opposite(i,j) or opposite(j,k) or opposite(k,i):
                    continue
                else:
                    bases.append([i, j, k])
            """
    return bases



def get_default_inv():
    return np.linalg.inv(make_basis(0, 3, 4))


if __name__ == '__main__':

    output_array = []

    valid_bases = get_valid_bases()
    default_inv = get_default_inv()

    # For each combination of vertices
    for x in range(256):

        if x == 0 or x == 255:
            #print(x, '--> (case = 0)')
            output_array.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            continue
        
        # Get case
        c = get_case(x)

        for basis in valid_bases:
            this_basis = make_basis(basis[0], basis[1], basis[2])

            A = this_basis @ default_inv @ make_hstack(base_cases[c])

            nums, inverted = get_nums(x)
            B = make_hstack(nums)

            Auniq = np.unique(A, axis=1)
            Buniq = np.unique(B, axis=1)

            if np.all(np.equal(Auniq, Buniq)):
                #print(x, '--> (case =', c, ", inverted =", int(inverted), ", basis =", basis, ')')
                #output_array.append([c, int(inverted), basis[0], basis[1], basis[2]])

                # We have currently found maps for 0, 3, 4 (default inv)                
                localMap = [basis[0], -1, -1, basis[1], basis[2], -1, -1, -1]

                # Find map for 1
                for i in range(8):
                    if i not in localMap and adjacent(i, localMap[0]):
                        localMap[1] = i
                        break
                
                for i in range(8):
                    if opposite(i, localMap[0]):
                        localMap[6] = i
                    elif opposite(i, localMap[1]):
                        localMap[7] = i
                    elif opposite(i, localMap[3]):
                        localMap[5] = i
                    elif opposite(i, localMap[4]):
                        localMap[2] = i

                output_array.append([c, int(inverted)] + localMap)
                break
    print('{')
    for i in range(len(output_array)):
        line = '{'
        for j in range(9):
            line += ' ' + str(output_array[i][j]) + ','
        line += ' ' + str(output_array[i][9]) + ' },'
        print(line)

    print('}')

