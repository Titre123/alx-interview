#!/usr/bin/python3
'''
    ALx Interview Question to rotate a 2-D matrix
'''


def rotate_2d_matrix(matrix):
    '''
        Set the matrix index
    '''
    def rotated(matrix):
        '''
            Rotate the matrix
        '''
        mater = []
        i = len(matrix) - 1
        while i < len(matrix) and i >= 0:
            if i == len(matrix) - 1:
                for ele in matrix[i]:
                    mater.append([])
                    mater[matrix[i].index(ele)].append(ele)
            else:
                for ele in matrix[i]:
                    mater[matrix[i].index(ele)].append(ele)
            i = i - 1
        return mater
    mater = rotated(matrix)
    for ele in mater:
        ind = mater.index(ele)
        matrix[ind] = ele
