import numpy as np
from prettytable import PrettyTable
import sys


class Simplex(object):

    def __init__(self, vector_C, vector_B, vector_limitation, row_names = None, col_names = None, origin_vec_c=None):
        self.vec_c = vector_C
        if (len(self.vec_c) == len(vector_limitation[0])):
            self.vec_c.insert(0, 0)
        self.vec_b = vector_B
        self.simplex_matrix = vector_limitation
        for i in range(len(self.vec_b)):
            self.simplex_matrix[i].insert(0, self.vec_b[i])

        self.res_row = 0
        self.res_col = 0
        self.flag_solution = False

        if (row_names is None) and (col_names is None):
            self.col_names = ["S0"]
            self.row_names = []
            for i in range(len(self.vec_b)):
                self.col_names.append(f"X{i + 1}")
                self.row_names.append(f"X{i + 4}")
            self.row_names.append("F ")
        else:
            self.col_names = col_names
            self.row_names = row_names

        if (origin_vec_c is None):
            self.origin_vec_c = vector_c
        else:
            self.origin_vec_c = origin_vec_c


        self.simplex_matrix.append(self.vec_c)

    def print_simplex_matrix(self):
        print("Симплекс таблица")
        mytable = PrettyTable()
        fields = [' ']
        for elem in self.col_names:
            fields.append(elem)
        mytable.field_names = fields
        for i in range(int(len(self.vec_b)) + 1):
            row = [str(self.row_names[i])]
            for j in range(int(len(self.vec_c))):
                row.append(str(np.round(self.simplex_matrix[i][j], 2)))
            mytable.add_row(row)
        print(mytable)

    # нахождение результирующих строк и столбцов при опорном решении
    def get_res_elements(self):  #
        for i in range(int(len(self.vec_b))):
            if (self.flag_solution == True):
                continue
            if (self.simplex_matrix[i][0] < 0):
                self.res_row = i
                for j in range(len(self.vec_c) - 1):
                    if (self.flag_solution == True):
                        continue
                    if (self.simplex_matrix[i][j] < 0) and (j != 0):
                        self.res_col = j
                        self.flag_solution = True
                min = sys.maxsize
                for j in range(int(len(self.simplex_matrix)) - 1):
                    if (self.simplex_matrix[j][self.res_col] != 0):
                        tmp = self.simplex_matrix[j][0] / self.simplex_matrix[j][self.res_col]
                        if (tmp > 0) and (tmp < min):
                            self.res_row = j
                            min = tmp
        if (self.flag_solution == True):
            print("Разрешающая строка:", self.row_names[self.res_row])
            print("Разрешающий столбец:", self.col_names[self.res_col])

    # нахождение результирующих строк и столбцов при оптимальном решении
    def get_optimum_res_elements(self):  #
        max_col = max(self.simplex_matrix[len(self.vec_b)])
        self.res_col = self.simplex_matrix[len(self.vec_b)].index(max_col)
        min_row = sys.maxsize
        for j in range(int(len(self.vec_b))):
            if (self.simplex_matrix[j][self.res_col] != 0):
                tmp = self.simplex_matrix[j][0] / self.simplex_matrix[j][self.res_col]
                if (tmp > 0) and (tmp < min_row):
                    self.res_row = j
                    min_row = tmp
                    self.flag_solution = True

        if (self.flag_solution == True):
            print("Разрешающий столбец:", self.col_names[self.res_col])
            print("Разрешающая строка:", self.row_names[self.res_row])

    # проверка результата
    def check_result(self):
        print("Проверка:")
        terms = []
        for i in range(len(self.row_names) - 1):
            if f"{self.var_name}{i + 1}" in self.row_names:
                terms.append(np.round(self.simplex_matrix[self.row_names.index(f"{self.var_name}{i + 1}")][0], 2))
            else:
                terms.append(0)
        result = 0
        print(f"{self.func_name} = ", end='')
        for i in range(len(terms)):
            result += self.origin_vec_c[i + 1] * terms[i]
            if (i == (len(terms) - 1)):
                print(f" {self.origin_vec_c[i + 1]}*{terms[i]}", ' ',end='')
            else:
                print(f" {self.origin_vec_c[i + 1]}*{terms[i]}", '+', end='')
        print("= ", result)
    

    def change_basis(self):

        self.row_names[self.res_row], self.col_names[self.res_col] =\
            self.col_names[self.res_col], self.row_names[self.res_row]
        pivot_value = self.simplex_matrix[self.res_row][self.res_col]
        matrix_size = len(self.simplex_matrix[0])
        tmp_matrix = np.zeros((matrix_size, matrix_size))

        tmp_matrix[self.res_row][self.res_col] = 1 / self.simplex_matrix[self.res_row][self.res_col]

        # разрещающая строка
        for j in range(matrix_size):
            if j == self.res_col:
                continue
            tmp_matrix[self.res_row][j] = self.simplex_matrix[self.res_row][j] / pivot_value

        # разрещающий столбец
        for i in range(matrix_size):
            if i == self.res_row:
                continue
            tmp_matrix[i][self.res_col] = - self.simplex_matrix[i][self.res_col] / pivot_value

        # остальные элементы симплекс таблицы
        for i, j in [(i, j) for i in range(matrix_size) for j in range(matrix_size)]:
            if i == self.res_row or j == self.res_col:
                continue
            tmp_matrix[i][j] = self.simplex_matrix[i][j] - self.simplex_matrix[self.res_row][j]\
                               * self.simplex_matrix[i][self.res_col] / pivot_value

        # выведение нового вектора коэффициентов целевой функции,
        # матрицы системы ограничений и вектора правой части системы ограничений
        self.simplex_matrix = tmp_matrix.tolist()
        new_vector_c = list(tmp_matrix[matrix_size - 1])
        new_matrix = np.zeros((matrix_size - 1, matrix_size - 1))
        for i in range(matrix_size - 1):
            for j in range(matrix_size - 1):
                new_matrix[i][j] = tmp_matrix[i][j + 1]
        new_matrix = new_matrix.tolist()
        new_vector_b = []
        for i in range(len(self.vec_b)):
            new_vector_b.append(tmp_matrix[i][0])
        self.print_simplex_matrix()
        self.check_result()


        # применение симплекс-метода над новым вариантом симплекс-таблицы
        new_simplex_matrix = Simplex(new_vector_c, new_vector_b, new_matrix, self.row_names, self.col_names, origin_vec_c=self.origin_vec_c)
        self.flag_solution = new_simplex_matrix.launch()

    # проверка наличия опорного решения системы
    def check_negative_vector_b(self):
        for i in range(len(self.vec_b)):
            if (self.simplex_matrix[i][0] < 0):
                return True
        return False

    # проверка наличия оптимального решения системы
    def check_positive_vector_c(self):
        for i in range(len(self.vec_c)):
            if (self.simplex_matrix[len(self.vec_b)][i] > 0) and (i != 0):
                return True
        return False

    def launch(self):
        print("Нахождение опорного решения:")
        self.flag_solution = False
        self.flag_check = self.check_negative_vector_b()
        if (self.flag_check == True):
            self.get_res_elements()
            if (self.flag_solution == True):
                print("Производим замену:", self.col_names[self.res_col], "<->",
                      self.row_names[self.res_row])
                self.change_basis()
        else:
            print("Так как элементы S0 неотрицательны -> опорное решение")
        if (self.flag_solution == False) and (self.flag_check == True):
            print("Не имеет опорного решения")
        else:
            print("Нахождение оптимального решения:")
            self.flag_solution = False
            self.flag_check = self.check_positive_vector_c()
            if (self.flag_check == True):
                self.get_optimum_res_elements()
                if (self.flag_solution == True):
                    print("Производим замену:", self.col_names[self.res_col], "<->",
                          self.row_names[self.res_row])
                    self.change_basis()
                else:
                    print("Имеет опорное решение, не имеет оптимального решения")
                    return False

            if (self.flag_solution == False):
                print("Оптимальное решение:")
                answer = []
                for i in range(len(self.row_names) - 1):
                    if f"X{i + 1}" in self.row_names:
                        answer.append(np.round(self.simplex_matrix[self.row_names.index(f"X{i + 1}")][0], 2))
                    else:
                        answer.append(0)
                for i in range(len(answer)):
                    print(f"X{i + 1}", "=", answer[i])
                print("F = ", -np.round(self.simplex_matrix[len(self.row_names) - 1][0], 2))
                return True
