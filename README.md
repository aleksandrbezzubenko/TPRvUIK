# TPRvUIK
 
## Вывод программы в консоль:

```
Прямая задача линейного программирования

Исходная симплекс таблица имеет вид:
Симплекс таблица
+----+----+----+-----+----+
|    | S0 | X1 |  X2 | X3 |
+----+----+----+-----+----+
| X4 | 6  | 2  |  1  | 2  |
| X5 | 6  | 1  |  2  | 0  |
| X6 | 2  | 0  | 0.5 | 1  |
| F  | 0  | 2  |  5  | 3  |
+----+----+----+-----+----+
Нахождение опорного решения:
Так как элементы S0 неотрицательны -> опорное решение
Нахождение оптимального решения:
Разрешающий столбец: X2
Разрешающая строка: X5
Производим замену: X2 <-> X5
Симплекс таблица
+----+-------+-------+-------+-----+
|    |   S0  |   X1  |   X5  |  X3 |
+----+-------+-------+-------+-----+
| X4 |  3.0  |  1.5  |  -0.5 | 2.0 |
| X2 |  3.0  |  0.5  |  0.5  | 0.0 |
| X6 |  0.5  | -0.25 | -0.25 | 1.0 |
| F  | -15.0 |  -0.5 |  -2.5 | 3.0 |
+----+-------+-------+-------+-----+
Проверка:
F  =  2*0 + 5*3.0 + 3*0  =  15.0
Нахождение опорного решения:
Так как элементы S0 неотрицательны -> опорное решение
Нахождение оптимального решения:
Разрешающий столбец: X3
Разрешающая строка: X6
Производим замену: X3 <-> X6
Симплекс таблица
+----+-------+-------+-------+------+
|    |   S0  |   X1  |   X5  |  X6  |
+----+-------+-------+-------+------+
| X4 |  2.0  |  2.0  |  0.0  | -2.0 |
| X2 |  3.0  |  0.5  |  0.5  | -0.0 |
| X3 |  0.5  | -0.25 | -0.25 | 1.0  |
| F  | -16.5 |  0.25 | -1.75 | -3.0 |
+----+-------+-------+-------+------+
Проверка:
F  =  2*0 + 5*3.0 + 3*0.5  =  16.5
Нахождение опорного решения:
Так как элементы S0 неотрицательны -> опорное решение
Нахождение оптимального решения:
Разрешающий столбец: X1
Разрешающая строка: X4
Производим замену: X1 <-> X4
Симплекс таблица
+----+--------+-------+-------+-------+
|    |   S0   |   X4  |   X5  |   X6  |
+----+--------+-------+-------+-------+
| X1 |  1.0   |  0.5  |  0.0  |  -1.0 |
| X2 |  2.5   | -0.25 |  0.5  |  0.5  |
| X3 |  0.75  |  0.12 | -0.25 |  0.75 |
| F  | -16.75 | -0.12 | -1.75 | -2.75 |
+----+--------+-------+-------+-------+
Проверка:
F  =  2*1.0 + 5*2.5 + 3*0.75  =  16.75
Нахождение опорного решения:
Так как элементы S0 неотрицательны -> опорное решение
Нахождение оптимального решения:
Оптимальное решение:
X1 = 1.0
X2 = 2.5
X3 = 0.75
F =  16.75

Двойственная задача линейного программирования

Исходная симплекс таблица имеет вид:
Симплекс таблица
+----+----+----+----+------+
|    | S0 | Y1 | Y2 |  Y3  |
+----+----+----+----+------+
| Y4 | -2 | -3 | -1 |  0   |
| Y5 | -6 | -1 | -2 | -0.5 |
| Y6 | -7 | -1 | 0  |  -2  |
| G  | 0  | -3 | -8 |  -1  |
+----+----+----+----+------+
Нахождение опорного решения:
Разрешающая строка: Y4
Разрешающий столбец: Y1
Производим замену: Y1 <-> Y4
Симплекс таблица
+----+-------+-------+-------+------+
|    |   S0  |   Y4  |   Y2  |  Y3  |
+----+-------+-------+-------+------+
| Y1 |  0.67 | -0.33 |  0.33 | -0.0 |
| Y5 | -5.33 | -0.33 | -1.67 | -0.5 |
| Y6 | -6.33 | -0.33 |  0.33 | -2.0 |
| G  |  2.0  |  -1.0 |  -7.0 | -1.0 |
+----+-------+-------+-------+------+
Проверка:
G  =  -3*0.67 + -8*0 + -1*0  =  -2.0100000000000002
Нахождение опорного решения:
Разрешающая строка: Y5
Разрешающий столбец: Y4
Производим замену: Y4 <-> Y5
Симплекс таблица
+----+------+------+------+------+
|    |  S0  |  Y5  |  Y2  |  Y3  |
+----+------+------+------+------+
| Y1 | 6.0  | -1.0 | 2.0  | 0.5  |
| Y4 | 16.0 | -3.0 | 5.0  | 1.5  |
| Y6 | -1.0 | -1.0 | 2.0  | -1.5 |
| G  | 18.0 | -3.0 | -2.0 | 0.5  |
+----+------+------+------+------+
Проверка:
G  =  -3*6.0 + -8*0 + -1*0  =  -18.0
Нахождение опорного решения:
Разрешающая строка: Y6
Разрешающий столбец: Y5
Производим замену: Y5 <-> Y6
Симплекс таблица
+----+------+------+------+-----+
|    |  S0  |  Y6  |  Y2  |  Y3 |
+----+------+------+------+-----+
| Y1 | 7.0  | -1.0 | 0.0  | 2.0 |
| Y4 | 19.0 | -3.0 | -1.0 | 6.0 |
| Y5 | 1.0  | -1.0 | -2.0 | 1.5 |
| G  | 21.0 | -3.0 | -8.0 | 5.0 |
+----+------+------+------+-----+
Проверка:
G  =  -3*7.0 + -8*0 + -1*0  =  -21.0
Нахождение опорного решения:
Так как элементы S0 неотрицательны -> опорное решение
Нахождение оптимального решения:
Разрешающий столбец: Y3
Разрешающая строка: Y5
Производим замену: Y3 <-> Y5
Симплекс таблица
+----+-------+-------+-------+-------+
|    |   S0  |   Y6  |   Y2  |   Y5  |
+----+-------+-------+-------+-------+
| Y1 |  5.67 |  0.33 |  2.67 | -1.33 |
| Y4 |  15.0 |  1.0  |  7.0  |  -4.0 |
| Y3 |  0.67 | -0.67 | -1.33 |  0.67 |
| G  | 17.67 |  0.33 | -1.33 | -3.33 |
+----+-------+-------+-------+-------+
Проверка:
G  =  -3*5.67 + -8*0 + -1*0.67  =  -17.68
Нахождение опорного решения:
Так как элементы S0 неотрицательны -> опорное решение
Нахождение оптимального решения:
Разрешающий столбец: Y6
Разрешающая строка: Y4
Производим замену: Y6 <-> Y4
Симплекс таблица
+----+-------+-------+-------+------+
|    |   S0  |   Y4  |   Y2  |  Y5  |
+----+-------+-------+-------+------+
| Y1 |  0.67 | -0.33 |  0.33 | -0.0 |
| Y6 |  15.0 |  1.0  |  7.0  | -4.0 |
| Y3 | 10.67 |  0.67 |  3.33 | -2.0 |
| G  | 12.67 | -0.33 | -3.67 | -2.0 |
+----+-------+-------+-------+------+
Проверка:
G  =  -3*0.67 + -8*0 + -1*10.67  =  -12.68
Нахождение опорного решения:
Так как элементы S0 неотрицательны -> опорное решение
Нахождение оптимального решения:
Оптимальное решение:
Y1 = 0.67
Y2 = 0
Y3 = 10.67
G =  -12.67

```
