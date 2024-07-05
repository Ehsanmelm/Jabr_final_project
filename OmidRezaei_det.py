from copy import deepcopy

cache = {}

def determinant(matrix, x0, y0, xn, yn) -> float:
    rows, cols = xn - x0, yn - y0
    if rows != cols:
        # print("only square matix accepted")
        return None
    
    key = "{0},{1},{2},{3}".format(x0, y0, xn, yn)
    if key in cache:
        return cache[key]
    
    if rows == 2:
        result = matrix[x0][y0] * matrix[xn-1][yn-1] - matrix[x0][yn-1] * matrix[xn-1][y0]
        cache[key] = result
        return result
    if rows == 1:
        result = matrix[x0][y0]
        cache[key] = result
        return result

    m_11   = determinant(matrix, x0+1, y0+1, xn, yn)
    m_1n   = determinant(matrix, x0+1, y0, xn, yn-1)
    m_n1   = determinant(matrix, x0, y0+1, xn-1, yn)
    m_nn   = determinant(matrix, x0, y0, xn-1, yn-1)
    m_11nn = determinant(matrix, x0+1, y0+1, xn-1, yn-1)
    
    result = m_11 * m_nn - m_1n * m_n1
    if m_11nn != 0:
        result *= (1 / m_11nn)
    cache[key] = result
    return result

# matrix = [[1.2, 4.1, 14.8, 1.0, 1.2],
#                 [6.4, 1.3, 1.6, 1.8, 2.4],
#                 [3.5, 1.8, 8.2, 4.6, 3.8],
#                 [9.1, 5.7, 2.6, 2.4, 4.6],
#                 [1.4, 3.5, 1.0, 8.9, 7.1]]


if __name__ == "__main__":
    dim_num = int(input())
    matrix = []
    for i in range(dim_num):
        input_list = list(map(float , input().split()))
        matrix.append(input_list)
        
    print("{}".format(int(determinant(matrix, 0, 0, dim_num, dim_num))))