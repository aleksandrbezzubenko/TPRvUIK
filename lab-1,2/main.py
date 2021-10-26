from Simplex import Simplex

if __name__ == '__main__':
    print("Прямая задача линейного программирования")
    vector_C = [2, 5, 3]
    vector_B = [6, 6, 2]
    vector_Limitation = [[2, 1, 2],
                         [1, 2, 0],
                         [0, 0.5, 1]]
    simplex_method = Simplex(vector_C, vector_B, vector_Limitation, "ПЗ ЛП")
    print("Исходная симплекс таблица имеет вид:")
    simplex_method.print_simplex_matrix()
    simplex_method.launch()

    print("\nДвойственная задача линейного программирования")
    vector_C_2 = [2, 6, 7]
    vector_B_2 = [3, 8, 1]
    vector_Limitation_2 = [[3, 1, 1],
                           [1, 2, 0],
                           [0, 0.5, 2]]
    simplex_method_2 = Simplex(vector_C_2, vector_B_2, vector_Limitation_2, "ДЗ ЛП", need_transposition=True)
    print("Исходная симплекс таблица имеет вид:")
    simplex_method_2.print_simplex_matrix()
    simplex_method_2.launch()
