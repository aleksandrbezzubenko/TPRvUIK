from Simplex import Simplex

if __name__ == '__main__':
    vector_C = [2, 5, 3]
    vector_B = [6, 6, 2]
    vector_Limitation = [[2, 1, 2],
                         [1, 2, 0],
                         [0, 0.5, 1]]
    simplex_method = Simplex(vector_C, vector_B, vector_Limitation)
    print("Исходная симплекс таблица имеет вид:")
    simplex_method.print_simplex_matrix()
    simplex_method.launch()
